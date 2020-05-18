\MAKEFLAGS -= --silent

.PHONY: local local-docker

local:
	./scripts/run-local.sh

local-docker: vault-login
	./scripts/run-local-docker.sh