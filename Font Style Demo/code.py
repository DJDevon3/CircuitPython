import board
import displayio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_hx8357 import HX8357

# This sketch should also work for the 2.5" TFT Featherwing, just change the size.
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

# Some quick colors. 
text_black = (0x000000)
text_blue = (0x0000FF)
text_cyan = (0x00FFFF)
text_green = (0x00FF00)
text_magenta = (0xFF00FF)
text_orange = (0xFFA500)
text_red = (0xFF0000)
text_white = (0xFFFFFF)
text_yellow = (0xFFFF00)

# Load Fonts including massive 121 BDF font.
small_font = bitmap_font.load_font("/fonts/Arial-12.bdf")
medium_font = bitmap_font.load_font("/fonts/Arial-16.bdf")
huge_font = bitmap_font.load_font("/fonts/GoodTimesRg-Regular-121.bdf")

# Foreground Text Labels
hello_label = label.Label(small_font)
hello_label.anchor_point = (0.5, 1.0)
hello_label.anchored_position = (DISPLAY_WIDTH/2, 15)
hello_label.scale = (1)
hello_label.color = text_white

test_label = label.Label(medium_font)
test_label.anchor_point = (0.5, 1.0)
test_label.anchored_position = (DISPLAY_WIDTH/2, 70)
test_label.scale = (3)
test_label.color = text_orange

test_data_label = label.Label(medium_font)
test_data_label.anchor_point = (0.5, 1.0)
test_data_label.anchored_position = (DISPLAY_WIDTH/2, 170)
test_data_label.scale = (3)
test_data_label.color = text_orange

clean_label = label.Label(huge_font)
clean_label.anchor_point = (0.5, 1.0)
clean_label.anchored_position = (DISPLAY_WIDTH/2, 300)
clean_label.scale = (1)
clean_label.color = text_orange

# ============= Shadow & Outline Font Styles ===========
test_shadow = label.Label(medium_font)
test_shadow.anchor_point = (0.5, 1.0)
test_shadow.anchored_position = (DISPLAY_WIDTH/2+2, 70+2)
test_shadow.scale = (3)
test_shadow.color = text_black

test_outline1 = label.Label(medium_font)
test_outline1.anchor_point = (0.5, 1.0)
test_outline1.anchored_position = (DISPLAY_WIDTH/2-2, 170-2)
test_outline1.scale = (3)
test_outline1.color = text_black

test_outline2 = label.Label(medium_font)
test_outline2.anchor_point = (0.5, 1.0)
test_outline2.anchored_position = (DISPLAY_WIDTH/2-2, 170+2)
test_outline2.scale = (3)
test_outline2.color = text_black

test_outline3 = label.Label(medium_font)
test_outline3.anchor_point = (0.5, 1.0)
test_outline3.anchored_position = (DISPLAY_WIDTH/2+2, 170-2)
test_outline3.scale = (3)
test_outline3.color = text_black

test_outline4 = label.Label(medium_font)
test_outline4.anchor_point = (0.5, 1.0)
test_outline4.anchored_position = (DISPLAY_WIDTH/2+2, 170+2)
test_outline4.scale = (3)
test_outline4.color = text_black

clean_outline1 = label.Label(huge_font)
clean_outline1.anchor_point = (0.5, 1.0)
clean_outline1.anchored_position = (DISPLAY_WIDTH/2-2, 300-2)
clean_outline1.scale = (1)
clean_outline1.color = text_black

clean_outline2 = label.Label(huge_font)
clean_outline2.anchor_point = (0.5, 1.0)
clean_outline2.anchored_position = (DISPLAY_WIDTH/2-2, 300+2)
clean_outline2.scale = (1)
clean_outline2.color = text_black

clean_outline3 = label.Label(huge_font)
clean_outline3.anchor_point = (0.5, 1.0)
clean_outline3.anchored_position = (DISPLAY_WIDTH/2+2, 300-2)
clean_outline3.scale = (1)
clean_outline3.color = text_black

clean_outline4 = label.Label(huge_font)
clean_outline4.anchor_point = (0.5, 1.0)
clean_outline4.anchored_position = (DISPLAY_WIDTH/2+2, 300+2)
clean_outline4.scale = (1)
clean_outline4.color = text_black

# Load Bitmap to tile grid first (background layer)
bitmap = displayio.OnDiskBitmap("/images/purbokeh_8.bmp")
tile_grid = displayio.TileGrid(
    bitmap,
    pixel_shader=bitmap.pixel_shader,
    width=1,
    height=1,
    tile_width=DISPLAY_WIDTH,
    tile_height=DISPLAY_HEIGHT)

text_group = displayio.Group()
text_group.append(tile_grid)

main_group = displayio.Group()
main_group.append(text_group)

# Text Foreground Layer
# It's very important to append style before its foreground text.
text_group.append(hello_label)

text_group.append(test_shadow)
text_group.append(test_label)

text_group.append(test_outline1)
text_group.append(test_outline2)
text_group.append(test_outline3)
text_group.append(test_outline4)
text_group.append(test_data_label)

text_group.append(clean_outline1)
text_group.append(clean_outline2)
text_group.append(clean_outline3)
text_group.append(clean_outline4)
text_group.append(clean_label)

display.show(main_group)

shadow_demo = "Shadow"
outline_demo = "Outline"
clean_demo = "HUGE"
while True:
    hello_label.text = "Font Style Demo"
    
    test_shadow.text = shadow_demo
    test_label.text = shadow_demo

    test_outline1.text = outline_demo
    test_outline2.text = outline_demo
    test_outline3.text = outline_demo
    test_outline4.text = outline_demo
    test_data_label.text = outline_demo
    
    clean_outline1.text = clean_demo
    clean_outline2.text = clean_demo
    clean_outline3.text = clean_demo
    clean_outline4.text = clean_demo
    clean_label.text = clean_demo
