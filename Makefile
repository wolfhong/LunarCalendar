PYTHON := python
PYTEST := pytest

.PHONY: test clean package package-test

test:
	PYTHONPATH=./ $(PYTEST) -v tests/

clean:
	rm -rf dist build

package: clean
	$(PYTHON) setup.py sdist bdist_wheel
	twine upload dist/*

package-test: clean
	$(PYTHON) setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
