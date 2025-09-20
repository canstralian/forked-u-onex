#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sandbox Runner for forked-u-onex with pre-flight dependency checking.
"""

from dependency_checker import DependencyChecker

if __name__ == "__main__":
    system_packages = ["nmap", "wireshark", "sqlmap"]
    python_packages = ["requests", "flask", "pyzmq"]

    DependencyChecker.verify_dependencies(system_packages, python_packages)

    print("✅ Dependencies checked. Continuing execution...")