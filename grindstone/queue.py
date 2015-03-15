from celery import Celery
from celery.task import backend_cleanup
import grindstone.logger

queue = Celery()
queue.config_from_object('grindstone.config')

# Default tasks
queue.task(backend_cleanup)
