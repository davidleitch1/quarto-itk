# Table Formatting Fix Plan

## Current Problems

### HTML Output
1. Caption font size not smaller (CSS `font-size: 0.85em` not applying)
2. First data row is incorrectly bold (`.table tbody tr:first-child td` rule)
3. Title and source combined in single caption line
4. Caption appears at bottom but styling incomplete

### Word Output
1. Caption appears at TOP instead of bottom (despite `tbl-cap-location: bottom`)
2. Caption in italics (Word default)
3. Title and source combined
4. No table numbering (acceptable per user)

### Root Causes Identified
1. **Quarto bug #8970**: Adding `{#tbl-label}` breaks Word alignment
2. **CSS specificity**: Bootstrap/Quarto styles may override our caption styling
3. **Pandoc limitation**: `tbl-cap-location` may not work without cross-references
4. **Wrong CSS rule**: `.table tbody tr:first-child td` makes first data row bold

## Desired Styling (Bloomberg-Inspired Professional Financial Tables)

### HTML Styling

| Element | Style |
|---------|-------|
| **Table title** | Bold, prominent, ~1.0-1.1em, same color as text, above table |
| **Column headers** | Bold (font-weight: 700), smaller than title (~0.85-0.9em) |
| **Header row border** | Solid 2px line below headers |
| **Data cells** | Smaller font (~0.85em), dense padding (0.3-0.4em) |
| **First column (labels)** | Left-justified |
| **Numeric columns** | Right-justified |
| **Row separators** | Subtle dotted lines in faint color (rgba(128,128,128,0.4)) |
| **Last row** | No bottom border |
| **Source/caption** | Below table, smaller font (~0.85em), left-justified, matches figure caption style |

### Word Styling

| Element | Style |
|---------|-------|
| **Table title** | Bold, prominent, above table or as caption |
| **Column headers** | Bold |
| **Header row border** | Solid line below headers |
| **Data cells** | Normal font weight |
| **First column (labels)** | Left-justified |
| **Numeric columns** | Right-justified or centered |
| **Row separators** | None needed (clean look) |
| **Source/caption** | Below table, smaller font, left-justified, NOT italic |

### Key Principles (Both Formats)
- Dense, compact presentation (financial/Bloomberg style)
- Clear visual hierarchy: Title > Headers > Data > Source
- Labels left-aligned, numbers right-aligned
- No table numbering (e.g., "Table 1:") required
- Source attribution appears below table, not as prominent as title

## Research Tasks

### Task 1: Understand Quarto/Pandoc table caption handling
- [ ] Test markdown table with caption but NO cross-reference
- [ ] Test `tbl-cap-location: bottom` behavior in docx without `{#tbl-label}`
- [ ] Check if caption position is controlled by Pandoc or Quarto filter

### Task 2: Find alternative table structure
- [ ] Test: Title as bold first row, source as plain text below table (not caption)
- [ ] Test: Using HTML table directly with Quarto
- [ ] Test: Separate title paragraph above table, source paragraph below

### Task 3: Fix CSS issues
- [ ] Inspect actual HTML to find correct selectors
- [ ] Test CSS specificity with `!important`
- [ ] Remove incorrect `.table tbody tr:first-child td` bold rule

### Task 4: Fix Word output
- [ ] Research reference.docx table caption styles
- [ ] Test Pandoc `--table-caption-location=bottom` directly
- [ ] Consider post-processing if needed

## Proposed Solution

### Option A: Separate Title and Source (Recommended)

Use this markdown structure:
```markdown
**Performance Summary**

| Metric | FY2022-23 | FY2023-24 |
|:-------|----------:|----------:|
| Data   | 123       | 456       |

*Source: Clean Energy Regulator*
```

- Title: Bold paragraph above table
- Table: Standard markdown with alignment markers
- Source: Italic paragraph below table (not a caption)

**Pros:**
- No cross-reference, so Word alignment works
- Full control over styling
- Works consistently in HTML and Word

**Cons:**
- Not a "proper" table caption semantically
- No automatic table numbering

### Option B: Custom Quarto Extension/Filter

Create a Lua filter to handle table captions separately for HTML and Word.

**Pros:**
- Proper semantic structure
- Could fix the Quarto bug locally

**Cons:**
- More complex to implement and maintain

### Option C: Two Separate Output Pipelines

- HTML: Use `{#tbl-label}` for proper captions
- Word: Remove labels before rendering

**Cons:**
- Maintenance burden

## Test Plan

### Test 1: Option A - Separate Title and Source
1. Create test table with structure:
   - Bold title paragraph
   - Markdown table with alignment markers
   - Italic source paragraph
2. Render to HTML - verify styling
3. Render to Word - verify alignment and appearance

### Test 2: CSS Fixes
1. Remove `.table tbody tr:first-child td` bold rule
2. Add more specific caption selectors
3. Verify caption styling in HTML

### Test 3: Word Caption Position
1. Test if source as regular paragraph appears correctly
2. Check alignment is preserved

## Implementation Steps

1. Fix CSS (remove incorrect bold rule, improve caption selectors)
2. Modify one table to use Option A structure
3. Render and test both outputs
4. If successful, apply to all tables
5. Update CLAUDE.md with new table formatting guidelines

## Files to Modify

- `styles.css` - Fix CSS rules
- `posts/safeguards  review.md` - Update table structure
- `_quarto.yml` - May need to adjust settings
- `CLAUDE.md` - Document the solution for future use
