import time
import board
import busio
import displayio
from digitalio import DigitalInOut
import adafruit_bmp280
import adafruit_sht31d
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
from adafruit_hx8357 import HX8357
displayio.release_displays()

# This sketch should also work for the 2.5" TFT, just change the size.
DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 320

i2c = board.I2C()
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
sht31d = adafruit_sht31d.SHT31D(i2c)
bmp280.sea_level_pressure = bmp280.pressure

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

# Connect to WiFi
print("Connecting to WiFi...")
wifi.connect()
print("Connected!\n")

# Value to be posted to AdafruitIO (NRF52840 on-board temp sensor)
update_val = "{:.1f}".format(bmp280.temperature*1.8+32)

# Your feed key might be different from the feed name (no underscore allowed).
# It's not your IO account key or feed name. It's the individual key for each feed.
# For example, create a feed "temp_test" at AdafruitIO it sets the key "temp-test".
feed_key = "sense-temp"
    
while True:
    try:
        print("Value: %.1f" % float(update_val))
        print("Posting Value...", end="")
        payload = {"value": (update_val)}
        response = wifi.post(
            "https://io.adafruit.com/api/v2/"
            + secrets["aio_username"]
            + "/feeds/"
            + feed_key
            + "/data",
            json=payload,
            headers={"X-AIO-KEY": secrets["aio_key"]},
        )
        print(response.json())
        response.close()
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        continue
    response = None
    time.sleep(3600)