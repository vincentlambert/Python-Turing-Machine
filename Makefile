#
# gmake
#
SHELL := /bin/bash
PYTHON := python
SRC_PATH := src

.ONESHELL: 			# Applies to every targets in the file!
.SHELLFLAGS += -e 	# Stop at the first failure

define load_dotenv
	$(eval include ${SRC_PATH}/.env)
	$(eval export sed 's/=.*//' ${SRC_PATH}/.env)
endef

#
# Setup
#
init-venv:
	@echo "***** $@"
	${PYTHON} -m venv ./.venv

update-venv: init-venv
	@echo "***** $@"
	@source .venv/bin/activate
	cd ${SRC_PATH}
	pip install --upgrade pip
	pip install -r requirements.txt

install-black: init-venv
	@echo "***** $@"
	@source .venv/bin/activate
	cd ${SRC_PATH}
	pip install black

install-pylint: init-venv
	@echo "***** $@"
	@source .venv/bin/activate
	cd ${SRC_PATH}
	pip install pylint

install-isort: update-venv
	@echo "***** $@"
	@source .venv/bin/activate
	cd ${SRC_PATH}
	pip install isort

init-project: update-venv install-black install-pylint install-isort

#
# Run local
#
run-local:
	@echo "***** $@"
	@source .venv/bin/activate
	cd ${SRC_PATH}
	@mkdir -p temp/log
	${PYTHON} main.py

run-tests:
	@echo "***** $@"
	@source .venv/bin/activate
	cd ${SRC_PATH}
	${PYTHON} -m pytest -p no:warnings

run-mypy:
	@echo "***** $@"
	@source .venv/bin/activate
	cd backend
	${PYTHON} -m mypy --ignore-missing-imports .
