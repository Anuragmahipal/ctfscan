#!/usr/bin/env python3
"""
Quick verification script for ctfscan package structure
Run this before deploying to PyPI
"""

import os
import sys
from pathlib import Path


def check_file_exists(path, description):
    """Check if a file exists"""
    if os.path.exists(path):
        print(f"✓ {description}: {path}")
        return True
    else:
        print(f"✗ MISSING {description}: {path}")
        return False


def check_directory_exists(path, description):
    """Check if a directory exists"""
    if os.path.isdir(path):
        print(f"✓ {description}: {path}")
        return True
    else:
        print(f"✗ MISSING {description}: {path}")
        return False


def verify_structure():
    """Verify the project structure is correct"""
    
    print("=" * 60)
    print("ctfscan PyPI Package Structure Verification")
    print("=" * 60)
    print()
    
    checks = []
    
    # Check directories
    print("Checking directories...")
    checks.append(check_directory_exists("src/ctfscan", "Package directory"))
    checks.append(check_directory_exists("tests", "Tests directory"))
    print()
    
    # Check essential files
    print("Checking essential files...")
    checks.append(check_file_exists("setup.py", "Setup.py"))
    checks.append(check_file_exists("pyproject.toml", "pyproject.toml"))
    checks.append(check_file_exists("README.md", "README.md"))
    checks.append(check_file_exists("LICENSE", "LICENSE"))
    checks.append(check_file_exists("MANIFEST.in", "MANIFEST.in"))
    print()
    
    # Check package files
    print("Checking package files...")
    checks.append(check_file_exists("src/ctfscan/__init__.py", "Package __init__.py"))
    checks.append(check_file_exists("src/ctfscan/core.py", "Core module"))
    checks.append(check_file_exists("src/ctfscan/cli.py", "CLI module"))
    print()
    
    # Check documentation
    print("Checking documentation...")
    checks.append(check_file_exists("CHANGELOG.md", "CHANGELOG.md"))
    checks.append(check_file_exists("CONTRIBUTING.md", "CONTRIBUTING.md"))
    checks.append(check_file_exists("DEPLOY.md", "DEPLOY.md"))
    checks.append(check_file_exists("DEPLOYMENT_CHECKLIST.md", "DEPLOYMENT_CHECKLIST.md"))
    print()
    
    # Check tests
    print("Checking tests...")
    checks.append(check_file_exists("tests/__init__.py", "Tests __init__.py"))
    checks.append(check_file_exists("tests/test_ctfscan.py", "Test module"))
    print()
    
    # Summary
    print("=" * 60)
    passed = sum(checks)
    total = len(checks)
    print(f"Result: {passed}/{total} checks passed")
    
    if passed == total:
        print("✓ All checks passed! Ready for PyPI deployment.")
        return 0
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(verify_structure())
