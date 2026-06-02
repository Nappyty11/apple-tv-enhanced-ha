"""Media player platform for Apple TV Enhanced."""

from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.components.media_player.const import (
    MediaPlayerEntityFeature,
    MediaPlayerState,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .apps import APP_IDS
from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Apple TV Enhanced media player."""
    async_add_entities([AppleTVEnhancedMediaPlayer(hass, entry)])


class AppleTVEnhancedMediaPlayer(MediaPlayerEntity):
    """Enhanced Apple TV media player."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize Apple TV Enhanced media player."""
        self.hass = hass
        self.entry = entry
        self._media_player_entity = entry.data["media_player_entity"]

        self._attr_name = "Apple TV Enhanced"
        self._attr_unique_id = f"{entry.entry_id}_media_player"
        self._attr_device_class = "tv"
        self._attr_supported_features = (
            MediaPlayerEntityFeature.TURN_ON
            | MediaPlayerEntityFeature.TURN_OFF
            | MediaPlayerEntityFeature.SELECT_SOURCE
            | MediaPlayerEntityFeature.PLAY
            | MediaPlayerEntityFeature.PAUSE
        )
        self._attr_source_list = list(APP_IDS.keys())
        self._attr_source = None

        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "name": "Apple TV Enhanced",
            "manufacturer": "Nappyty11",
            "model": "Enhanced Apple TV Controller",
            "sw_version": "0.0.1",
        }

    @property
    def state(self):
        """Return Apple TV state."""
        state = self.hass.states.get(self._media_player_entity)

        if state is None:
            return MediaPlayerState.OFF

        if state.state in ["off", "unavailable", "unknown"]:
            return MediaPlayerState.OFF

        return MediaPlayerState.IDLE

    @property
    def source(self):
        """Return selected source."""
        return self._attr_source

    @property
    def source_list(self):
        """Return source list."""
        return self._attr_source_list

    async def async_turn_on(self) -> None:
        """Turn Apple TV on."""
        await self.hass.services.async_call(
            "media_player",
            "turn_on",
            {"entity_id": self._media_player_entity},
            blocking=True,
        )
        self.async_write_ha_state()

    async def async_turn_off(self) -> None:
        """Turn Apple TV off."""
        await self.hass.services.async_call(
            "media_player",
            "turn_off",
            {"entity_id": self._media_player_entity},
            blocking=True,
        )
        self.async_write_ha_state()

    async def async_select_source(self, source: str) -> None:
        """Launch selected app."""
        if source not in APP_IDS:
            return

        self._attr_source = source

        await self.hass.services.async_call(
            "media_player",
            "play_media",
            {
                "entity_id": self._media_player_entity,
                "media_content_id": APP_IDS[source],
                "media_content_type": "app",
            },
            blocking=True,
        )

        self.async_write_ha_state()

    async def async_media_play(self) -> None:
        """Play media."""
        await self.hass.services.async_call(
            "media_player",
            "media_play",
            {"entity_id": self._media_player_entity},
            blocking=True,
        )

    async def async_media_pause(self) -> None:
        """Pause media."""
        await self.hass.services.async_call(
            "media_player",
            "media_pause",
            {"entity_id": self._media_player_entity},
            blocking=True,
        )
