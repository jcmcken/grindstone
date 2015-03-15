from grindstone.queue import queue
import logging

LOG = logging.getLogger(__name__)

@queue.task
def add(x, y):
    return x + y

LOG.info(add.name)
