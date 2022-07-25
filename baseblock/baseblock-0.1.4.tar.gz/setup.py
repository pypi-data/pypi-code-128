# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['baseblock']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==6.0', 'cryptography==37.0.4', 'plac']

setup_kwargs = {
    'name': 'baseblock',
    'version': '0.1.4',
    'description': 'Base Block of Common Enterprise Python Utilities',
    'long_description': None,
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
