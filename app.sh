#!/usr/bin/env bash

uwsgi --http 127.0.0.1:4759 -T --manage-script-name --mount /=main:app
