#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Robust, idempotent pre-flight dependency checker for forked-u-onex.

This module provides secure and comprehensive dependency checking for both
system packages and Python modules across multiple Linux distributions.
"""

import re
import subprocess
import importlib.util
from typing import List, Optional


class DependencyChecker:
    """
    Secure dependency checker supporting multiple package managers.
    
    Provides idempotent checking for system packages (dpkg, rpm, apk, yum)
    and Python packages with robust error handling and input validation.
    """

    @staticmethod
    def _validate_package_name(package_name: str) -> bool:
        """
        Validate package name for security.
        
        Args:
            package_name: The package name to validate
            
        Returns:
            bool: True if package name is safe, False otherwise
        """
        if not package_name or not isinstance(package_name, str):
            return False
        
        # Allow alphanumeric, hyphens, underscores, dots, and plus signs
        pattern = r'^[a-zA-Z0-9._+-]+$'
        return bool(re.match(pattern, package_name.strip()))

    @staticmethod
    def check_system_package(package_name: str) -> bool:
        """
        Check if a system package is installed using available package managers.
        
        Supports dpkg (Debian/Ubuntu), rpm (RedHat/CentOS/Fedora),
        apk (Alpine), and yum (older RedHat systems).
        
        Args:
            package_name: Name of the package to check
            
        Returns:
            bool: True if package is installed, False otherwise
        """
        if not DependencyChecker._validate_package_name(package_name):
            print(f"[DependencyChecker] Warning: Invalid package name "
                  f"'{package_name}' - skipping")
            return False

        package_name = package_name.strip()

        # Try dpkg (Debian/Ubuntu)
        try:
            result = subprocess.run(
                ["dpkg", "-s", package_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # Try rpm (RedHat/CentOS/Fedora)
        try:
            result = subprocess.run(
                ["rpm", "-q", package_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # Try apk (Alpine)
        try:
            result = subprocess.run(
                ["apk", "info", "-e", package_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # Try yum (older RedHat systems)
        try:
            result = subprocess.run(
                ["yum", "list", "installed", package_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        return False

    @staticmethod
    def check_python_package(package_name: str) -> bool:
        """
        Check if a Python package is available for import.
        
        Args:
            package_name: Name of the Python package to check
            
        Returns:
            bool: True if package can be imported, False otherwise
        """
        if not DependencyChecker._validate_package_name(package_name):
            print(f"[DependencyChecker] Warning: Invalid Python package "
                  f"name '{package_name}' - skipping")
            return False

        try:
            return importlib.util.find_spec(package_name.strip()) is not None
        except (ImportError, ValueError, ModuleNotFoundError):
            return False

    @staticmethod
    def verify_dependencies(system_packages: List[str],
                          python_packages: List[str]) -> None:
        """
        Verify system and Python dependencies and report status.
        
        Args:
            system_packages: List of system package names to check
            python_packages: List of Python package names to check
        """
        if not isinstance(system_packages, list):
            system_packages = []
        if not isinstance(python_packages, list):
            python_packages = []

        # Filter and check system packages
        valid_sys_packages = [pkg for pkg in system_packages 
                            if DependencyChecker._validate_package_name(pkg)]
        missing_sys = [pkg for pkg in valid_sys_packages 
                      if not DependencyChecker.check_system_package(pkg)]

        # Filter and check Python packages  
        valid_py_packages = [pkg for pkg in python_packages
                           if DependencyChecker._validate_package_name(pkg)]
        missing_py = [pkg for pkg in valid_py_packages
                     if not DependencyChecker.check_python_package(pkg)]

        # Report results
        if missing_sys:
            print(f"[DependencyChecker] Missing system packages: "
                  f"{', '.join(missing_sys)}")
        else:
            print("[DependencyChecker] All system packages installed ✅")

        if missing_py:
            print(f"[DependencyChecker] Missing Python packages: "
                  f"{', '.join(missing_py)}")
        else:
            print("[DependencyChecker] All Python packages installed ✅")

        if missing_sys or missing_py:
            print("[DependencyChecker] Skipping already installed packages. "
                  "Manual or automated install can follow.")
        
        # Report any invalid package names
        invalid_sys = [pkg for pkg in system_packages 
                      if not DependencyChecker._validate_package_name(pkg)]
        invalid_py = [pkg for pkg in python_packages
                     if not DependencyChecker._validate_package_name(pkg)]
        
        if invalid_sys or invalid_py:
            print(f"[DependencyChecker] Skipped {len(invalid_sys + invalid_py)} "
                  f"invalid package names for security")


if __name__ == "__main__":
    # Example usage when run directly
    example_sys = ["git", "curl", "python3"]
    example_py = ["requests", "urllib3"]
    
    print("🔍 Running dependency checker example...")
    DependencyChecker.verify_dependencies(example_sys, example_py)