#!/bin/bash

# Download and extract Quarto directly (no dpkg needed)
wget -q https://github.com/quarto-dev/quarto-cli/releases/download/v1.6.39/quarto-1.6.39-linux-amd64.tar.gz
tar -xzf quarto-1.6.39-linux-amd64.tar.gz

# Move Quarto out of the project directory to avoid scanning it
mv quarto-1.6.39 /tmp/

# Add Quarto to PATH and render (excluding drafts)
export PATH="/tmp/quarto-1.6.39/bin:$PATH"
quarto render --no-render-drafts
