"""Config flow for Apple TV Enhanced."""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers import entity_registry as er

DOMAIN = "apple_tv_enhanced"


class AppleTVEnhancedConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle Apple TV Enhanced config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle setup."""

        entity_registry = er.async_get(self.hass)

        apple_tv_media_players = []

        for entity in entity_registry.entities.values():
            if not entity.entity_id.startswith("media_player."):
                continue
            if entity.platform != "apple_tv":
                continue

            state = self.hass.states.get(entity.entity_id)
            if state is None:
                continue

            friendly_name = state.attributes.get("friendly_name", "").lower()
            model_name = state.attributes.get("model_name", "").lower()
            device_class = state.attributes.get("device_class", "").lower()

            if (
                "apple tv" in friendly_name
                or "apple tv" in model_name
                or device_class == "tv"
            ):
                apple_tv_media_players.append(entity.entity_id)

        if user_input is not None:
            selected_entity = user_input["media_player_entity"]
            registry_entry = entity_registry.async_get(selected_entity)

            user_input["device_id"] = registry_entry.device_id

            return self.async_create_entry(
                title="Apple TV Enhanced",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("media_player_entity"): vol.In(
                        apple_tv_media_players
                    ),
                    vol.Optional("custom_source_name", default=""): str,
                    vol.Optional("custom_source_target", default=""): str,
                }
            ),
        )

