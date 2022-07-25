# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_mail', 'fastapi_mail.email_utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'aiosmtplib>=1.1.6,<2.0.0',
 'blinker>=1.5,<2.0',
 'email-validator>=1.1.3,<2.0.0',
 'pydantic>=1.8.2,<2.0.0']

extras_require = \
{'fakeredis': ['fakeredis[fakeredis]>=1.8.2,<2.0.0'],
 'httpx': ['httpx[httpx]>=0.23.0,<0.24.0']}

setup_kwargs = {
    'name': 'fastapi-mail',
    'version': '1.1.4',
    'description': 'Simple lightweight mail library for FastApi',
    'long_description': '\n# Fastapi-mail\n\nThe fastapi-mail simple lightweight mail system, sending emails and attachments(individual && bulk)\n\n\n[![MIT licensed](https://img.shields.io/github/license/sabuhish/fastapi-mail)](https://raw.githubusercontent.com/sabuhish/fastapi-mail/master/LICENSE)\n[![GitHub stars](https://img.shields.io/github/stars/sabuhish/fastapi-mail.svg)](https://github.com/sabuhish/fastapi-mail/stargazers)\n[![GitHub forks](https://img.shields.io/github/forks/sabuhish/fastapi-mail.svg)](https://github.com/sabuhish/fastapi-mail/network)\n[![GitHub issues](https://img.shields.io/github/issues-raw/sabuhish/fastapi-mail)](https://github.com/sabuhish/fastapi-mail/issues)\n[![Downloads](https://pepy.tech/badge/fastapi-mail)](https://pepy.tech/project/fastapi-mail)\n\n\n###  🔨  Installation ###\n\n```sh\n $ pip install fastapi-mail\n```\n\n---\n**Documentation**: [FastApi-MAIL](https://sabuhish.github.io/fastapi-mail/)\n---\n\n\nThe key features are:\n\n-  sending emails with either with FastApi or using asyncio module \n-  sending emails using FastApi background task managment\n-  sending files either from form-data or files from server\n-  Using Jinja2 HTML Templates\n-  email utils (utility allows you to check temporary email addresses, you can block any email or domain)\n-  email utils has two available classes ```DefaultChecker``` and  ```WhoIsXmlApi```\n-  Unittests using FastapiMail\n\nMore information on [Getting-Started](https://sabuhish.github.io/fastapi-mail/getting-started/)\n\n\n### Guide\n\n\n```python\n\nfrom fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form\nfrom starlette.responses import JSONResponse\nfrom starlette.requests import Request\nfrom fastapi_mail import FastMail, MessageSchema,ConnectionConfig\nfrom pydantic import BaseModel, EmailStr\nfrom typing import List\n\n\n\nclass EmailSchema(BaseModel):\n    email: List[EmailStr]\n\n\nconf = ConnectionConfig(\n    MAIL_USERNAME = "YourUsername",\n    MAIL_PASSWORD = "strong_password",\n    MAIL_FROM = "your@email.com",\n    MAIL_PORT = 587,\n    MAIL_SERVER = "your mail server",\n    MAIL_TLS = True,\n    MAIL_SSL = False,\n    USE_CREDENTIALS = True,\n    VALIDATE_CERTS = True\n)\n\napp = FastAPI()\n\n\nhtml = """\n<p>Thanks for using Fastapi-mail</p> \n"""\n\n\n@app.post("/email")\nasync def simple_send(email: EmailSchema) -> JSONResponse:\n\n    message = MessageSchema(\n        subject="Fastapi-Mail module",\n        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass \n        body=html,\n        subtype="html"\n        )\n\n    fm = FastMail(conf)\n    await fm.send_message(message)\n    return JSONResponse(status_code=200, content={"message": "email has been sent"})     \n```\n\n## List of Examples\n\nFor more examples of using fastapi-mail please check [example](https://sabuhish.github.io/fastapi-mail/example/) section\n\n# Contributing\nFeel free to open issues and send pull requests.\n\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([🚧](https://sabuhish.github.io/fastapi-mail/example.html)):\n\n\n<table>\n  <tr>\n    <td align="center"><a href="https://github.com/sabuhish"><img src="https://avatars.githubusercontent.com/u/46589585?v=3" width="100px;" alt=""/><br /><sub><b>Sabuhi Shukurov</b></sub></a><br /><a href="#maintenance-tbenning" title="Answering Questions">💬</a> <a href="https://github.com/sabuhish/fastapi-mail/" title="Reviewed Pull Requests">👀</a> <a href="#maintenance-jakebolam" title="Maintenance">🚧</a></td>\n    <td align="center"><a href="https://github.com/Turall"><img src="https://avatars.githubusercontent.com/u/32899328?v=3" width="100px;" alt=""/><br /><sub><b>Tural Muradov</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a href="https://github.com/sabuhish/fastapi-mail/" title="Reviewed Pull Requests">👀</a> <a href="#tool-jfmengels" title="Tools">🔧</a></td>\n    <td align="center"><a href="https://github.com/AliyevH"><img src="https://avatars.githubusercontent.com/u/5507950?v=3" width="100px;" alt=""/><br /><sub><b>Hasan Aliyev</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a href="#maintenance-jakebolam" title="Maintenance">🚧</a> <a href="https://github.com/sabuhish/fastapi-mail/" title="Reviewed Pull Requests">👀</a></td>\n    <td align="center"><a href="https://github.com/imaskm"><img src="https://avatars.githubusercontent.com/u/20543833?v=3" width="100px;" alt=""/><br /><sub><b>Ashwani</b></sub></a><br /><a href="#maintenance-tbenning" title="Maintenance">🚧</a></td>\n    <td align="center"><a href="https://github.com/LLYX"><img src="https://avatars1.githubusercontent.com/u/10430633" width="100px;" alt=""/><br /><sub><b>Leon Xu</b></sub></a><br /><a href="#maintenance-tbenning" title="Maintenance">🚧</a></td>\n    <td align="center"><a href="https://github.com/gabrielponto"><img src="https://avatars.githubusercontent.com/u/7227328" width="100px;" alt=""/><br /><sub><b>Gabriel Oliveira</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a href="#maintenance-jakebolam" title="Maintenance">🚧</a></td>\n    <td align="center"><a href="https://github.com/maestro-1"><img src="https://avatars0.githubusercontent.com/u/40833254" width="100px;" alt=""/><br /><sub><b>Onothoja Marho</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a  href="#maintenance-jakebolam"  title="Maintenance">🚧</a> <a href="#tool-jfmengels" title="Tools">🔧</a></td>\n\n  </tr>\n <tr>\n    <td align="center"><a href="https://github.com/TheTimKiely"><img src="https://avatars1.githubusercontent.com/u/34795732" width="100px;" alt=""/><br /><sub><b>Tim Kiely</b></sub></a><br /><a href="#maintenance-tbenning" title="Maintenance">🚧</a></td>\n    <td align="center"><a href=https://github.com/DmitriySolodkiy"><img src="https://avatars1.githubusercontent.com/u/37667152" width="100px;" alt=""/><br/><sub><b>Dmitriy Solodkiy</b></sub></a><br /><a href="#maintenance-tbenning" title="Maintenance">🚧</a></td>\n    <td align="center"><a href="https://github.com/pboers1988"><img src="https://avatars1.githubusercontent.com/u/3235585" width="100px;" alt=""/><br /><sub><b>Peter Boers</b></sub></a><br /><a href="#maintenance-tbenning" title="Maintenance">🚧</a></td>\n    <td align="center"><a href="https://github.com/jdvalentine"><img src="https://avatars.githubusercontent.com/u/557514" width="100px;" alt=""/><br /><sub><b>James Valentine</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a  href="#maintenance-jakebolam"  title="Maintenance">🚧</a> <a href="#tool-jfmengels" title="Tools">🔧</a></td>\n    <td align="center"><a href="https://github.com/gogoku"><img src="https://avatars.githubusercontent.com/u/25707104" width="100px;" alt=""/><br /><sub><b>Gogoku</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a  href="#maintenance-jakebolam"  title="Maintenance">🚧</a> <a href="#tool-jfmengels" title="Tools">🔧</a></td>\n    <td align="center"><a href="https://github.com/kucera-lukas"><img src="https://avatars.githubusercontent.com/u/85391931" width="100px;" alt=""/><br /><sub><b>Kucera-Lukas</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a  href="#maintenance-jakebolam"  title="Maintenance">🚧</a> <a href="#tool-jfmengels" title="Tools">🔧</a></td>\n    <td align="center"><a href="https://github.com/LLYX"><img src="https://avatars.githubusercontent.com/u/10430633" width="100px;" alt=""/><br /><sub><b>LLYX</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a  href="#maintenance-jakebolam"  title="Maintenance">🚧</a> <a href="#tool-jfmengels" title="Tools">🔧</a></td></tr>\n  \n<tr>\n    <td align="center"><a href="https://github.com/floodpants"><img src="https://avatars.githubusercontent.com/u/37890036?" width="100px;" alt=""/><br /><sub><b>floodpants</b></sub></a><br /><a href="#maintenance-tbenning" title="Maintenance">🚧</a></td>\n    <td align="center"><a href="https://github.com/andredias"><img src="https://avatars.githubusercontent.com/u/902540" width="100px;" alt=""/><br /><sub><b>André Felipe Dias</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a href="https://github.com/sabuhish/fastapi-mail/" title="Reviewed Pull Requests">👀</a> <a href="#tool-jfmengels" title="Tools">🔧</a></td></b></sub></a><br /><a href="#maintenance-tbenning" title="Maintenance">🚧</a></td>\n    <td align="center"><a href="https://github.com/wjurkowlaniec"><img src="https://avatars.githubusercontent.com/u/1134323" width="100px;" alt=""/><br /><sub><b>Wojtek Jurkowlaniec</b></sub></a><br /><a href="https://github.com/sabuhish/fastapi-mail/" title="Documentation">📖</a> <a href="https://github.com/sabuhish/fastapi-mail/" title="Reviewed Pull Requests">👀</a> <a href="#tool-jfmengels" title="Tools">🔧</a></td></b></sub></a><br /><a href="#maintenance-tbenning" title="Maintenance">🚧</a></td>\n\n</tr>\n</table>\n\n\nThis project follows the [all-contributors](https://allcontributors.org) specification.\nContributions of any kind are welcome!\n\nBefore you start please read [CONTRIBUTING](https://github.com/sabuhish/fastapi-mail/blob/master/CONTRIBUTING.md)\n\n\n\n## LICENSE\n\n[MIT](LICENSE)\n',
    'author': 'Sabuhi Shukurov',
    'author_email': 'sabuhi.shukurov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sabuhish/fastapi-mail',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
