SHELL = /bin/sh +x
export PATH := ./bin:$(PATH)
PACKAGE_NAME ?= differencesvc
VIRTUALENV_NAME ?= differencesvc
# `make APP_PORT=8080 run` to run on port other than default
APP_PORT ?= 8000
APP_DIR ?= exampleapp
# `make SETUP_PY_TARGET=develop install` to install as "developer egg"
SETUP_PY_TARGET ?= install
GIT_BRANCH ?= master
INSTALL_ROOT ?= $(HOME)

# Each of your targets should be listed as .PHONY (unless you are actually
# compiling a C source file or similar)
# :r! grep '^[a-z-]\+:' % | cut -d: -f1 | sort | tr "\n" " "
.PHONY: config edit install package-deps run test uninstall virtualenv 
# first target is default, let it be something harmless
config:


# dev-helper targets

edit:
	vim README.md Makefile requirements.txt setup.py `find ./$(PACKAGE_NAME) ./sql ./$(APP_DIR) \( -path '*.egg-info' -o -path '*/build/*' -o -name 'jquery*' -o -name __init__.py -o -name '*.egg' -o -name '*.pyc' -o -name '*.swp' -o -name '*.swo' -o -iname '*.ico' -o -iname '*.png' -o -iname '*.gif' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.pdf' -o -iname '*.doc' \) -prune  -o -type f  -print`

test:
	nosetests  -sv --with-doctest --logging-level=INFO --cover-branches --with-coverage --cover-erase --cover-package=$(PACKAGE_NAME) $(PACKAGE_NAME)

# runtime targets

run:
	. ./bin/activate && ./$(APP_DIR)/app.py --port=$(APP_PORT) --debug

# installation targets

install: virtualenv
	git pull origin $(GIT_BRANCH) && . ./bin/activate && ./setup.py $(SETUP_PY_TARGET)

package-deps:
	sudo aptitude update && sudo aptitude safe-upgrade && sudo aptitude install git make python2.7 python-dev python-pip python-virtualenv

requirements:
	. ./bin/activate && pip freeze > requirements.txt

uninstall:
	. ./bin/activate && yes | pip uninstall $(PACKAGE_NAME)

virtualenv:
	virtualenv --python=/usr/bin/python2.7 --no-site-packages --setuptools --prompt="[$(VIRTUALENV_NAME)]" . && \
	. ./bin/activate && pip install -r requirements.txt

# make is notoriously picky about formatting, these settings should make it
# reasonably safe to edit it with vim.  You might also want to frequently do:
# :%s/\s\+$// to remove all trailing whitespace
# vim: set noexpandtab shiftwidth=8 softtabstop=8 tabstop=8:
