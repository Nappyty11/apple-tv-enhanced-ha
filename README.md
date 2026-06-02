# Apple TV Enhanced for Home Assistant

Enhanced Apple TV controls, app launching, HomeKit support, and custom launch targets for Home Assistant.

---

## Features

- Launch Apple TV apps directly from Home Assistant
- Home Screen shortcut
- Fast Sleep support
- Custom app launch targets
- Custom deep links
- HomeKit compatible
- HACS installable

---

## Requirements

Before installing Apple TV Enhanced, your Apple TV must already be working in Home Assistant through the native Apple TV integration.

### Add Apple TV to Home Assistant

1. Open Home Assistant
2. Go to **Settings → Devices & Services**
3. Click **Add Integration**
4. Search for **Apple TV**
5. Complete pairing
6. Verify your Apple TV appears and functions correctly

---

## Installation

### Install Through HACS

1. Open **HACS**
2. Click the **three-dot menu**
3. Select **Custom Repositories**
4. Add this repository:

```text
https://github.com/Nappyty11/apple-tv-enhanced-ha
```

Category:

```text
Integration
```

5. Click **Add**
6. Install **Apple TV Enhanced**
7. Restart Home Assistant

---

## Setup

1. Go to **Settings → Devices & Services**
2. Click **Add Integration**
3. Search for:

```text
Apple TV Enhanced
```

4. Select your Apple TV media player
5. Optional: add a custom source name and target
6. Complete setup

---

## Custom Sources

Apple TV Enhanced supports one custom source in the setup flow.

This can be used for:

- Custom app bundle IDs
- Deep links
- Show links
- Movie links
- App shortcuts

### Custom App Example

Custom Source Name:

```text
My App
```

Custom Source Target:

```text
com.example.app
```

### Deep Link Example

Custom Source Name:

```text
Severance
```

Custom Source Target:

```text
https://tv.apple.com/show/severance/umc.cmc.1srk2goyh2q2zdxcx605w8vtx
```

After setup, the custom source will appear in the Apple TV Enhanced source list.

---

## Home Screen

Apple TV Enhanced includes a dedicated **Home Screen** source.

Selecting **Home Screen** sends the Apple TV Home command and returns directly to the Apple TV Home Screen.

No additional configuration required.

---

## HomeKit Support

Apple TV Enhanced can be exposed to Apple Home through Home Assistant HomeKit Bridge.

### Important

Power controls currently work more reliably through Apple Home than through Home Assistant dashboards.

This is a limitation of the current Apple TV / Home Assistant ecosystem and not Apple TV Enhanced itself.

For best results:

- Use Apple TV Enhanced for app launching
- Use Apple TV Enhanced for Home Screen navigation
- Use Apple TV Enhanced for custom sources
- Use Apple Home for power controls when available

---

## Included Apps

### Apple

- Apple TV
- Apple Music
- Apple Podcasts
- Apple Photos
- Apple Settings
- Apple App Store

### Streaming

- Netflix
- YouTube
- Hulu
- Disney+
- Max
- Amazon Prime Video
- Peacock
- Twitch
- Crunchyroll

### Other

- Calendar by Dashbd

---

## Verified Bundle IDs

| App | Bundle ID |
|---|---|
| Apple TV | `com.apple.TVWatchList` |
| Apple Music | `com.apple.TVMusic` |
| Apple Podcasts | `com.apple.Podcasts` |
| Apple Photos | `com.apple.TVPhotos` |
| Apple Settings | `com.apple.TVSettings` |
| Apple App Store | `com.apple.TVAppStore` |
| Netflix | `com.netflix.Netflix` |
| YouTube | `com.google.ios.youtube` |
| Hulu | `com.hulu.plus` |
| Disney+ | `com.disney.disneyplus` |
| Max | `com.wbd.stream` |
| Amazon Prime Video | `com.amazon.aiv.AIVApp` |
| Peacock | `com.peacocktv.peacock` |
| Twitch | `tv.twitch` |
| Crunchyroll | `com.crunchyroll.iphone` |
| Calendar by Dashbd | `com.benoitzohar.Calendar` |

---

## Known Issues

### Power Controls

Apple TV power commands can behave differently depending on:

- tvOS version
- Home Assistant version
- Apple TV model
- Apple TV integration behavior

Current testing shows power controls work most consistently through Apple Home when exposed through HomeKit Bridge.

### App Availability

Apps only launch if they are installed on the Apple TV.

If an app is not installed, selecting it may do nothing.

### Native Apple TV App List

The native Apple TV integration may fail to retrieve the installed app list on some systems.

Apple TV Enhanced uses a verified bundle ID database instead of relying only on Home Assistant's app discovery.

---

## Releases

### v0.0.1

Initial release.

- Apple TV Enhanced media player
- Built-in app source list
- App launcher support
- Fast Sleep support
- HomeKit support

### v0.0.2

Custom source foundation.

- Custom source groundwork
- Deep link groundwork
- Improved app source handling

### v0.0.3

Home Screen and cleaner custom source setup.

- Home Screen source
- Custom Source Name field
- Custom Source Target field
- Improved setup flow
- HACS custom repository support confirmed

---

## Roadmap

### v0.0.4

Planned source management update.

- Editable custom sources
- Add / Edit / Delete sources
- Multiple custom sources
- Deep link management
- Favorite shows
- Favorite movies

### Future

- Expanded app database
- Remote control actions
- Additional Apple TV commands
- Community verified app list
- Better Home Assistant dashboard power handling
- More HomeKit behavior testing

---

## Support

Feature requests and bug reports:

```text
https://github.com/Nappyty11/apple-tv-enhanced-ha/issues
```

---

## License

MIT License
