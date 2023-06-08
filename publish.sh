rm -rf dist

python -m build --sdist .
python -m build --wheel .

python -m twine upload dist/ngm_salam-0.*.tar.gz dist/ngm_salam-0.*-py3-none-any.whl
