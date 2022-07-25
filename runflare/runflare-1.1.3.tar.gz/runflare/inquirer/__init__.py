from __future__ import print_function

__version__ = '2.7.0'


from runflare.inquirer.prompt import prompt
from runflare.inquirer.questions import Text, Editor, Password, Confirm, List, Checkbox, \
    Path, load_from_dict, load_from_json, load_from_list
from runflare.inquirer.shortcuts import text, editor, password, confirm, list_input, \
    checkbox

__all__ = ['prompt', 'Text', 'Editor', 'Password', 'Confirm', 'List',
           'Checkbox', 'Path', 'load_from_list', 'load_from_dict',
           'load_from_json', 'text', 'editor', 'password', 'confirm',
           'list_input', 'checkbox']
# except ImportError as e:
#     print("An error was found, but returning just with the version: %s" % e)
