#from grindstone.queue import queue
#from grindstone.config import IMPORT_TASKS
#import grindstone.logger
#import logging
#
#LOG = logging.getLogger(__name__)
#
#def import_task_module(module):
#    try:
#        imported = __import__(module)
#        LOG.info('succesfully imported task module "%s" from %s' %\
#            (module, imported.__file__))
#    except ImportError:
#        LOG.error('failed to load task module "%s"' % module)
#    return imported
#
#map(import_task_module, IMPORT_TASKS)
