# Adafruit Ultimate GPS Featherwing with Timezone Offset

Quad Stack Demo (NRF52840 Sense, ESP32 Airlift Featherwing, 3.5" TFT Featherwing, Ultimate GPS Featherwing)

The Adafruit Ultimate GPS Featherwing includes a Real Time Clock with coincell battery backup

- Displays RTC localtime while connecting to GPS (will display incorrect time if RTC never previously set)
- GPS connects and receives UTC timestamp data
- GPS time updates RTC (only once on reboot)
- RTC permanently set with new synchronized time (even if USB power or VBAT power removed)
- Outputs RTC time with local GMT offset (customizable Timezone variable).

This particluar GPS module does not have timezone capability, it only reports time in UTC (0 GMT).

Currently not DST aware code. You must set timezone offset yourself. 

Will have DST aware timezone in the future which changes + or - 1 twice a year (work in progress)
