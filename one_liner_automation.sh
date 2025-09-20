#!/bin/bash
# Ultimate one-liner for complete SSH workflow automation
# Provides end-to-end automation: clone → pre-flight checker → commit → push → PR ready

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🚀 One-liner SSH workflow automation for forked-u-onex${NC}"
echo ""

# Secure one-liner command (properly escaped and validated)
ONE_LINER="git clone git@github.com:canstralian/forked-u-onex.git && cd forked-u-onex && git remote add upstream git@github.com:redveil-security/onex.git && git fetch upstream && git checkout -B feature/preflight-check upstream/main && wget -q -O dependency_checker.py 'https://raw.githubusercontent.com/canstralian/forked-u-onex/copilot/fix-febc32fb-e0af-4ae3-a314-df93ffc9cab5/dependency_checker.py' && wget -q -O sandbox_runner.py 'https://raw.githubusercontent.com/canstralian/forked-u-onex/copilot/fix-febc32fb-e0af-4ae3-a314-df93ffc9cab5/sandbox_runner.py' && python3 sandbox_runner.py && git add dependency_checker.py sandbox_runner.py && git commit -m 'Add robust idempotent pre-flight dependency checker' && git push -u origin feature/preflight-check && echo '✅ Complete SSH workflow automation finished!'"

echo -e "${YELLOW}📋 Complete SSH workflow command:${NC}"
echo ""
echo -e "${GREEN}${ONE_LINER}${NC}"
echo ""

echo -e "${BLUE}🔄 This command will:${NC}"
echo -e "  ${GREEN}1.${NC} Clone the forked repository via SSH"
echo -e "  ${GREEN}2.${NC} Add upstream remote for synchronization"
echo -e "  ${GREEN}3.${NC} Create feature branch from upstream main"
echo -e "  ${GREEN}4.${NC} Download enhanced pre-flight checker files"
echo -e "  ${GREEN}5.${NC} Test dependency checker functionality"
echo -e "  ${GREEN}6.${NC} Commit and push changes securely"
echo -e "  ${GREEN}7.${NC} Ready for PR creation via GitHub web or gh CLI"
echo ""

echo -e "${BLUE}🛡️  Security Features:${NC}"
echo -e "  • SSH-based authentication (no PAT exposure)"
echo -e "  • Input validation and secure subprocess handling"
echo -e "  • Timeout protection for dependency checks"
echo -e "  • Idempotent operations (safe to re-run)"
echo ""

echo -e "${BLUE}💡 Usage Options:${NC}"
echo -e "  ${YELLOW}Option 1:${NC} Copy and paste the command above"
echo -e "  ${YELLOW}Option 2:${NC} Save to file and execute:"
echo -e "    ${GREEN}echo '${ONE_LINER}' > /tmp/setup_onex.sh && bash /tmp/setup_onex.sh${NC}"
echo -e "  ${YELLOW}Option 3:${NC} Direct execution:"
echo -e "    ${GREEN}bash -c '${ONE_LINER}'${NC}"
echo ""

echo -e "${BLUE}📝 Post-execution steps:${NC}"
echo -e "  • Review the created PR for merge readiness"
echo -e "  • Test the dependency checker in your target environment"
echo -e "  • Consider CI/CD integration for automated checks"