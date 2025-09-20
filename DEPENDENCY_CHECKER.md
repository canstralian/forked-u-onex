# Robust Pre-Flight Dependency Checker

A comprehensive, idempotent pre-flight dependency checker for the forked-u-onex project, featuring robust security validation, multi-platform support, and automated workflow integration.

## Files Added/Enhanced

- `dependency_checker.py` - Core dependency checking with security validation
- `sandbox_runner.py` - Enhanced example integration with error handling  
- `automate_workflow.sh` - Robust SSH-based workflow automation
- `one_liner_automation.sh` - Complete end-to-end automation script
- `DEPENDENCY_CHECKER.md` - Comprehensive documentation

## 🚀 Features

### Security & Robustness
- **Input Validation**: Regex-based package name validation to prevent injection attacks
- **Timeout Protection**: 10-second timeouts on package manager commands
- **Error Handling**: Comprehensive exception handling for all operations
- **Secure Subprocess**: Proper subprocess handling with controlled environments

### Cross-Platform Support
- **Debian/Ubuntu**: dpkg package manager support
- **RedHat/CentOS/Fedora**: rpm and yum package manager support  
- **Alpine Linux**: apk package manager support
- **Python Packages**: importlib-based module availability checking

### Operational Excellence
- **Idempotent**: Safe to run multiple times, skips installed packages
- **PEP 8 Compliant**: Follows Python coding standards with proper line lengths
- **Clear Feedback**: Colored output with emojis and actionable messages
- **CI/CD Ready**: Suitable for continuous integration workflows

## 📋 Usage

### Basic Usage

```python
from dependency_checker import DependencyChecker

# Check system and Python packages
system_packages = ["nmap", "wireshark", "sqlmap", "git"]
python_packages = ["requests", "flask", "urllib3"]

DependencyChecker.verify_dependencies(system_packages, python_packages)
```

### Standalone Execution

```bash
# Run the example checker
python3 sandbox_runner.py

# Run the core module directly
python3 dependency_checker.py
```

### Automated SSH Workflow

```bash
# Step-by-step automation
./automate_workflow.sh

# Complete one-liner (copy from script output)
./one_liner_automation.sh
```

## 🔧 Integration with Onex

The dependency checker seamlessly integrates with the existing onex ecosystem:

### Pre-Installation Checks
```bash
# Before running onex installations
python3 dependency_checker.py
# Then proceed with onex tool installations
```

### Supported Tools
- **Network Tools**: nmap, wireshark, netcat
- **Security Tools**: sqlmap, nikto, dirb
- **Development Tools**: git, curl, python3
- **Python Libraries**: requests, flask, pyzmq

### Distribution Compatibility
- Works across all Linux distributions supported by onex
- Detects package managers automatically
- Provides consistent feedback regardless of underlying system

## 🔒 Security Features

### Input Sanitization
```python
# Package names are validated against secure regex
pattern = r'^[a-zA-Z0-9._+-]+$'
```

### Secure Execution
- No shell injection vulnerabilities
- Controlled subprocess environments
- Timeout protection against hanging commands
- Proper error handling and logging

### SSH Workflow Security
- No Personal Access Token (PAT) exposure in scripts
- SSH key-based authentication throughout
- Secure remote operations for CI/CD integration

## 🌐 SSH Workflow Benefits

### Developer Experience
- **No PAT Management**: SSH keys handle all authentication
- **Scriptable**: Full automation from clone to PR creation
- **Consistent**: Same workflow across different environments
- **Secure**: No credential exposure in scripts or logs

### CI/CD Integration
```bash
# Example CI/CD integration
git clone git@github.com:canstralian/forked-u-onex.git
cd forked-u-onex
python3 sandbox_runner.py  # Pre-flight check
# Continue with deployment if checks pass
```

### Automation Workflow
1. **Clone**: SSH-based repository cloning
2. **Branch**: Feature branch creation from upstream
3. **Check**: Comprehensive dependency validation
4. **Commit**: Automated change staging and committing
5. **Push**: Secure push to feature branch
6. **PR Ready**: Prepared for GitHub PR creation

## 🧪 Testing & Validation

### Manual Testing
```bash
# Test basic functionality
python3 dependency_checker.py

# Test with custom packages
python3 -c "
from dependency_checker import DependencyChecker
DependencyChecker.verify_dependencies(['git'], ['sys'])
"
```

### Security Testing
```bash
# Test input validation (should safely handle invalid inputs)
python3 -c "
from dependency_checker import DependencyChecker
DependencyChecker.verify_dependencies(['bad;package', ''], ['hack`cmd`'])
"
```

### Automation Testing
```bash
# Test workflow scripts
./automate_workflow.sh  # Should complete without errors
./one_liner_automation.sh  # Should display usage information
```

## 🔧 Customization

### Adding Package Managers
```python
# Extend check_system_package method
try:
    result = subprocess.run(
        ["pacman", "-Q", package_name],  # Arch Linux example
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=10
    )
    return result.returncode == 0
except (FileNotFoundError, subprocess.TimeoutExpired):
    pass
```

### Custom Package Lists
```python
# In sandbox_runner.py or your own script
security_tools = ["nmap", "wireshark", "sqlmap", "metasploit"]
web_tools = ["curl", "wget", "httpie"]
python_libs = ["requests", "beautifulsoup4", "scrapy"]

DependencyChecker.verify_dependencies(
    security_tools + web_tools, 
    python_libs
)
```

## 📊 Example Output

```
🚀 Starting forked-u-onex pre-flight dependency check...
📦 Checking standard packages...
[DependencyChecker] Missing system packages: nmap, wireshark, sqlmap
[DependencyChecker] All Python packages installed ✅
[DependencyChecker] Skipping already installed packages. Manual or automated install can follow.

🛡️  Testing security validation...
[DependencyChecker] Warning: Invalid package name 'bad;package' - skipping
[DependencyChecker] Skipped 3 invalid package names for security

✅ Dependencies checked. System ready for onex operations!
💡 Tip: Install missing packages before running onex tools
```

## 🚀 Quick Start

1. **Download and Test**:
   ```bash
   wget https://raw.githubusercontent.com/canstralian/forked-u-onex/main/dependency_checker.py
   python3 dependency_checker.py
   ```

2. **Full Automation**:
   ```bash
   ./one_liner_automation.sh  # Copy the displayed command
   ```

3. **Manual Integration**:
   ```bash
   git clone git@github.com:canstralian/forked-u-onex.git
   cd forked-u-onex
   python3 sandbox_runner.py
   ```

This robust dependency checker ensures your forked-u-onex environment is properly configured and secure before executing any hacking tools or security operations.