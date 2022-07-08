# Adafruit Ultimate GPS Featherwing with Timezone Offset

Quad Stack Demo (NRF52840 Sense, ESP32 Airlift Featherwing, 3.5" TFT Featherwing, Ultimate GPS Featherwing)

The Adafruit Ultimate GPS Featherwing includes a Real Time Clock with coincell battery backup

- Displays RTC localtime while connecting to GPS (will display incorrect time if RTC never previously set)
- GPS connects and pulls UTC timestamp
- GPS time updates RTC (only once on reboot)
- RTC now permanently set with that time (even if USB power or VBAT power removed)
- Outputs renewed/reinitialized RTC time with GMT offset (customizable Timezone variable).

Currently not DST aware code. You'll need to set timezone with DST offset.

Will have DST aware timezone in the future (work in progress)
