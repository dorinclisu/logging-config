import json
import logging
import os

os.environ['LOG_LEVEL'] = 'DEBUG'     # use 'INFO' for production deployment
os.environ['LOG_TIMESTAMP'] = 'true'  # use 'false' (default) for container deployment (docker / kubernetes provide their own timestamp)
os.environ['LOG_COLORING'] = 'true'   # use 'false' if the terminal / logging system does not support ANSI color codes
os.environ['LOG_COLOR_MAP'] = json.dumps({'CRITICAL': 'red,bg_white'})  # custom color mapping, see https://github.com/borntyping/python-colorlog
import logging_config


logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
