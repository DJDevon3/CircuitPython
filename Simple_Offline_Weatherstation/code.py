# SPDX-FileCopyrightText: 2020 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
#
"""DJDevon3 Simple Offline Weatherstation"""
import time
import board
import adafruit_bmp280
import adafruit_sht31d
import displayio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_hx8357 import HX8357
from analogio import AnalogIn

# This sketch should also work for the 2.5" TFT, just change the size.
DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 320

# Initialize TFT Display
displayio.release_displays()
i2c = board.I2C()
spi = board.SPI()
tft_cs = board.D9
tft_dc = board.D10
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = HX8357(display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

vbat_voltage = AnalogIn(board.VOLTAGE_MONITOR)
def get_voltage(pin):
    return (pin.value * 3.3) / 65536 * 2
vbat = get_voltage(vbat_voltage)

bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
sht31d = adafruit_sht31d.SHT31D(i2c)

# BMP280 altitude sensor changes with barometric pressure!
# I set sea level pressure to sensor pressure because I'm always at sea level.
# Set manually if it doesn't work well for your elevation.
# bmp280.sea_level_pressure = 1010.80
bmp280.sea_level_pressure = bmp280.pressure

# Some quick colors. Must be HEX values. You can add custom colors.
text_black = (0x000000)
text_blue = (0x0000FF)
text_cyan = (0x00FFFF)
text_green = (0x00FF00)
text_magenta = (0xFF00FF)
text_orange = (0xFFA500)
text_red = (0xFF0000)
text_white = (0xFFFFFF)
text_yellow = (0xFFFF00)

# Fonts are optional
small_font = bitmap_font.load_font("/fonts/Arial-12.bdf")
medium_font = bitmap_font.load_font("/fonts/Arial-16.bdf")
large_font = bitmap_font.load_font("/fonts/Arial-Bold-24.bdf")

# Individual customizable position labels
# https://learn.adafruit.com/circuitpython-display-support-using-displayio/text
hello_label = label.Label(small_font)
# Anchor point bottom center of text
hello_label.anchor_point = (0.5, 1.0)
# Display width divided in half for center of display (x,y)
hello_label.anchored_position = (DISPLAY_WIDTH/2, 15)
hello_label.scale = (1)
hello_label.color = text_white

temp_label = label.Label(medium_font)
temp_label.anchor_point = (1.0, 0.0)
temp_label.anchored_position = (475, 80)
temp_label.scale = (2)
temp_label.color = text_orange

temp_data_label = label.Label(large_font)
temp_data_label.anchor_point = (0.5, 1.0)
temp_data_label.anchored_position = (DISPLAY_WIDTH/2, 200)
temp_data_label.scale = (5)
temp_data_label.color = text_orange

humidity_label = label.Label(small_font)
# Anchor point bottom left of text
humidity_label.anchor_point = (0.0, 1.0)
humidity_label.anchored_position = (5, DISPLAY_HEIGHT)
humidity_label.scale = (1)
humidity_label.color = text_white

humidity_data_label = label.Label(medium_font)
humidity_data_label.anchor_point = (0.0, 1.0)
humidity_data_label.anchored_position = (5, DISPLAY_HEIGHT-25)
humidity_data_label.scale = (1)
humidity_data_label.color = text_white

barometric_label = label.Label(small_font)
# Anchor point bottom center of text
barometric_label.anchor_point = (0.5, 1.0)
barometric_label.anchored_position = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT)
barometric_label.scale = (1)
barometric_label.color = text_white

barometric_data_label = label.Label(medium_font)
barometric_data_label.anchor_point = (0.5, 1.0)
barometric_data_label.anchored_position = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT-25)
barometric_data_label.scale = (1)
barometric_data_label.color = text_white

altitude_label = label.Label(small_font)
# Anchor point bottom right of text
altitude_label.anchor_point = (1.0, 1.0)
altitude_label.anchored_position = (470, DISPLAY_HEIGHT)
altitude_label.scale = (1)
altitude_label.color = text_white

altitude_data_label = label.Label(medium_font)
altitude_data_label.anchor_point = (1.0, 1.0)
altitude_data_label.anchored_position = (470, DISPLAY_HEIGHT-25)
altitude_data_label.scale = (1)
altitude_data_label.color = text_white

vbat_label = label.Label(small_font)
vbat_label.anchor_point = (1.0, 1.0)
vbat_label.anchored_position = (DISPLAY_WIDTH, 15)
vbat_label.scale = (1)

# Load Bitmap to tile grid first (background layer)
bitmap = displayio.OnDiskBitmap("/images/Astral_Fruit_8bit.bmp")
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
text_group = displayio.Group()
text_group.append(tile_grid)

# Label Display Group (foreground layer)
text_group.append(hello_label)
text_group.append(vbat_label)
text_group.append(temp_label)
text_group.append(temp_data_label)
text_group.append(humidity_label)
text_group.append(humidity_data_label)
text_group.append(barometric_label)
text_group.append(barometric_data_label)
text_group.append(altitude_label)
text_group.append(altitude_data_label)
display.show(text_group)
vbat_label.text = "{:.2f}".format(vbat)
while True:
    # Label.text in the loop for sensor data updates
    hello_label.text = "Simple Offline Weatherstation"
    
    # Changes battery voltage color depending on charge level
    if vbat_label.text >= "4.00":
        vbat_label.color = text_green
    elif vbat_label.text >= "3.80" and vbat_label.text <= "3.99":
        vbat_label.color = text_yellow
    elif vbat_label.text >= "3.75" and vbat_label.text <= "3.79":
        vbat_label.color = text_orange
    elif vbat_label.text <= "3.74":
        vbat_label.color = text_red
    else:
        vbat_label.color = text_white
        
    vbat_label.text
    temp_label.text = "°F"
    temp_data_label.text = "{:.1f}".format(bmp280.temperature*1.8+32)
    humidity_label.text = "Humidity"
    humidity_data_label.text = "{:.1f} %".format(sht31d.relative_humidity)
    altitude_label.text = "Altitude"
    altitude_data_label.text = "{:.1f} f".format(bmp280.altitude*3.28)
    barometric_label.text = "Pressure"
    barometric_data_label.text = f"{bmp280.pressure:.1f}"

    # Serial printout for debugging
    # print("Temperature: {:.1f} F".format(bmp280.temperature*1.8+32))
    # print("Humidity: {:.1f} %".format(sht31d.relative_humidity))
    # print("Barometric pressure:", bmp280.pressure)
    # print("Altitude: {:.1f} m".format(bmp280.altitude))
    print("VBat voltage: {:.2f}".format(vbat))

    time.sleep(5.0)
    pass