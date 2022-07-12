# SPDX-FileCopyrightText: 2022 DJDevon3 for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Analog Out Single-Color LED Candle Flicker Example"""
import board
import time
import random
from analogio import AnalogOut

analog_out = AnalogOut(board.A0)

# Manually Set Flicker Type = Breeze or Gust
Flicker_Type = ("Gust")

Breeze_Flicker = random.randint(50000, 60000)
Gust_Flicker = random.randint(10000, 30000)
random_low = random.randint(1000, 50000)
while True:
    if Flicker_Type == ("Breeze"):
        Breeze_Flicker = random_low
    elif Flicker_Type == ("Gust"):
        Gust_Flicker = random_low
    else:
        random_low
        pass
    random.randint(50000, 60000)
    random_high = random.randint(60000, 65535)
    analog_out.value = random.randint(random_low, random_high)
    rand_sleep = random.uniform(.001, 0.005)
    time.sleep(rand_sleep)
    pass
