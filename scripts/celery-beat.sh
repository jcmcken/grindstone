#!/bin/sh

celery -A grindstone.queue beat $@
