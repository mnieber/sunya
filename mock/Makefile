#
# Python
#

install:
	pip install -r .requirements/dev.txt

pip-compile:
	pip-compile .requirements/base.in -o .requirements/base.txt
	pip-compile .requirements/dev.in -o .requirements/dev.txt

#
# Stack
#

init-dev: \
	pip-compile \
	install
