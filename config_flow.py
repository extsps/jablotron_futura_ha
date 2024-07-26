from homeassistant import config_entries
import voluptuous as vol
from homeassistant.core import callback
from .const import DOMAIN  # You should have a const.py file with DOMAIN defined

# Define the schema for the configuration step
DATA_SCHEMA = vol.Schema({
    vol.Required("host"): str,
})

class JablotronFuturaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Jablotron Futura."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    def __init__(self):
        """Initialize the config flow."""
        self._errors = {}

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        self._errors = {}
        if user_input is not None:
            host = user_input.get("host")

            # Perform any checks or validations here
            if self._is_valid_host(host):
                return self.async_create_entry(title="Jablotron Futura", data=user_input)
            else:
                self._errors["base"] = "invalid_host"

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=self._errors
        )

    def _is_valid_host(self, host):
        """Validate the IP address or hostname."""
        # Basic check if the host is a valid IP address or hostname
        return True  # Implement your validation logic here

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return JablotronFuturaOptionsFlow(config_entry)

class JablotronFuturaOptionsFlow(config_entries.OptionsFlow):
    """Handle Jablotron Futura options."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return await self.async_step_user(user_input)

    async def async_step_user(self, user_input=None):
        """Handle the options step."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options_schema = vol.Schema({
            vol.Required("host", default=self.config_entry.options.get("host", "")): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=options_schema
        )
