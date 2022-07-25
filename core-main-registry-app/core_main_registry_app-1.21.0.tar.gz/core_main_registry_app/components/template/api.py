""" Template's registry api
"""

from core_main_app.commons import exceptions as exceptions
from core_main_app.components.template import api as template_api
from core_main_app.components.version_manager import api as version_manager_api
from core_main_registry_app.settings import REGISTRY_XSD_FILENAME


# NOTE: access control from main apis
def get_current_registry_template(request):
    """Get the current template used for the registry.

    Args:
        request:

    Returns:

    """
    try:
        template_version = (
            version_manager_api.get_active_global_version_manager_by_title(
                REGISTRY_XSD_FILENAME, request=request
            )
        )
        return template_api.get(template_version.current, request=request)
    except Exception as e:
        raise exceptions.ModelError(str(e))
