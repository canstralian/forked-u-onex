#!/bin/bash
# One-liner automation for SSH-based fork workflow with pre-flight checker
# Usage: ./automate_workflow.sh

set -e

echo "🚀 Starting automated SSH workflow for forked-u-onex"

# Create feature branch from upstream
echo "📦 Creating feature branch with pre-flight checker..."
git fetch origin 2>/dev/null || echo "Origin already up to date"
git checkout -B feature/preflight-check origin/copilot/fix-febc32fb-e0af-4ae3-a314-df93ffc9cab5 2>/dev/null || echo "Branch already exists"

# Verify files exist
if [ ! -f "dependency_checker.py" ] || [ ! -f "sandbox_runner.py" ]; then
    echo "❌ Pre-flight checker files not found!"
    exit 1
fi

# Test the dependency checker
echo "🧪 Testing dependency checker..."
python3 sandbox_runner.py

# Show what we're committing
echo "📋 Files to be committed:"
git status --porcelain

echo "✅ Automated workflow complete!"
echo "📝 Next steps:"
echo "  1. Review changes with: git diff"
echo "  2. Commit changes with: git add . && git commit -m 'Add idempotent pre-flight dependency checker'"
echo "  3. Push with: git push -u origin feature/preflight-check"
echo "  4. Create PR via SSH-compatible method"