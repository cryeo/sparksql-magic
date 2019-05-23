.PHONY: prepare
prepare:
	pipenv install --dev

.PHONY: test
test: prepare
	pytest

.PHONY: clean
clean:
	rm -rf sparksql_magic.egg-info build dist
.PHONY: dist
dist: clean
	python setup.py sdist bdist_wheel
