from homeassistant import config_entries
import voluptuous as vol
from homeassistant.const import CONF_IP_ADDRESS, CONF_PORT
from . import DOMAIN, DEFAULT_PORT

class JablotronFuturaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Jablotron Futura config flow."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Jablotron Futura", data=user_input)

        data_schema = vol.Schema(
            {
                vol.Required(CONF_IP_ADDRESS): str,
                vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
            }
        )
        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)
