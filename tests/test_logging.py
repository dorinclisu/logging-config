import logging

import pytest
import requests

import src.logging_config



def test_basic_logging():
    logging.debug('Debug message')
    logging.info('Info message')
    logging.warning('Warning message')
    logging.error('Error message')

def test_package_logging():
    requests.get('https://google.com')


if __name__ == '__main__':
    test_basic_logging()
    test_package_logging()
