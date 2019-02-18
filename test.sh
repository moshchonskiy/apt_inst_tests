#!/usr/bin/env bash
pipenv install
pytest -vvv -s tests/test_apt_install.py