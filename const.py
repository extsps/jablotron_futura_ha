# Define the domain for your integration
DOMAIN = "jablotron_futura"

# Configuration keys
CONF_HOST = "host"

# Default values (if any)
DEFAULT_HOST = "192.168.1.100"  # Change this to a reasonable default or leave it empty

# Other constants (if needed)
# For example, if you have predefined modes or state values, define them here
VENTILATION_MODES = {
    0: "Off",
    1: "Manual Low",
    2: "Manual Medium",
    3: "Manual High",
    4: "Automatic",
    5: "Boost"
}

# Example Modbus register addresses
MODBUS_REGISTER_TEMP_INDOOR = 32  # Register for indoor temperature
MODBUS_REGISTER_TEMP_OUTDOOR = 33  # Register for outdoor temperature
MODBUS_REGISTER_HUMIDITY = 36  # Register for indoor humidity
# Add more registers as needed

# Error messages or constants for error handling
ERROR_INVALID_HOST = "Invalid host"
