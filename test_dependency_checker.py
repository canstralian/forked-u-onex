#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Basic tests for the dependency_checker module.

These tests verify the core functionality of the DependencyChecker class
and ensure it handles various scenarios correctly.
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dependency_checker import DependencyChecker


class TestDependencyChecker(unittest.TestCase):
    """Test cases for DependencyChecker class."""
    
    def test_validate_package_name_valid(self):
        """Test validation of valid package names."""
        valid_names = [
            "git",
            "python3",
            "curl",
            "package-name",
            "package_name",
            "package.name",
            "package+name",
            "123package",
            "a",
            "Package123"
        ]
        
        for name in valid_names:
            with self.subTest(package_name=name):
                self.assertTrue(
                    DependencyChecker._validate_package_name(name),
                    f"Package name '{name}' should be valid"
                )
    
    def test_validate_package_name_invalid(self):
        """Test validation of invalid package names."""
        invalid_names = [
            "",           # Empty string
            None,         # None value
            123,          # Not a string
            "bad;package", # Contains semicolon
            "hack`command`", # Contains backticks
            "bad|pipe",   # Contains pipe
            "bad&command", # Contains ampersand
            "bad$var",    # Contains dollar sign
            "bad space",  # Contains space
            "bad\nline",  # Contains newline
            "bad\ttab",   # Contains tab
        ]
        
        for name in invalid_names:
            with self.subTest(package_name=name):
                self.assertFalse(
                    DependencyChecker._validate_package_name(name),
                    f"Package name '{name}' should be invalid"
                )
    
    def test_check_system_package_exists(self):
        """Test checking for packages that should exist on most systems."""
        # These packages are very likely to exist on CI systems
        likely_packages = ["sh", "ls"]  # Basic shell commands
        
        for package in likely_packages:
            with self.subTest(package_name=package):
                # We don't assert True here because package managers vary
                # but the function should not raise an exception
                result = DependencyChecker.check_system_package(package)
                self.assertIsInstance(result, bool)
    
    def test_check_system_package_nonexistent(self):
        """Test checking for packages that definitely don't exist."""
        fake_packages = [
            "this-package-definitely-does-not-exist-12345",
            "nonexistent-package-xyz",
        ]
        
        for package in fake_packages:
            with self.subTest(package_name=package):
                result = DependencyChecker.check_system_package(package)
                # Should return False for non-existent packages
                self.assertFalse(result)
    
    def test_check_python_package_standard_library(self):
        """Test checking for Python standard library modules."""
        stdlib_modules = ["sys", "os", "re", "subprocess", "importlib"]
        
        for module in stdlib_modules:
            with self.subTest(module_name=module):
                result = DependencyChecker.check_python_package(module)
                self.assertTrue(
                    result,
                    f"Standard library module '{module}' should be available"
                )
    
    def test_check_python_package_nonexistent(self):
        """Test checking for Python packages that don't exist."""
        fake_modules = [
            "this_module_definitely_does_not_exist_12345",
            "nonexistent_python_package_xyz",
        ]
        
        for module in fake_modules:
            with self.subTest(module_name=module):
                result = DependencyChecker.check_python_package(module)
                self.assertFalse(
                    result,
                    f"Non-existent module '{module}' should not be available"
                )
    
    def test_verify_dependencies_no_exception(self):
        """Test that verify_dependencies doesn't raise exceptions."""
        # Test with a mix of valid and invalid package names
        system_packages = ["git", "this-does-not-exist"]
        python_packages = ["sys", "this_does_not_exist"]
        
        # This should not raise an exception
        try:
            DependencyChecker.verify_dependencies(system_packages, python_packages)
        except Exception as e:
            self.fail(f"verify_dependencies raised an exception: {e}")
    
    def test_verify_dependencies_empty_lists(self):
        """Test verify_dependencies with empty package lists."""
        try:
            DependencyChecker.verify_dependencies([], [])
        except Exception as e:
            self.fail(f"verify_dependencies with empty lists raised an exception: {e}")


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)