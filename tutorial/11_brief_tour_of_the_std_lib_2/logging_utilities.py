#!/usr/bin/env python

import logging

# Send log messages to stderr
# Level: DEBUG (restricted by default)
logging.debug('Debugging information')
# Level: INFO (restricted by default)
logging.info('Informational message')
# Level: WARNING
logging.warning('Warning:config file %s not found', 'server.conf')
# Level: ERROR
logging.error('Error occured')
# Level: CRITICAL
logging.critical('Critical error -- shutting down')
