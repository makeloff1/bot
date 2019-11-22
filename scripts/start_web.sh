#!/usr/bin/env bash

set -x
set -u

pipenv run flask db init
pipenv run flask db migrate
pipenv run flask db upgrade
pipenv run flask run --host=0.0.0.0 --port=10090
