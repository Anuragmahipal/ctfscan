# DEPLOYMENT_CHECKLIST.md

## ✅ Pre-Deployment Checklist for PyPI

Before deploying `ctfscan` to PyPI, verify all items:

### Project Structure ✓
- [x] `src/ctfscan/` - Main package directory
  - [x] `__init__.py` - Package initialization
  - [x] `core.py` - Core scanner functionality
  - [x] `cli.py` - Command-line interface
- [x] `tests/` - Unit tests
- [x] `setup.py` - Setup configuration (setuptools)
- [x] `pyproject.toml` - Modern Python project config
- [x] `MANIFEST.in` - Package manifest
- [x] `README.md` - Project documentation
- [x] `LICENSE` - MIT License
- [x] `CHANGELOG.md` - Release notes
- [x] `CONTRIBUTING.md` - Contribution guidelines
- [x] `requirements-dev.txt` - Dev dependencies
- [x] `.gitignore` - Git ignore rules
- [x] `.github/workflows/tests-and-deploy.yml` - CI/CD pipeline

### Metadata Validation ✓
- [x] `name` = "ctfscan"
- [x] `version` = "1.0.0"
- [x] `author` = "Anuragmahipal"
- [x] `author_email` = "your-email@example.com" (⚠️ UPDATE THIS)
- [x] `description` = Clear and concise
- [x] `long_description` = Formatted as markdown
- [x] `url` = GitHub repository URL
- [x] `license` = "MIT"
- [x] `keywords` = Relevant search terms
- [x] `classifiers` = Correct categories
- [x] `python_requires` = ">=3.6"

### Code Quality ✓
- [x] `__init__.py` properly exports public APIs
- [x] Functions have docstrings
- [x] Error handling is implemented
- [x] Code follows PEP 8 style
- [x] No hardcoded paths or credentials
- [x] Command-line interface works correctly

### Documentation ✓
- [x] README.md includes PyPI installation instructions
- [x] README.md has examples and usage info
- [x] CHANGELOG.md documents version 1.0.0
- [x] CONTRIBUTING.md guides contributors
- [x] Code includes docstrings
- [x] No TODO or FIXME comments

### Testing ✓
- [x] Unit tests exist in `tests/`
- [x] Tests cover main functionality
- [x] Tests can be run with: `pytest tests/`

### Build Verification ✓
- [x] setup.py is syntactically correct
- [x] pyproject.toml is valid TOML
- [x] MANIFEST.in includes all necessary files
- [x] No circular imports
- [x] Console script entry point defined

### Entry Point ✓
- [x] CLI entry point: `ctfscan = ctfscan.cli:main`
- [x] Command works: `ctfscan -h`
- [x] Installation creates `/bin/ctfscan` (or Windows equivalent)

---

## 🚀 Ready to Deploy!

### Step 1: Setup PyPI Credentials
```bash
# Create PyPI account: https://pypi.org/account/register/
# Create API token: https://pypi.org/manage/account/

# Create ~/.pypirc (or %APPDATA%\pip\pip.ini on Windows)
[distutils]
index-servers =
    pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi_xxxxxxxxxxxx...
```

### Step 2: Update Author Email (IMPORTANT!)
```bash
# In setup.py and pyproject.toml:
# Change: author_email = "your-email@example.com"
# To: author_email = "your-actual-email@example.com"
```

### Step 3: Build Distribution
```bash
pip install --upgrade build twine
python -m build
```

### Step 4: Verify Distribution
```bash
twine check dist/*
```

### Step 5: Test Upload (Optional)
```bash
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ --no-deps ctfscan
ctfscan -h
```

### Step 6: Production Upload
```bash
twine upload dist/*
```

### Step 7: Verify Installation
```bash
pip install ctfscan
ctfscan -h
```

---

## 📝 Important Notes

1. **Author Email**: Update the email address in both `setup.py` and `pyproject.toml`
2. **GitHub URL**: Ensure the repository URL is correct and public
3. **Version**: Only increment when making changes
4. **PyPI API Token**: Keep secure, never commit to repository
5. **Testing**: Run tests locally before uploading

---

## 🔗 Useful Links

- PyPI: https://pypi.org/project/ctfscan/
- Package Index: https://pypi.org/
- Packaging Guide: https://packaging.python.org/
- Twine Documentation: https://twine.readthedocs.io/

---

See `DEPLOY.md` for detailed deployment instructions.
