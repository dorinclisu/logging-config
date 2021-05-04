# Description
Simple logging done right. Say goodbye to print statements or complicated log configs.

By default, Python logging is too flexible and provides many ways for beginners to do it wrong. This package logging format is fairly opinionated, but is the result of experience monitoring and troubleshooting complex production systems.

So if you are an expert, you should consider using this format and fine tune it to your specific needs. If you are a beginner, you should definitely use it.

# Installation
- `pip install https://github.com/dorinclisu/logging-config/archive/master.zip`

# Example usage
Just import the package in the main file, and use the simple logging functions everywhere else.

```Python
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
```
```
2021-05-04 12:31:48,439 DEBUG   [/Users/dorinclisu/Git/logging-config/example.py:012]    Debug message
2021-05-04 12:31:48,439 INFO    [/Users/dorinclisu/Git/logging-config/example.py:013]    Info message
2021-05-04 12:31:48,439 WARNING [/Users/dorinclisu/Git/logging-config/example.py:014]    Warning message
2021-05-04 12:31:48,439 ERROR   [/Users/dorinclisu/Git/logging-config/example.py:015]    Error message
2021-05-04 12:31:48,439 CRITICAL [/Users/dorinclisu/Git/logging-config/example.py:016]   Critical message
```
