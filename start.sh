#!/usr/bin/env bash
export PYTHONPATH=$pwd;
export DJANGO_SETTINGS_MODULE=djangoDemo.db.settings.local;
python djangoDemo/conf/service_app.py