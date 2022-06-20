import time
import board
import busio
import displayio
from digitalio import DigitalInOut
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
from adafruit_hx8357 import HX8357
displayio.release_displays()

# This sketch should also work for the 2.5" TFT, just change the size.
DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 320

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("Secrets File Import Error")
    raise

# Initialize SPI bus
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# Initilize ESP32 Airlift on SPI bus
esp32_cs = DigitalInOut(board.D13)
esp32_ready = DigitalInOut(board.D11)
esp32_reset = DigitalInOut(board.D12)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
status_light = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)
wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)

# Initialize TFT Display on SPI bus
tft_cs = board.D9
tft_dc = board.D10
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = HX8357(display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

counter = 0
print("Airlift Featherwing ESP32 SPI AdafruitIO Test\n")

while True:
    try:
        print("Posting data...", end="")
        data = counter
        feed = "test"
        payload = {"value": data}
        response = wifi.post(
            "https://io.adafruit.com/api/v2/"
            + secrets["aio_username"]
            + "/feeds/"
            + feed
            + "/data",
            json=payload,
            headers={"X-AIO-KEY": secrets["aio_key"]},
        )
        print(response.json())
        response.close()
        print("Count: {}".format(counter) + "\n")
        counter = counter + 1
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        continue
    response = None
    time.sleep(10)
