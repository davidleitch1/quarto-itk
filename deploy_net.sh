#!/usr/bin/env bash
set -euo pipefail

echo "🔄 Incremental Quarto build…"
quarto render --incremental

echo "🚀 Deploying to Netlify…"
netlify deploy --dir=_site --prod

echo "✅ Deployment complete!"