#!/usr/bin/make

include .env

SHELL = /bin/sh
CURRENT_UID := $(shell id -u):$(shell id -g)

export CURRENT_UID

reqs:
	pipenv lock -r > ./bot/requirements.txt
up:
	docker-compose up -d
upb:
	docker-compose up -d --force-recreate --build
down:
	docker-compose down
sh:
	docker exec -it /tel_bot /bin/sh
