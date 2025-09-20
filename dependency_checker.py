#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Idempotent pre-flight dependency checker for forked-u-onex.
"""

import subprocess
import importlib.util
from typing import List


class DependencyChecker:
    @staticmethod
    def check_system_package(package_name: str) -> bool:
        """Check if a system package is installed using dpkg or rpm."""
        try:
            result = subprocess.run(["dpkg", "-s", package_name],
                                    stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL)
            return result.returncode == 0
        except FileNotFoundError:
            try:
                result = subprocess.run(["rpm", "-q", package_name],
                                        stdout=subprocess.DEVNULL,
                                        stderr=subprocess.DEVNULL)
                return result.returncode == 0
            except FileNotFoundError:
                return False

    @staticmethod
    def check_python_package(package_name: str) -> bool:
        """Check if a Python package is available for import."""
        return importlib.util.find_spec(package_name) is not None

    @staticmethod
    def verify_dependencies(system_packages: List[str], python_packages: List[str]) -> None:
        """Verify system and Python dependencies and report status."""
        missing_sys = [pkg for pkg in system_packages if not DependencyChecker.check_system_package(pkg)]
        missing_py = [pkg for pkg in python_packages if not DependencyChecker.check_python_package(pkg)]

        if missing_sys:
            print(f"[DependencyChecker] Missing system packages: {', '.join(missing_sys)}")
        else:
            print("[DependencyChecker] All system packages installed ✅")

        if missing_py:
            print(f"[DependencyChecker] Missing Python packages: {', '.join(missing_py)}")
        else:
            print("[DependencyChecker] All Python packages installed ✅")

        if missing_sys or missing_py:
            print("[DependencyChecker] Skipping already installed packages. Manual or automated install can follow.")