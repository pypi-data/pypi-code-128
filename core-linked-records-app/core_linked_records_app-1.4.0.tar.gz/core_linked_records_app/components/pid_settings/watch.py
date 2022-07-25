""" Initialization function for PID Settings
"""
import logging

from core_linked_records_app import settings
from core_linked_records_app.components.pid_settings import api as pid_settings_api
from core_linked_records_app.components.pid_settings.models import PidSettings
from core_main_app.commons.exceptions import CoreError

logger = logging.getLogger(__name__)


def init():
    try:
        if not PidSettings.get():
            pid_settings = PidSettings(auto_set_pid=settings.AUTO_SET_PID)
            pid_settings_api.upsert(pid_settings)
    except Exception as exc:
        error_message = "An unexpected error occurred while initializing PidSettings"

        logger.error(f"{error_message}: {str(exc)}")
        raise CoreError(f"{error_message}.")
