# Adafruit GPS with Real Time Clock & Timezone Offset

![](https://raw.githubusercontent.com/DJDevon3/CircuitPython/main/Ultimate%20GPS%20Featherwing/screenshot_connecting.bmp)

UTC Time = 5:39. The -5 GMT Timezone offset correctly displays localtime as 00:39. Changes date appropriately.

If the microcontroller board is battery powered the GPS and RTC ensure proper time keeping during a power outage.

![](https://raw.githubusercontent.com/DJDevon3/CircuitPython/main/Ultimate%20GPS%20Featherwing/screenshot_gps.bmp)

Quad Stack Demo (NRF52840 Sense, ESP32 Airlift Featherwing, 3.5" TFT Featherwing, Ultimate GPS Featherwing)

The Adafruit Ultimate GPS Featherwing includes a Real Time Clock with coincell battery backup

- Displays RTC localtime while connecting to GPS (will display incorrect time if RTC never previously set)
- GPS connects and receives UTC timestamp data
- GPS time updates RTC only once per reboot. (time drift will occur eventually, reboot to resync time)
- RTC permanently set with new synchronized time (even if USB power or VBAT power removed)
- Outputs RTC time with local GMT offset (customizable Timezone variable).

This particluar GPS module does not have timezone capability, it only reports time in UTC (0 GMT).

Currently not DST aware code. You must set timezone offset yourself. 

Will have DST aware timezone in the future which changes + or - 1 twice a year (work in progress)

Thanks to [Neradoc](https://github.com/Neradoc) for coding the Timezone offset correction for Adafruit GPS.
