ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

init-dev:
	pip install compile-env==0.4.1

compile-env:
	cd ${ROOT_DIR}/env/dev && compile-env env-spec.yaml

create-opt-paths:
	sudo mkdir -p /opt/projects/sunya/mock
	sudo chmod -R 777 /opt/projects/sunya
	sudo echo     "- cmd: echo 'start of the fish history'" >> /opt/projects/sunya/mock/fish_history
	sudo mkdir -p /opt/projects/sunya/mock/ipython
	sudo mkdir -p /opt/projects/sunya/mock/assets
	sudo touch    /opt/projects/sunya/mock/pytest_report.html
	sudo mkdir -p /opt/projects/sunya/frontend
	sudo chmod -R 777 /opt/projects/sunya
	sudo echo     "- cmd: echo 'start of the fish history'" >> /opt/projects/sunya/frontend/fish_history

create-landler-opt-paths:
	sudo mkdir -p /opt/projects/sunya/landler
	sudo chmod -R 777 /opt/projects/sunya
	sudo echo     "- cmd: echo 'start of the fish history'" >> /opt/projects/sunya/landler/fish_history
	sudo mkdir -p /opt/projects/sunya/landler/ipython
	sudo mkdir -p /opt/projects/sunya/landler/assets
	sudo touch    /opt/projects/sunya/landler/pytest_report.html
	sudo mkdir -p /opt/projects/sunya/landler/media
	sudo mkdir -p /opt/projects/sunya/landler/static
	sudo chmod -R 777 /opt/projects/sunya
