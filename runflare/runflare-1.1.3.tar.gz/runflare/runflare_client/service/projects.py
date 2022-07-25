from runflare.runflare_client.requester import Requester
from runflare.settings import PROJECT_LIST_URL,ITEM_LIST_URL
from colorama import Fore, Style
from halo import Halo


spinner = Halo(text=Style.BRIGHT + "Getting Projects List...", color="magenta")
def get_projects(email=None,password=None):
    spinner.start()
    request = Requester("GET", PROJECT_LIST_URL,spinner=spinner,extra={"email" : email,"password" : password})
    spinner.stop()
    return request.get_response


@Halo(text=Style.BRIGHT + "Getting Item List...", color="magenta")
def get_project_items(project_id):
    request = Requester("GET", ITEM_LIST_URL.format(project_id))
    return request.get_response
