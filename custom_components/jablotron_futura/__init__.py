import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from homeassistant.const import CONF_IP_ADDRESS, CONF_PORT
from .modbus import ModbusHub

DOMAIN = "jablotron_futura"
DEFAULT_PORT = 502
_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Jablotron Futura integration from YAML configuration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Jablotron Futura from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    modbus_hub = ModbusHub(hass, entry.data[CONF_IP_ADDRESS], entry.data[CONF_PORT])
    hass.data[DOMAIN][entry.entry_id] = modbus_hub
    hass.config_entries.async_setup_platforms(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Jablotron Futura config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["sensor"])
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
