#!/bin/bash

# Markdown Proofreading Script
# Usage: ./proofread.sh filename.md

if [ $# -eq 0 ]; then
    echo "Usage: $0 <markdown-file>"
    echo "Example: $0 posts/MyArticle.md"
    exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found."
    exit 1
fi

echo "Starting Claude Code proofreading session for: $FILE"
echo "Launching Claude Code with proofreading instructions..."

# Launch Claude Code with the file
claude-code --file "$FILE" --prompt "Please proofread this markdown file for spelling mistakes, double words, and grammatical errors. Present proposed changes with checkboxes for my approval before making any edits."