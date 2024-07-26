from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    hub = hass.data["jablotron_futura"]
    async_add_entities([
        JablotronFuturaSensor(hub, "Temperature", "temp_indoor", TEMP_CELSIUS)
    ])

class JablotronFuturaSensor(SensorEntity):
    def __init__(self, hub, name, register, unit):
        self._hub = hub
        self._name = name
        self._register = register
        self._unit = unit
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    async def async_update(self):
        result = await self._hub.read_register(self._register)
        self._state = result
