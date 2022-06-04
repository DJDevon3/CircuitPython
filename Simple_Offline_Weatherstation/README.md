A project that began on Arduino and eventually updated to Circuit Python 7.x

# Hardware Required:
- Adafruit NRF52840 Bluefruit Sense Board (running Circuit Python)
- Adafruit 3.5" TFT Featherwing

The BMP images must be 8-bit indexed formatted. You lose a lot of color compared to Arduino but still does the job. I've included 2 BMP's in the images folder as examples. If you attempt to use 16-bit or higher BMP's you'll get an error message on the TFT about true color BMP's not being supported. This is a limitation of the graphics library as true color BMP's work just fine in my Arduino version on the same hardware.

![](https://raw.githubusercontent.com/DJDevon3/CircuitPython/main/Simple_Offline_Weatherstation/TFT_Output_Example.jpg)
