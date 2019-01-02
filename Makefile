VENV = .lair
VIRTUALENV = virtualenv
BIN = $(VENV)/bin
PYTHON = $(BIN)/python

INSTALL = $(BIN)/pip install

.PHONY: all test docs build_extras dist build

all: build

$(PYTHON):
	$(VIRTUALENV) $(VTENV_OPTS) $(VENV)

build: $(PYTHON)
	$(PYTHON) setup.py develop

clean:
	rm -rf $(VENV)

test_dependencies:
	$(INSTALL) -r test-requirements.txt

test: build test_dependencies
	$(BIN)/flake8 lair
	$(BIN)/tox

run:
	FLASK_APP=lair bin/flask run

dist:
	$(INSTALL) wheel
	$(PYTHON) setup.py sdist bdist_wheel
