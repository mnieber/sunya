#
# React
#

install:
	yarn install

run-server:
	yarn dev --host

create-bundle:
	rm -rf /app/bundle/*
	yarn build
	cp -rf ./build/* /app/bundle

#
# Stack
#

init-dev: \
	install
