import json
import logging
import os
import sys

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
log_level:      str = os.getenv('LOG_LEVEL', 'DEBUG')
log_timestamp: bool = os.getenv('LOG_TIMESTAMP', '').lower() in ['true', 'yes', '1']
log_coloring:  bool = os.getenv('LOG_COLORING', 'true').lower() in ['true', 'yes', '1']
log_color_map: dict = json.loads(os.getenv('LOG_COLOR_MAP', '{}'))

logging_fmt: str = '{levelname:7} [{pathname}:{lineno:03d}]\t {message}'

if log_timestamp:
    logging_fmt = '{asctime} ' + logging_fmt

if not log_coloring:
    formatter = CustomFormatter(fmt=logging_fmt, style='{')
else:
    formatter = CustomColorFormatter(fmt='{log_color}'+logging_fmt, style='{',
        log_colors={
            'DEBUG':    'thin_white',
            'INFO':     'white',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red',
            **log_color_map
        }
    )

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logging.basicConfig(handlers=[handler], level=log_level)
