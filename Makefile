ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

init-dev:
	pip install compile-env==0.4.1

compile-env:
	cd ${ROOT_DIR}/envs/local/compile-env/blogs && compile-env ./env-spec.yaml
	cd ${ROOT_DIR}/envs/local/compile-env/darshana && compile-env ./env-spec.yaml
	cd ${ROOT_DIR}/envs/local/compile-env/landler && compile-env ./env-spec.yaml

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

create-blogs-be-opt-paths:
	sudo mkdir -p /opt/projects/sunya/blogs_be
	sudo chmod -R 777 /opt/projects/sunya
	sudo echo     "- cmd: echo 'start of the fish history'" >> /opt/projects/sunya/blogs_be/fish_history
	sudo mkdir -p /opt/projects/sunya/blogs_be/ipython
	sudo mkdir -p /opt/projects/sunya/blogs_be/assets
	sudo touch    /opt/projects/sunya/blogs_be/pytest_report.html
	sudo mkdir -p /opt/projects/sunya/blogs_be/media
	sudo mkdir -p /opt/projects/sunya/blogs_be/static
	sudo chmod -R 777 /opt/projects/sunya

create-darshana-be-opt-paths:
	sudo mkdir -p /opt/projects/sunya/darshana_be
	sudo chmod -R 777 /opt/projects/sunya
	sudo echo     "- cmd: echo 'start of the fish history'" >> /opt/projects/sunya/darshana_be/fish_history
	sudo mkdir -p /opt/projects/sunya/darshana_be/ipython
	sudo mkdir -p /opt/projects/sunya/darshana_be/assets
	sudo touch    /opt/projects/sunya/darshana_be/pytest_report.html
	sudo mkdir -p /opt/projects/sunya/darshana_be/media
	sudo mkdir -p /opt/projects/sunya/darshana_be/static
	sudo chmod -R 777 /opt/projects/sunya

create-landler-be-opt-paths:
	sudo mkdir -p /opt/projects/sunya/landler_be
	sudo chmod -R 777 /opt/projects/sunya
	sudo echo     "- cmd: echo 'start of the fish history'" >> /opt/projects/sunya/landler_be/fish_history
	sudo mkdir -p /opt/projects/sunya/landler_be/ipython
	sudo mkdir -p /opt/projects/sunya/landler_be/assets
	sudo touch    /opt/projects/sunya/landler_be/pytest_report.html
	sudo mkdir -p /opt/projects/sunya/landler_be/media
	sudo mkdir -p /opt/projects/sunya/landler_be/static
	sudo chmod -R 777 /opt/projects/sunya
