import os
import string
import celery
from grindstone.util import import_file

# Grindstone Defaults
#
DEFAULT_ENV = 'development'
ENVIRONMENT = os.environ.get('GRINDSTONE_ENV', DEFAULT_ENV)
DEFAULT_CONFIG = os.path.join(os.path.expanduser('~'), '.grindstone')
OVERRIDE_CONFIG = os.environ.get('GRINDSTONE_CONFIG', DEFAULT_CONFIG)
LOG_LEVEL = os.environ.get('GRINDSTONE_LOG_LEVEL', 'INFO')
LOG_STDOUT = os.environ.get('GRINDSTONE_LOG_STDOUT', 'true') == 'true'

# Modules from which `grindstone' should auto-load tasks
#
CELERY_IMPORTS = ('foobar.tasks',)
    
# Celery Defaults
#
BROKER_URL = 'mongodb://localhost:27017/celery'
BROKER_BACKEND = 'mongodb'
CELERY_RESULT_BACKEND = 'mongodb'
# long-running jobs should not suffer because of broker
# restarts
CELERY_RESULT_PERSISTENT = True
CELERY_TASK_RESULT_EXPIRES = 60*60*24
CELERYBEAT_SCHEDULE = {
  'expire-results': {
    'task': 'celery.backend_cleanup',
    'schedule': 60*60,
  }
}

if ENVIRONMENT == 'test':
    BROKER_BACKEND = 'memory'
    # block until tasks complete
    CELERY_ALWAYS_EAGER = True
    CELERY_EAGER_PROPOGATES_EXCEPTIONS = True
elif ENVIRONMENT == 'development':
    # expire results after 30 seconds
    CELERY_TASK_RESULT_EXPIRES = 30
    # run expiry every 30 seconds too
    CELERYBEAT_SCHEDULE['expire-results']['schedule'] = 30

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Config Overrides/Customizations
#
if os.path.isfile(OVERRIDE_CONFIG):
    override = import_file(OVERRIDE_CONFIG)
    valid_options = ( i for i in dir(override) if i[0] in string.ascii_uppercase ) 
    for option in valid_options:
        globals()[option] = getattr(override, option)
