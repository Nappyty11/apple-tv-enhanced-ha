# Apple TV Enhanced

Launch Apple TV apps, custom apps, and deep links directly from Home Assistant.

## Features

- Launch Apple TV apps from a source selector
- Home Screen shortcut
- Fast Sleep support
- Custom app entries
- Custom deep links
- HomeKit compatible
- HACS installable

## Requirements

### 1. Add Apple TV to Home Assistant

Before installing Apple TV Enhanced, your Apple TV must already be configured through Home Assistant's native Apple TV integration.

Home Assistant:

Settings → Devices & Services → Add Integration → Apple TV

Verify your Apple TV appears and functions before continuing.

---

### 2. Install Apple TV Enhanced

#### HACS Installation

1. Open HACS
2. Click the three dots menu
3. Custom Repositories
4. Add:

text https://github.com/Nappyty11/apple-tv-enhanced-ha 

Category:

text Integration 

5. Install Apple TV Enhanced
6. Restart Home Assistant

---

### 3. Add Integration

Settings → Devices & Services → Add Integration

Search:

text Apple TV Enhanced 

Select your Apple TV from the list.

---

## HomeKit Support

Apple TV Enhanced can be exposed to Apple Home through Home Assistant HomeKit Bridge.

### Important

Power controls currently work more reliably through Apple Home than through Home Assistant dashboards.

This is a limitation of the current Apple TV/Home Assistant ecosystem and not Apple TV Enhanced itself.

For the best experience:

- Use Apple TV Enhanced for launching apps, Home Screen navigation, and custom sources.
- Use Apple Home for power controls when available.

---

## Custom Sources

Create custom launcher entries without editing code.

Example:

Name:

text Severance 

Target:

text https://tv.apple.com/show/severance/... 

or

Name:

text My App 

Target:

text com.example.app 

---

## Verified Apps

- Apple TV
- Apple Music
- Apple Podcasts
- Apple Photos
- Apple Settings
- Apple App Store
- Netflix
- YouTube
- Hulu
- Disney+
- Max
- Amazon Prime Video
- Peacock
- Twitch
- Crunchyroll
- Calendar by Dashbd

---

## Roadmap

### v0.0.4

- Editable custom sources
- Source management without reinstalling integration

### v0.0.5

- Deep link support
- Content shortcuts
- Show and movie launchers

### Future

- Volume controls
- Remote controls
- Additional Apple TV commands
- Expanded app database

---

## Support

Issues and feature requests:

https://github.com/Nappyty11/apple-tv-enhanced-ha/issues
