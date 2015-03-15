#!/bin/sh

celery -A grindstone.queue flower $@
