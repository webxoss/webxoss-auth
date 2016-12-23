#!/usr/bin/env bash

uwsgi --http 127.0.0.1:80 -T --manage-script-name --mount /=main:app
