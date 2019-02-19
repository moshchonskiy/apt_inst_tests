# apt-get install tests example



Requirements
------------

- [Docker](https://docs.docker.com/install/)


Notes
-----

Tests are executed inside docker container

CI
--

CircleCI runs tests on branches 
[![CircleCI](https://circleci.com/gh/moshchonskiy/apt_inst_tests.svg?style=svg)](https://circleci.com/gh/moshchonskiy/apt_inst_tests)


Tests
-----
To run tests locally:

- Clone repository

- Build docker ./build_docker.sh

- Tests can be executed by ./test.sh
