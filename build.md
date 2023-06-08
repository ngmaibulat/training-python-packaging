### Docs:

-   https://realpython.com/lessons/python-packages-virtual-env/
-   [Python Packaging User Guide](https://packaging.python.org/)
-   https://packaging.python.org/en/latest/specifications/declaring-project-metadata/
-   https://packaging.python.org/en/latest/distributing.html
-   https://packaging.python.org/en/latest/tutorials/packaging-projects/
-   https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use
-   https://packaging.python.org/en/latest/key_projects/#twine

### Test Repository

-   https://test.pypi.org/

### Config

.pypirc:

```ini
[distutils]
index-servers =
    pypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: username
password: password
```

### Install, during dev:

```bash
pip install -e .
```

### Build:

```bash
pip install build
pip install twine
rm -fr dist
python -m build --sdist .
python -m build --wheel .
```

### Publish:

```bash
python -m twine upload dist/*
```
