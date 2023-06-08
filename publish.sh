python -m pytest

rm -rf dist
rm -rf build

python -m build --sdist .
python -m build --wheel .

python -m twine upload dist/*
