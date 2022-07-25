# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brevettiai',
 'brevettiai.data',
 'brevettiai.data.image',
 'brevettiai.interfaces',
 'brevettiai.io',
 'brevettiai.model',
 'brevettiai.model.factory',
 'brevettiai.model.metadata',
 'brevettiai.platform',
 'brevettiai.platform.models',
 'brevettiai.tests',
 'brevettiai.utils']

package_data = \
{'': ['*'], 'brevettiai.tests': ['bin/*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0',
 'altair==4.1.0',
 'backoff>=1.10',
 'configparser>=5.0',
 'cryptography>=36.0.1',
 'h5py>=3.6.0,<4.0.0',
 'minio>=7.0,<7.1',
 'mmh3>=3.0',
 'numpy>=1.18.1',
 'onnxruntime>=1.6.0',
 'pandas>=1.1,<1.2',
 'plotly>=4.14.3',
 'py7zr>=0.18.9,<0.19.0',
 'pydantic>=1.9.0,!=1.9.1',
 'requests>=2.23',
 'scikit-learn>=0.23.1',
 'shapely>=1.7.0',
 'tf2onnx>=1.9.0',
 'toml>=0.10.2,<0.11.0',
 'tqdm>=4.62']

extras_require = \
{':(python_version >= "3.7" and python_version < "3.11") and (extra == "tf")': ['tensorflow-io-gcs-filesystem'],
 'cv2': ['opencv-python>=4.1'],
 'cv2-headless': ['opencv-python-headless>=4.1'],
 'tf': ['tensorflow>=2.7'],
 'tfa': ['tensorflow_addons>=0.16.1']}

setup_kwargs = {
    'name': 'brevettiai',
    'version': '0.5.6',
    'description': 'Brevetti AI library',
    'long_description': '# Brevetti AI core library\nThe brevettiai library enables integration with the [brevetti.ai](https://brevetti.ai) platform for development of training packages\n\nThe library is used as an API through the Job class with a number of utility functions for easy development of models.\nThe tools support both local development on linux and windows as well as hosted training on e.g. Amazon Web Services sagemaker platform.\n\n## Contents\nDeveloper documentation can be found at [docs.brevetti.ai](https://docs.brevetti.ai/) and generated [package documentation](https://s3.eu-west-1.amazonaws.com/public.data.criterion.ai/documentation/brevettiai%200.3.7/index.html) is also\n',
    'author': 'Emil Tyge',
    'author_email': 'emil@brevetti.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://platform.brevetti.ai',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
