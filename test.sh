#!/usr/bin/env bash
pipenv install
pipenv shell
pytest -vvv -s tests/test_apt_install.py