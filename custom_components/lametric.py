"""
Support for Lametric notification service.
For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/notify.lametric/
"""
import logging

import voluptuous as vol
import requests
import base64

from homeassistant.components.notify import (
    ATTR_MESSAGE, PLATFORM_SCHEMA,
    BaseNotificationService)
from homeassistant.const import CONF_API_KEY, CONF_HOST
import homeassistant.helpers.config_validation as cv

NOTE_URL = 'http://' + CONF_HOST + ':8080/api/v2/device/notifications'

encoded_api = base64.b64encode(CONF_API_KEY, altchars=None)

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Basic' + encoded_api
    'Cache-Control': 'no-cache',
}

data = '{"priority": "warning", "icon_type": "none", "model": {"frames": [{"icon": "i3579", "text":' + ATTR_MESSAGE + '}], "sound": {"category": "notifications", "id": "positive4"}}}'

requests.post(NOTE_URL, headers=headers, data=data)
