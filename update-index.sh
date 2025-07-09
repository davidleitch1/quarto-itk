#!/bin/zsh
# Render index.md and deploy updated files to Netlify

echo "Opening and saving in VSCode..."
code index.md --save

echo "Rendering index.md..."
quarto render index.md --output-dir _site

echo "Deploying changes to Netlify..."
netlify deploy --prod

echo "Update completed successfully!"