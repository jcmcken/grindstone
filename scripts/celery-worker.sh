#!/bin/sh

celery -A grindstone.queue worker $@
