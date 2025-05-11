# Publishing VisionLLM to PyPI

This guide explains how to build and publish the VisionLLM package to PyPI.

## Prerequisites

- Poetry installed (`pip install poetry`)
- PyPI account (create one at [pypi.org](https://pypi.org/account/register/))
- API token from PyPI (create one at [pypi.org/manage/account/token/](https://pypi.org/manage/account/token/))

## Build the package

```bash
# Make sure you're in the project root directory
cd /path/to/visionllm

# Build the package
poetry build
```

This will create both the wheel (.whl) and source distribution (.tar.gz) files in the `dist/` directory at the project root.

## Publish to PyPI

### First-time setup

Configure Poetry with your PyPI token:

```bash
poetry config pypi-token.pypi YOUR_PYPI_TOKEN
```

### Publishing

```bash
# Publish to PyPI
poetry publish

# Or build and publish in one step
poetry publish --build
```

### Publishing to TestPyPI (optional)

If you want to test the publishing process before releasing to the main PyPI:

```bash
# Configure TestPyPI
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi YOUR_TESTPYPI_TOKEN

# Publish to TestPyPI
poetry publish -r testpypi
```

## Versioning

To update the version for a new release:

```bash
# Update version (patch, minor, or major)
poetry version patch  # Increments from 0.1.0 to 0.1.1
# or
poetry version minor  # Increments from 0.1.0 to 0.2.0
# or
poetry version major  # Increments from 0.1.0 to 1.0.0

# Or set a specific version
poetry version 0.2.0
```

## Verifying the published package

After publishing, you can verify the installation works:

```bash
# Create a new virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install the package from PyPI
pip install visionllm

# Test the installation
visionllm --version
```

## Common issues

- **Package name already exists**: Someone else might have claimed the package name. Check PyPI to make sure the name is available.
- **Invalid credentials**: Make sure your PyPI token is correctly configured.
- **Version conflict**: You cannot upload a package with the same version twice. Make sure to increment the version number for each release.
- **Project structure**: Ensure you're running Poetry commands from the root directory of the project, not from within the visionllm subdirectory. 