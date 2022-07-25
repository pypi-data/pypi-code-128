# -*- coding: utf-8 -*-

# Tell python that there are more sub-packages present, physically located elsewhere.
# See: https://stackoverflow.com/questions/8936884/python-import-path-packages-with-the-same-name-in-different-folders
import pkgutil

__path__ = pkgutil.extend_path(__path__, __name__)

import logging
from .version import __version__ as version
from .cloudio_attribute import cloudio_attribute
from .model_to_cloud_connector import Model2CloudConnector

# Do not output logs if logging module is not configured
logging.getLogger(__name__).addHandler(logging.NullHandler())

logging.getLogger(__name__).info(f'cloudio-glue-python version: {version}')
