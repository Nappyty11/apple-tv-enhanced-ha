# Apple TV Enhanced for Home Assistant

A community project focused on improving Apple TV controls, app launching, and HomeKit integration in Home Assistant.

## Verified Bundle IDs

| App | Bundle ID |
|------|------|
| Netflix | com.netflix.Netflix |
| YouTube | com.google.ios.youtube |
| Hulu | com.hulu.plus |
| Disney Plus | com.disney.disneyplus |
| HBO Max | com.wbd.stream |
| Amazon Prime | com.amazon.aiv.AIVApp |
| Peacock | com.peacocktv.peacock |
| Twitch | tv.twitch |
| Crunchyroll | com.crunchyroll.iphone |
| Calendar by Dashbd | com.benoitzohar.Calendar |

## Known Issues

- Apple TV app_list command fails on tvOS 26.5
- Home Assistant cannot always automatically discover launchable applications
- Some bundle IDs must be manually tested and verified

## Goals

- Build a verified Apple TV bundle ID database
- Create a Home Assistant Blueprint
- Create a HACS integration
- Improve HomeKit compatibility
- Simplify Apple TV app launching
