#
# Python
#

pip-compile:
	uv pip compile --upgrade .requirements/requirements.in .requirements/requirements.editable -o .requirements/requirements.txt

install:
	pip install -e . -r .requirements/requirements.txt -r .requirements/requirements.dev.txt

#
# Stack
#

init-dev: \
	pip-compile \
	install
