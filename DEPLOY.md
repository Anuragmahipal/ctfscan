# Quick deployment guide for ctfscan to PyPI

## Prerequisites

1. **Python 3.6+ and pip**
   ```bash
   python --version
   pip --version
   ```

2. **Build tools**
   ```bash
   pip install --upgrade setuptools wheel build twine
   ```

3. **PyPI Account**
   - Create account at https://pypi.org/account/register/
   - Create API token at https://pypi.org/manage/account/
   - Create `.pypirc` file in home directory

## Step 1: Prepare Your Repository

```bash
# Update version in setup.py if needed
nano setup.py  # Change version = "1.0.0"

# Update CHANGELOG.md with release notes
nano CHANGELOG.md

# Commit changes
git add -A
git commit -m "Prepare release v1.0.0"
git tag v1.0.0
git push origin main --tags
```

## Step 2: Build Distribution

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build source distribution and wheel
python -m build
```

## Step 3: Verify Build

```bash
# Check the distribution
twine check dist/*

# List contents
tar -tzf dist/ctfscan-1.0.0.tar.gz
```

## Step 4: Test Upload (Optional but Recommended)

```bash
# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Install from TestPyPI to verify
pip install --index-url https://test.pypi.org/simple/ ctfscan

# Test the tool
ctfscan -h
```

## Step 5: Production Upload

```bash
# Upload to official PyPI
twine upload dist/*

# Or with username
twine upload -u __token__ dist/*
```

## Step 6: Verify Installation

```bash
# Install from PyPI
pip install ctfscan

# Test it works
ctfscan -h
```

## Step 7: Create GitHub Release

1. Go to https://github.com/Anuragmahipal/ctfscan/releases
2. Click "New Release"
3. Select your tag (v1.0.0)
4. Add release notes from CHANGELOG.md
5. Click "Publish release"

## Troubleshooting

### "Invalid distribution" errors
- Run: `twine check dist/*`
- Fix issues in README.md, setup.py, or CHANGELOG.md

### Authentication fails
- Check `.pypirc` file is in home directory
- Use `twine upload --verbose` for debugging

### Package already exists
- Increment version number in setup.py
- Rebuild and retry

## Automating with GitHub Actions

The project includes GitHub Actions workflows in `.github/workflows/`.

To enable automatic PyPI deployment:

1. Go to repository Settings → Secrets
2. Click "New repository secret"
3. Name: `PYPI_API_TOKEN`
4. Value: Your PyPI API token
5. Save
6. Push a git tag to trigger deployment: `git push origin v1.0.0`

---

For more info:
- PyPI Docs: https://packaging.python.org/
- Twine Docs: https://twine.readthedocs.io/
