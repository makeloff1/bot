#!/usr/bin/env bash

set -x
set -u

pipenv run flask run --host=0.0.0.0 --port=10090
