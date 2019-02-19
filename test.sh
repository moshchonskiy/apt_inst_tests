#!/usr/bin/env bash

docker run -t apt_tests /bin/bash -c 'pipenv run pytest -vvv -s --junit-xml=./test-results tests/test_apt_install.py'