#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sandbox Runner for forked-u-onex with comprehensive pre-flight dependency checking.

This script demonstrates robust dependency checking with various types of
packages and scenarios, including error handling and security validation.
"""

import sys
from dependency_checker import DependencyChecker


def main():
    """Main function demonstrating comprehensive dependency checking."""
    print("🚀 Starting forked-u-onex pre-flight dependency check...")
    
    # Security and hacking tools commonly used with onex
    system_packages = [
        "nmap",          # Network mapper
        "wireshark",     # Network protocol analyzer
        "sqlmap",        # SQL injection tool
        "git",           # Version control (should be installed)
        "curl",          # HTTP client (should be installed)
        "python3"        # Python interpreter (should be installed)
    ]
    
    # Python packages for security and networking
    python_packages = [
        "requests",      # HTTP library
        "flask",         # Web framework
        "pyzmq",         # ZeroMQ bindings
        "urllib3",       # HTTP client (should be installed)
        "socket"         # Built-in module (should be available)
    ]
    
    # Test with some invalid package names (for security validation)
    invalid_packages = [
        "",              # Empty string
        "bad;package",   # Contains semicolon
        "hack`command`", # Contains backticks
        "valid-package"  # This one is actually valid
    ]
    
    print("📦 Checking standard packages...")
    DependencyChecker.verify_dependencies(system_packages, python_packages)
    
    print("\n🛡️  Testing security validation...")
    DependencyChecker.verify_dependencies(invalid_packages, [])
    
    print("\n✅ Dependencies checked. System ready for onex operations!")
    print("💡 Tip: Install missing packages before running onex tools")
    
    return 0


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n⚠️  Dependency check interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during dependency check: {e}")
        sys.exit(1)