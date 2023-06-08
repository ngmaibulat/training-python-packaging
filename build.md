### Docs:

-   [Python Packaging User Guide](https://packaging.python.org/)
-   https://packaging.python.org/en/latest/specifications/declaring-project-metadata/
-   https://packaging.python.org/en/latest/distributing.html
-   https://packaging.python.org/en/latest/tutorials/packaging-projects/
-   https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use
-   https://packaging.python.org/en/latest/key_projects/#twine

### Install, during dev:

```bash
pip install -e .
```

### Build:

```bash
pip install build
python -m build --sdist .
python -m build --wheel .
```

### Publish:

```bash
python -m twine upload dist/ngm_salam-0.0.4.tar.gz dist/ngm_salam-0.0.4-py3-none-any.whl
```
