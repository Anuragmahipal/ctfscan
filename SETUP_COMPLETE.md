# 🚀 ctfscan PyPI Deployment Guide - Complete Setup

## Summary

Your `ctfscan` project is now **fully prepared** for PyPI deployment! Here's what has been set up:

### ✅ What's Been Done

1. **Python Package Structure**
   - Converted bash script to Python (Python 3.6+)
   - Created `src/ctfscan/` package with proper modules
   - Entry point configured for `ctfscan` command

2. **PyPI Configuration**
   - `setup.py` with all required metadata
   - `pyproject.toml` for modern Python packaging
   - `MANIFEST.in` for file inclusion
   - `LICENSE` (MIT) included

3. **Documentation**
   - Updated README.md for PyPI
   - CHANGELOG.md for version history
   - CONTRIBUTING.md for contributors
   - DEPLOY.md with detailed instructions
   - DEPLOYMENT_CHECKLIST.md with verification steps

4. **Testing & CI/CD**
   - Unit tests in `tests/` directory
   - GitHub Actions workflow for automated testing and deployment
   - Tests cover all major functionality

5. **Development Setup**
   - requirements-dev.txt for development dependencies
   - .gitignore properly configured
   - verification script to check structure

---

## 📋 Pre-Deployment Steps (IMPORTANT!)

### Step 1: Update Author Email
Your email address is currently a placeholder. Update it:

**In `setup.py` (line ~13):**
```python
author_email='your-actual-email@example.com',
```

**In `pyproject.toml` (line ~6):**
```toml
authors = [
    {name = "Anuragmahipal", email = "your-actual-email@example.com"},
]
```

### Step 2: Create PyPI Account
1. Go to https://pypi.org/account/register/
2. Create an account
3. Navigate to https://pypi.org/manage/account/
4. Create an API token for automated uploads

### Step 3: Configure PyPI Credentials

**On Linux/macOS:**
Create `~/.pypirc`:
```
[distutils]
index-servers =
    pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi_XXXXXXXXXXXXXXXXXXX
```

**On Windows:**
Create `%APPDATA%\pip\pip.ini`:
```
[distutils]
index-servers =
    pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi_XXXXXXXXXXXXXXXXXXX
```

---

## 🔨 Deployment Commands

### Option A: Manual Deployment (Recommended for First Upload)

```bash
# 1. Install build tools
pip install --upgrade setuptools wheel build twine

# 2. Clean previous builds
rm -rf build/ dist/ *.egg-info

# 3. Build distribution
python -m build

# 4. Verify the build
twine check dist/*

# 5. Upload to PyPI
twine upload dist/*
```

### Option B: Automated Deployment (GitHub Actions)

To enable automatic deployment on git tags:

1. Go to your GitHub repository
2. Settings → Secrets and variables → Actions
3. New repository secret:
   - Name: `PYPI_API_TOKEN`
   - Value: (Your PyPI API token from account)
4. Save
5. Deploy by pushing a tag: `git push origin v1.0.0`

---

## 🧪 Testing Before Deployment

### Run Unit Tests
```bash
pip install pytest
pytest tests/ -v
```

### Test Local Installation
```bash
pip install -e .
ctfscan -h
```

### Test PyPI Upload (Optional)
```bash
# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --no-deps ctfscan

# Test it
ctfscan -h
```

---

## 📦 After Deployment

### Verify Installation Works
```bash
# Uninstall test version
pip uninstall ctfscan

# Install from PyPI
pip install ctfscan

# Test
ctfscan -h
```

### Check PyPI Package
Visit: https://pypi.org/project/ctfscan/

### Create GitHub Release
1. Go to https://github.com/Anuragmahipal/ctfscan/releases
2. New Release → Select tag v1.0.0
3. Add CHANGELOG.md notes
4. Publish

---

## 📂 Project Structure

```
ctfscan/
├── src/
│   └── ctfscan/
│       ├── __init__.py          # Package exports
│       ├── core.py              # Main functionality
│       └── cli.py               # Command-line interface
├── tests/
│   ├── __init__.py
│   └── test_ctfscan.py          # Unit tests
├── .github/
│   └── workflows/
│       └── tests-and-deploy.yml # GitHub Actions CI/CD
├── setup.py                     # setuptools configuration
├── pyproject.toml               # Modern Python config
├── MANIFEST.in                  # Package manifest
├── README.md                    # Documentation
├── LICENSE                      # MIT License
├── CHANGELOG.md                 # Version history
├── CONTRIBUTING.md              # Contribution guide
├── DEPLOY.md                    # Deployment guide
├── DEPLOYMENT_CHECKLIST.md      # Pre-deployment checklist
├── requirements-dev.txt         # Dev dependencies
├── .gitignore                   # Git ignore rules
└── verify_structure.py          # Verification script
```

---

## 🎯 Quick Checklist

Before uploading to PyPI:

- [ ] Updated author email in setup.py and pyproject.toml
- [ ] Created PyPI account
- [ ] Created and saved PyPI API token
- [ ] Configured ~/.pypirc or %APPDATA%\pip\pip.ini
- [ ] Ran verification script: `python verify_structure.py`
- [ ] Ran unit tests: `pytest tests/ -v`
- [ ] Tested local installation: `pip install -e .`
- [ ] Built distribution: `python -m build`
- [ ] Verified build: `twine check dist/*`

---

## 🐛 Troubleshooting

### "twine not found"
```bash
pip install twine
```

### "Build directory exists"
```bash
rm -rf build/ dist/ *.egg-info
```

### "Invalid distribution"
```bash
twine check dist/*
# Check README.md and setup.py for formatting errors
```

### "Authentication failed"
- Verify PyPI API token is correct
- Check .pypirc file exists and is readable
- Try: `twine upload --verbose dist/*`

---

## 📚 Useful Resources

- **PyPI Help**: https://pypi.org/help/
- **Packaging Guide**: https://packaging.python.org/
- **Twine Docs**: https://twine.readthedocs.io/
- **Setup.py Guide**: https://setuptools.pypa.io/
- **PEP 440 Versioning**: https://www.python.org/dev/peps/pep-0440/

---

## 🎉 You're Ready!

Your package is production-ready. Follow the deployment steps above and your `ctfscan` tool will be available on PyPI!

```bash
# Users will be able to install it with:
pip install ctfscan
```

---

**Questions or Issues?**
Open an issue on GitHub: https://github.com/Anuragmahipal/ctfscan/issues
