#!/bin/bash

set -e

psql -c "create database giraffe"
psql -c "create user migrator with password 'migrator' superuser"
psql -c "create user web with password 'web'"
psql -c "create user giraffe with password 'giraffe'"

pgmigrate -t latest migrate
