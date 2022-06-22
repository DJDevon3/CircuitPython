# Project Description:
Quick demo for those who have a triple stack with TFT featherwing and Airlift featherwing (multiple SPI bus devices).

# Hardware:
- Adafruit NRF52840 Bluefruit Sense Board https://www.adafruit.com/product/4516
- Adafruit 3.5" TFT Featherwing https://www.adafruit.com/product/3651
- Adafruit Airlift ESP32 Featherwing https://www.adafruit.com/product/4264

# Circuit Python 7.3.x Libraries:
- adafruit_esp32spi (required for airlift featherwing)
- adafruit_hx8357 (required for 3.5" TFT featherwing)

[Get the adafruit-circuitpython-bundle-7.x here](https://circuitpython.org/libraries)
Only put the library folders you actively need in CIRCUITPY/lib

# AdafruitIO:
- AdafruitIO account username & key (edit secrets.py file)


# Serial and TFT Output Example:

This demo code will connect to your AdafruitIO feed named "test" and post an integer value starting at 0 then counting up with each sequential post. 
It's a quick demo for how to connect to AdafruitIO and post some data.
```
Connecting to WiFi...
Connected!

Value: 89.6
Posting Value...{'created_at': '2022-06-22T06:32:15Z', 'id': 'obfuscated', 'expiration': '2022-07-22T06:32:15Z', 'created_epoch': 1655879535, 'feed_id': obfuscated, 'value': '89.6', 'feed_key': 'sense-temp'}
```
# Warning about SPI bus lock ups
The SPI bus can get locked sometimes when interacting with multiple feather boards through SPI.
If your SPI bus is locked it will throw the error `ValueError: SCK in use` no matter what software pin you attempt to choose.
When the SPI bus gets locked it can persist through code changes and soft-reboots!
A simple board reset (physical button reset) after a code change involving SPI bus can solve that. Reset the board and run your code again. 

# Default Sleep Timer
For the purpose of testing it's set to 10 seconds. `time.sleep(10)` Set to 3600 for hourly updates when you finalize your code.
AdafruitIO free accounts have a 1000 update daily limit which you can easily exceed by posting every 10 seconds. The most you can safely post 1 value within a 24 hour period without going over the 1000 limit is once every 1.5 minutes (90 seconds).
