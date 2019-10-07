#!/usr/bin/make

include .env

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
