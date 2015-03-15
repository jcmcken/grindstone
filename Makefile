.PHONY: test venv

test:
	env -i nosetests --with-coverage --cover-package grindstone grindstone/tests

venv:
	bash scripts/venv.sh
