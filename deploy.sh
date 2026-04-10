#!/bin/zsh
#
# Incremental Quarto render + Netlify deploy
#
# Usage: ./deploy.sh "Your commit message"
#    or: ./deploy.sh --full "message"   (force full render)

set -e
cd "$(dirname "$0")"

# --- Parse args ---
FULL_RENDER=false
if [ "$1" = "--full" ]; then
    FULL_RENDER=true
    shift
fi

if [ -z "$1" ]; then
    echo "Usage: ./deploy.sh [--full] \"Your commit message\""
    exit 1
fi

MESSAGE="$1"
T_START=$SECONDS

# --- Listing pages that must re-render when their content dirs change ---
typeset -A LISTING_PAGES=(
    posts       posts.qmd
    background  background.qmd
    Presentations presentations.qmd
    jotter      jotter.qmd
)

# --- Global files that trigger a full render ---
GLOBAL_PATTERN='_quarto\.yml|styles\.css|flexoki-light\.scss|_metadata\.yml|apa\.csl|references\.bib'

# --- Detect changes (staged + unstaged vs last commit) ---
CHANGED=$(git diff --name-only HEAD 2>/dev/null)
STAGED=$(git diff --name-only --cached 2>/dev/null)
ALL_CHANGED=$(echo -e "$CHANGED\n$STAGED" | sort -u | grep -v '^$')

if [ -z "$ALL_CHANGED" ]; then
    echo "No changes detected. Nothing to render or deploy."
    exit 0
fi

echo "Changed files:"
echo "$ALL_CHANGED" | sed 's/^/  /'
echo ""

# --- Decide: full or incremental render ---
T_RENDER=$SECONDS
if $FULL_RENDER; then
    echo "=== Full render (--full flag) ==="
    quarto render
elif echo "$ALL_CHANGED" | grep -qE "$GLOBAL_PATTERN"; then
    echo "=== Full render (global config changed) ==="
    quarto render
else
    echo "=== Incremental render ==="
    RENDERED_LISTINGS=""

    # Render changed content files
    for f in $(echo "$ALL_CHANGED" | grep -E '\.(md|qmd)$'); do
        [ -f "$f" ] || continue

        # Skip listing pages (we handle them below)
        IS_LISTING=false
        for lp in ${(v)LISTING_PAGES}; do
            [ "$f" = "$lp" ] && IS_LISTING=true && break
        done
        $IS_LISTING && continue

        echo "  Rendering: $f"
        quarto render "$f"
    done

    # Re-render listing pages whose content directories were touched
    for dir in ${(k)LISTING_PAGES}; do
        if echo "$ALL_CHANGED" | grep -q "^${dir}/"; then
            echo "  Rendering listing: ${LISTING_PAGES[$dir]} (${dir}/ changed)"
            quarto render "${LISTING_PAGES[$dir]}"
        fi
    done

    # Re-render index.md if posts changed (front page references recent posts)
    if echo "$ALL_CHANGED" | grep -q "^posts/"; then
        echo "  Rendering: index.md (posts changed)"
        quarto render index.md 2>/dev/null || true
    fi

    echo ""
    echo "=== Incremental render complete ==="
fi

# --- Deploy to Netlify ---
T_DEPLOY=$SECONDS
echo ""
echo "Deploying _site/ to Netlify..."
netlify deploy --prod --dir _site

# --- Git commit and push (for history, not build trigger) ---
T_GIT=$SECONDS
echo ""
echo "Committing and pushing to git..."
git add .
git commit -m "$MESSAGE"
git push

# --- Timing summary ---
T_END=$SECONDS
echo ""
echo "=== Timing ==="
printf "  Render:  %dm %ds\n" $(( (T_DEPLOY - T_RENDER) / 60 )) $(( (T_DEPLOY - T_RENDER) % 60 ))
printf "  Deploy:  %dm %ds\n" $(( (T_GIT - T_DEPLOY) / 60 )) $(( (T_GIT - T_DEPLOY) % 60 ))
printf "  Git:     %dm %ds\n" $(( (T_END - T_GIT) / 60 )) $(( (T_END - T_GIT) % 60 ))
printf "  Total:   %dm %ds\n" $(( (T_END - T_START) / 60 )) $(( (T_END - T_START) % 60 ))
echo ""
echo "Done. Site deployed and changes pushed."
