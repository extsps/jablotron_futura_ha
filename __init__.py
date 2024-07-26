import logging
from homeassistant.components.modbus import ModbusHub
from homeassistant.helpers import discovery

_LOGGER = logging.getLogger(__name__)

DOMAIN = "jablotron_futura"

def setup(hass, config):
    hub = ModbusHub(
        name="Jablotron Futura",
        host="DEVICE_IP",
        port=502,
        timeout=3
    )
    hass.data[DOMAIN] = hub

    discovery.load_platform(hass, "sensor", DOMAIN, {}, config)
    discovery.load_platform(hass, "switch", DOMAIN, {}, config)

    return True
