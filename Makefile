# p7doi's Makefile
#
SRC=p7doi
VENV=venv
BINUTILS=$(VENV)/bin

PIP=$(BINUTILS)/pip

COVERFILE:=.coverage
COVERAGE_REPORT:=report -m

.DEFAULT: all
.PHONY: all check check-versions stylecheck covercheck

all: check-versions

deps: $(VENV)
	$(PIP) install -qr requirements.txt

$(VENV):
	virtualenv $@

check: deps
	$(BINUTILS)/python tests/test.py

check-versions: deps
	$(BINUTILS)/tox

stylecheck: deps
	$(BINUTILS)/pep8 $(SRC)
	$(BINUTILS)/pyflakes $(SRC)/*.py

covercheck: deps
	$(BINUTILS)/coverage run --source=p7doi tests/test.py
	$(BINUTILS)/coverage $(COVERAGE_REPORT)

clean:
	rm -f *~ */*~
	rm -f $(COVERFILE)

publish: deps check-versions
	$(BINUTILS)/python setup.py sdist upload
