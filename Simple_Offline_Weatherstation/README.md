A project that began on Arduino and eventually updated to Circuit Python 7.x

# Hardware Required:
- Adafruit NRF52840 Bluefruit Sense Board (running Circuit Python)
- Adafruit 3.5" TFT Featherwing

The BMP images must be 8-bit indexed formatted. You lose a lot of color compared to Arduino but still does the job. I've included 2 BMP's in the images folder as examples. If you attempt to use 16-bit or higher BMP's you'll get an error message on the TFT about true color BMP's not being supported. This is a limitation of the circuit python graphics library as true color BMP's work fine in my Arduino version on the same hardware. 

You can choose to use the default TERMINALIO font instead of the bitmap fonts for much faster loading time (first display initialization). TERMINALIO doesn't look as nice but will "boot up" much faster. For a weatherstation that only updates every 60 seconds the "boot up" taking 20 seconds more is an acceptable sacrifice for better font aesthetics.

Circuit Python is more resource intensive than Arduino. If your project becomes too big (loading too large of an image) you can more easily run out of memory. 

With that said, while running only 1 8-bit BMP background image there's still plenty of overhead for larger sketches on the Bluefruit Sense. What really chews up the storage vs Arduino code is the amount of circuit python libraries for sketches. I've been running this in my garage for the past 2 years and it works wonderfully. The pressure sensor in particular is an extremely precise sensor and valuable data point to anyone living in an area of the world with regular large storms.

![](https://raw.githubusercontent.com/DJDevon3/CircuitPython/main/Simple_Offline_Weatherstation/TFT_Output_Example2.jpg)
