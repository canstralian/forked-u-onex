#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Asynchronous, robust, idempotent pre-flight dependency checker for forked-u-onex.

This module provides secure and comprehensive asynchronous dependency checking for both
system packages and Python modules across multiple Linux distributions.
"""

import re
import asyncio
import importlib.util
from typing import List


class AsyncDependencyChecker:
    """
    Secure asynchronous dependency checker supporting multiple package managers.

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
    async def check_system_package(package_name: str) -> bool:
        """
        Asynchronously check if a system package is installed using available package managers.

        Supports dpkg (Debian/Ubuntu), rpm (RedHat/CentOS/Fedora),
        apk (Alpine), and yum (older RedHat systems).

        Args:
            package_name: Name of the package to check

        Returns:
            bool: True if package is installed, False otherwise
        """
        if not AsyncDependencyChecker._validate_package_name(package_name):
            print(f"[AsyncDependencyChecker] Warning: Invalid package name "
                  f"'{package_name}' - skipping")
            return False

        package_name = package_name.strip()

        # Try dpkg (Debian/Ubuntu)
        try:
            process = await asyncio.create_subprocess_exec(
                "dpkg", "-s", package_name,
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL
            )
            await asyncio.wait_for(process.wait(), timeout=10)
            return process.returncode == 0
        except (FileNotFoundError, asyncio.TimeoutError):
            pass

        # Try rpm (RedHat/CentOS/Fedora)
        try:
            process = await asyncio.create_subprocess_exec(
                "rpm", "-q", package_name,
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL
            )
            await asyncio.wait_for(process.wait(), timeout=10)
            return process.returncode == 0
        except (FileNotFoundError, asyncio.TimeoutError):
            pass

        # Try apk (Alpine)
        try:
            process = await asyncio.create_subprocess_exec(
                "apk", "info", "-e", package_name,
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL
            )
            await asyncio.wait_for(process.wait(), timeout=10)
            return process.returncode == 0
        except (FileNotFoundError, asyncio.TimeoutError):
            pass

        # Try yum (older RedHat systems)
        try:
            process = await asyncio.create_subprocess_exec(
                "yum", "list", "installed", package_name,
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL
            )
            await asyncio.wait_for(process.wait(), timeout=10)
            return process.returncode == 0
        except (FileNotFoundError, asyncio.TimeoutError):
            pass

        return False

    @staticmethod
    def check_python_package(package_name: str) -> bool:
        """
        Check if a Python package is available for import.

        Note: This method is not async as importlib operations are typically fast
        and don't benefit from async execution.

        Args:
            package_name: Name of the Python package to check

        Returns:
            bool: True if package can be imported, False otherwise
        """
        if not AsyncDependencyChecker._validate_package_name(package_name):
            print(f"[AsyncDependencyChecker] Warning: Invalid Python package "
                  f"name '{package_name}' - skipping")
            return False

        try:
            return importlib.util.find_spec(package_name.strip()) is not None
        except (ImportError, ValueError, ModuleNotFoundError):
            return False

    @staticmethod
    async def verify_dependencies(system_packages: List[str],
                                  python_packages: List[str]) -> None:
        """
        Asynchronously verify system and Python dependencies and report status.

        Args:
            system_packages: List of system package names to check
            python_packages: List of Python package names to check
        """
        if not isinstance(system_packages, list):
            system_packages = []
        if not isinstance(python_packages, list):
            python_packages = []

        # Filter valid packages
        valid_sys_packages = [pkg for pkg in system_packages
                              if AsyncDependencyChecker._validate_package_name(pkg)]
        valid_py_packages = [pkg for pkg in python_packages
                             if AsyncDependencyChecker._validate_package_name(pkg)]

        # Check system packages asynchronously
        sys_tasks = [
            AsyncDependencyChecker.check_system_package(pkg)
            for pkg in valid_sys_packages
        ]
        sys_results = await asyncio.gather(*sys_tasks, return_exceptions=True)

        # Handle any exceptions from system package checks
        missing_sys = []
        for i, result in enumerate(sys_results):
            if isinstance(result, Exception):
                print(f"[AsyncDependencyChecker] Error checking {valid_sys_packages[i]}: {result}")
                missing_sys.append(valid_sys_packages[i])
            elif not result:
                missing_sys.append(valid_sys_packages[i])

        # Check Python packages (these are synchronous but fast)
        missing_py = [pkg for pkg in valid_py_packages
                      if not AsyncDependencyChecker.check_python_package(pkg)]

        # Report results
        if missing_sys:
            print(f"[AsyncDependencyChecker] Missing system packages: "
                  f"{', '.join(missing_sys)}")
        else:
            print("[AsyncDependencyChecker] All system packages installed ✅")

        if missing_py:
            print(f"[AsyncDependencyChecker] Missing Python packages: "
                  f"{', '.join(missing_py)}")
        else:
            print("[AsyncDependencyChecker] All Python packages installed ✅")

        if missing_sys or missing_py:
            print("[AsyncDependencyChecker] Skipping already installed packages. "
                  "Manual or automated install can follow.")

        # Report any invalid package names
        invalid_sys = [pkg for pkg in system_packages
                       if not AsyncDependencyChecker._validate_package_name(pkg)]
        invalid_py = [pkg for pkg in python_packages
                      if not AsyncDependencyChecker._validate_package_name(pkg)]

        if invalid_sys or invalid_py:
            print(f"[AsyncDependencyChecker] Skipped {len(invalid_sys + invalid_py)} "
                  f"invalid package names for security")


async def main():
    """Main async function demonstrating comprehensive dependency checking."""
    print("🚀 Starting async forked-u-onex pre-flight dependency check...")

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
        "hack`command`",  # Contains backticks
        "valid-package"  # This one is actually valid
    ]

    print("📦 Checking standard packages asynchronously...")
    await AsyncDependencyChecker.verify_dependencies(system_packages, python_packages)

    print("\n🛡️  Testing security validation...")
    await AsyncDependencyChecker.verify_dependencies(invalid_packages, [])

    print("\n✅ Async dependencies checked. System ready for onex operations!")
    print("💡 Tip: Install missing packages before running onex tools")

    return 0


if __name__ == "__main__":
    try:
        exit_code = asyncio.run(main())
        exit(exit_code)
    except KeyboardInterrupt:
        print("\n⚠️  Async dependency check interrupted by user")
        exit(1)
    except Exception as e:
        print(f"\n❌ Error during async dependency check: {e}")
        exit(1)
