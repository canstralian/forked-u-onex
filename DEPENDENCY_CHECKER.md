# Pre-Flight Dependency Checker

This directory now includes an idempotent pre-flight dependency checker for the forked-u-onex project.

## Files Added

- `dependency_checker.py` - Core dependency checking functionality
- `sandbox_runner.py` - Example integration showing usage
- `automate_workflow.sh` - Automation script for SSH-based workflow

## Features

- **Idempotent**: Skips already installed packages
- **Cross-platform**: Works with both dpkg (Debian/Ubuntu) and rpm (RedHat/CentOS) systems
- **Python package support**: Checks Python modules using importlib
- **Clean output**: Clear status messages with emojis
- **PEP 8 compliant**: Follows Python coding standards
- **Zen of Python**: Simple, readable, and explicit implementation

## Usage

### Basic Usage

```python
from dependency_checker import DependencyChecker

system_packages = ["nmap", "wireshark", "sqlmap"]
python_packages = ["requests", "flask", "pyzmq"]

DependencyChecker.verify_dependencies(system_packages, python_packages)
```

### Standalone Execution

```bash
python3 sandbox_runner.py
```

### Automated Workflow

```bash
./automate_workflow.sh
```

## Integration with Onex

The dependency checker integrates seamlessly with the existing onex tool installation workflow by:

1. Pre-checking dependencies before attempting installations
2. Providing clear feedback on what's missing vs. already installed
3. Supporting the same tools that onex installs (nmap, wireshark, etc.)
4. Working across the same Linux distributions that onex supports

## SSH Workflow Benefits

- No PAT exposure → more secure for scripts & CI/CD
- Works consistently across cloning, pushing, and PR creation
- Compatible with automated pre-flight checks and sandbox execution
- Fully aligned with forked-u-onex workflow