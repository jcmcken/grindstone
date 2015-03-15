import logging
from grindstone.config import LOG_LEVEL, LOG_STDOUT

def log_level(level):
    return getattr(logging, level.upper(), 'INFO')

LOG = logging.getLogger()
LOG.setLevel(log_level(LOG_LEVEL))

if LOG_STDOUT:
    logging.basicConfig()
