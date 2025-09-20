#!/bin/bash
# Robust SSH-based workflow automation for forked-u-onex with pre-flight checker
# Usage: ./automate_workflow.sh

set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Color codes for better output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Starting automated SSH workflow for forked-u-onex${NC}"

# Validate prerequisites
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 is required but not installed${NC}"
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git is required but not installed${NC}"
    exit 1
fi

# Create feature branch from upstream (with error handling)
echo -e "${YELLOW}📦 Creating feature branch with pre-flight checker...${NC}"
if git fetch origin 2>/dev/null; then
    echo -e "${GREEN}✅ Origin fetched successfully${NC}"
else
    echo -e "${YELLOW}⚠️  Could not fetch origin - continuing with local refs${NC}"
fi

# Try to create branch, handle if it already exists
if git checkout -B feature/preflight-check origin/copilot/fix-febc32fb-e0af-4ae3-a314-df93ffc9cab5 2>/dev/null; then
    echo -e "${GREEN}✅ Feature branch created/updated${NC}"
else
    echo -e "${YELLOW}⚠️  Branch may already exist or ref not found - continuing${NC}"
fi

# Verify required files exist
echo -e "${YELLOW}🔍 Verifying pre-flight checker files...${NC}"
missing_files=()

if [ ! -f "dependency_checker.py" ]; then
    missing_files+=("dependency_checker.py")
fi

if [ ! -f "sandbox_runner.py" ]; then
    missing_files+=("sandbox_runner.py")
fi

if [ ${#missing_files[@]} -gt 0 ]; then
    echo -e "${RED}❌ Missing required files: ${missing_files[*]}${NC}"
    echo -e "${YELLOW}💡 Files should be in the current directory${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All required files found${NC}"

# Test the dependency checker with timeout
echo -e "${YELLOW}🧪 Testing dependency checker...${NC}"
if timeout 30 python3 sandbox_runner.py; then
    echo -e "${GREEN}✅ Dependency checker test passed${NC}"
else
    echo -e "${RED}❌ Dependency checker test failed or timed out${NC}"
    exit 1
fi

# Show what we're about to commit
echo -e "${YELLOW}📋 Checking repository status...${NC}"
if git status --porcelain | grep -q .; then
    echo -e "${BLUE}Files that will be committed:${NC}"
    git status --porcelain
else
    echo -e "${GREEN}✅ Working directory is clean${NC}"
fi

echo -e "${GREEN}✅ Automated workflow completed successfully!${NC}"
echo ""
echo -e "${BLUE}📝 Next steps:${NC}"
echo -e "  ${GREEN}1.${NC} Review changes: ${YELLOW}git diff${NC}"
echo -e "  ${GREEN}2.${NC} Commit changes: ${YELLOW}git add . && git commit -m 'Add robust pre-flight dependency checker'${NC}"
echo -e "  ${GREEN}3.${NC} Push changes: ${YELLOW}git push -u origin feature/preflight-check${NC}"
echo -e "  ${GREEN}4.${NC} Create PR via GitHub web interface or ${YELLOW}gh CLI${NC}"
echo ""
echo -e "${BLUE}🔒 Security: This workflow uses SSH for secure repository operations${NC}"