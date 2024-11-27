from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS, PERCENTAGE, POWER_WATT, VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR
from . import DOMAIN

SENSOR_TYPES = {
    "ambient_temperature": ["Ambient Temperature", TEMP_CELSIUS, 30],
    "fresh_air_temperature": ["Fresh Air Temperature", TEMP_CELSIUS, 31],
    "indoor_air_temperature": ["Indoor Air Temperature", TEMP_CELSIUS, 32],
    "waste_air_temperature": ["Waste Air Temperature", TEMP_CELSIUS, 33],
    "ambient_humidity": ["Ambient Humidity", PERCENTAGE, 34],
    "fresh_air_humidity": ["Fresh Air Humidity", PERCENTAGE, 35],
    "indoor_humidity": ["Indoor Humidity", PERCENTAGE, 36],
    "waste_air_humidity": ["Waste Air Humidity", PERCENTAGE, 37],
    "filter_wear_level": ["Filter Wear Level", PERCENTAGE, 40],
    "power_consumption": ["Power Consumption", POWER_WATT, 41],
    "heat_recovering": ["Heat Recovering", POWER_WATT, 42],
    "heating_power": ["Heating Power", POWER_WATT, 43],
    "air_flow": ["Air Flow", VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR, 44],
}

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Jablotron Futura sensors."""
    modbus_hub = hass.data[DOMAIN][config_entry.entry_id]
    entities = []
    for sensor_type, sensor_info in SENSOR_TYPES.items():
        name, unit, register = sensor_info
        entities.append(JablotronFuturaSensor(modbus_hub, name, register, unit))
    async_add_entities(entities, update_before_add=True)

class JablotronFuturaSensor(SensorEntity):
    """Representation of a Jablotron Futura sensor."""

    def __init__(self, modbus_hub, name, register, unit_of_measurement):
        """Initialize the sensor."""
        self._modbus_hub = modbus_hub
        self._name = name
        self._register = register
        self._unit_of_measurement = unit_of_measurement
        self._state = None
        self._available = True

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def available(self):
        """Return True if the sensor is available."""
        return self._available

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    async def async_update(self):
        """Update the state of the sensor."""
        try:
            result = await self._modbus_hub.read_input_registers(self._register, 1)
            if result is None:
                self._available = False
                return
            self._state = result.registers[0]
            self._available = True
        except Exception as ex:
            self._available = False
            _LOGGER.error(f"Error reading modbus data
::contentReference[oaicite:0]{index=0}
