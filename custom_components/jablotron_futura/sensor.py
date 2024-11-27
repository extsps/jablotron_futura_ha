from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS
from . import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Jablotron Futura sensors from config entry."""
    modbus_hub = hass.data[DOMAIN]
    async_add_entities(
        [
            JablotronFuturaSensor(modbus_hub, "Ambient Temperature", 30, TEMP_CELSIUS),
            JablotronFuturaSensor(modbus_hub, "Fresh Air Temperature", 31, TEMP_CELSIUS),
            # Add more sensors as required
        ],
        update_before_add=True,
    )
