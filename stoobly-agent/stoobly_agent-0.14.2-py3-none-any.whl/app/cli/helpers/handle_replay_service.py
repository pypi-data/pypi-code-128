import json
import pdb

from typing import Callable

from stoobly_agent.app.cli.helpers.context import ReplayContext
from stoobly_agent.app.proxy.replay.body_parser_service import decode_response
from stoobly_agent.lib.logger import Logger, bcolors
from stoobly_agent.lib.utils import jmespath

DEFAULT_FORMAT = 'default'
JSON_FORMAT = 'json'

def print_request(context: ReplayContext, format_handler: Callable[[ReplayContext], None] = None):
  format_handler = format_handler or default_format_handler 
  format_handler(context)

def print_request_query(context: ReplayContext, query: str):
  response = context.response
  content = response.content
  content_type = response.headers.get('content-type')

  decoded_response = decode_response(content, content_type)
  if not isinstance(decoded_response, dict) and not isinstance(decoded_response, list):
    Logger.instance().error(
      f"{bcolors.FAIL}Could not query request, expected responsed to be of type {dict} or {list}, got {decoded_response.__class__} {bcolors.ENDC}"
    )
    print_request(context)
  else:
    print(jmespath.search(query, decoded_response))

def default_format_handler(context: ReplayContext, additional=''):
  response = context.response
  print(response.content.decode())

  seconds = context.end_time - context.start_time
  ms = round(seconds * 1000)
  print(f"Completed {response.status_code} in {ms}ms${additional}")

def json_format_handler(context: ReplayContext):
  response = context.response
  headers = dict(response.headers)
  content = response.content.decode()

  output = {'headers': headers, 'content': content}
  print(json.dumps(output))