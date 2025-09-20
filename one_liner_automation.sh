#!/bin/bash
# Ultimate one-liner for complete SSH workflow automation
# This automates: clone → pre-flight checker addition → commit → push → PR creation

# One-liner command (can be executed as a single command):
# git clone git@github.com:canstralian/forked-u-onex.git && cd forked-u-onex && git remote add upstream git@github.com:redveil-security/onex.git && git fetch upstream && git checkout -B feature/preflight-check upstream/main && wget -q https://raw.githubusercontent.com/canstralian/forked-u-onex/copilot/fix-febc32fb-e0af-4ae3-a314-df93ffc9cab5/dependency_checker.py && wget -q https://raw.githubusercontent.com/canstralian/forked-u-onex/copilot/fix-febc32fb-e0af-4ae3-a314-df93ffc9cab5/sandbox_runner.py && python3 sandbox_runner.py && git add dependency_checker.py sandbox_runner.py && git commit -m "Add idempotent pre-flight dependency checker" && git push -u origin feature/preflight-check && echo "✅ Complete SSH workflow automation finished!"

echo "🚀 One-liner SSH workflow automation command:"
echo ""
echo "git clone git@github.com:canstralian/forked-u-onex.git && cd forked-u-onex && git remote add upstream git@github.com:redveil-security/onex.git && git fetch upstream && git checkout -B feature/preflight-check upstream/main && wget -q https://raw.githubusercontent.com/canstralian/forked-u-onex/copilot/fix-febc32fb-e0af-4ae3-a314-df93ffc9cab5/dependency_checker.py && wget -q https://raw.githubusercontent.com/canstralian/forked-u-onex/copilot/fix-febc32fb-e0af-4ae3-a314-df93ffc9cab5/sandbox_runner.py && python3 sandbox_runner.py && git add dependency_checker.py sandbox_runner.py && git commit -m 'Add idempotent pre-flight dependency checker' && git push -u origin feature/preflight-check && echo '✅ Complete SSH workflow automation finished!'"
echo ""
echo "This command will:"
echo "1. Clone the fork via SSH"
echo "2. Add upstream remote"
echo "3. Create feature branch from upstream"
echo "4. Download the pre-flight checker files"
echo "5. Test the dependency checker"
echo "6. Commit and push changes"
echo "7. Ready for PR creation via gh CLI or web interface"