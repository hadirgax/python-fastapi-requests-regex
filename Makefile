ENV_NAME ?= pythonenv

#### Hooks ####

install-git-hooks:
	pre-commit install

uninstall-git-hooks:
	pre-commit uninstall


##### Env #####

env-create:
	conda env create -n $(ENV_NAME) -f environment_dev.yml

env-remove:
	conda env remove -n $(ENV_NAME)

env-update: env-remove env-create

##### Run #####

run-app:
	./scripts/run.sh


##### Test #####

smoke-test:
	./test/smoke-test.sh
