import json
import logging
import os
import socket
import sys
from typing import Optional

import colorlog



def strip_packages_path(pathname: str) -> str:
    return pathname.replace(sys.path[-1] + '/', '') if sys.path else pathname


class CustomFormatter(logging.Formatter):
    def format(self, record):
        message = super().format(record)
        return strip_packages_path(message)


class CustomColorFormatter(colorlog.ColoredFormatter):
    def format(self, record):
        message = super().format(record)
        return strip_packages_path(message)


###################################################################################################
true_options = ('true', 'yes', '1')

log_level:             str = os.getenv('LOG_LEVEL', 'DEBUG')
log_timestamp:        bool = os.getenv('LOG_TIMESTAMP', '').lower() in true_options
log_id_path: Optional[str] = os.getenv('LOG_ID_PATH')
log_id_template:       str = os.getenv('LOG_ID_TEMPLATE', '{hostname}-{uid}')
log_coloring:         bool = os.getenv('LOG_COLORING', 'true').lower() in true_options
log_color_map:        dict = json.loads(os.getenv('LOG_COLOR_MAP', '{}'))

###################################################################################################
if '/' in log_id_template or ' ' in log_id_template:
    raise ValueError(f'Characters "/" and " " not allowed in LOG_ID_TEMPLATE ({log_id_template})')

if log_id_path:
    if not os.path.isdir(log_id_path):
        os.makedirs(log_id_path)

    uid_filepath = os.path.join(log_id_path, '.logging_config')
    if os.path.exists(uid_filepath):
        with open(uid_filepath, 'r') as f:
            uid = f.read()
    else:
        uid = os.urandom(3).hex()
        with open(uid_filepath, 'w') as f:
            f.write(uid)

    try:
        with open('/etc/hostname', 'r') as f:
            hostname = f.read().strip(' \n')
    except:
        print('WARNING [logging_config] Could not read hostname from /etc/hostname, fallback to socket.gethostname()')
        hostname = socket.gethostname()

    id = log_id_template.format(hostname=hostname, uid=uid)
else:
    id = ''

###################################################################################################
if log_id_path:
    logging_fmt = '{levelname:7} [' + id + ' {pathname}:{lineno:03d}]\t {message}'
else:
    logging_fmt = '{levelname:7} [{pathname}:{lineno:03d}]\t {message}'

if log_timestamp:
    logging_fmt = '{asctime} ' + logging_fmt

if not log_coloring:
    formatter = CustomFormatter(fmt=logging_fmt, style='{')
else:
    formatter = CustomColorFormatter(fmt='{log_color}'+logging_fmt, style='{',
        log_colors={
            'DEBUG':    'thin_white',
            #'INFO':     'white',  # leave the default white as more pure than colorlog white
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red',
            **log_color_map
        }
    )

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logging.basicConfig(handlers=[handler], level=log_level)
