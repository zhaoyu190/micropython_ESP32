from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
import tsl2561
import _thread
i2c = I2C(sda=Pin(27), scl=Pin(14))
oled = SSD1306_I2C(128, 64, I2C(sda=Pin(21), scl=Pin(22)), addr=0x3c)
sensor = tsl2561.TSL2561(i2c)
def show_lux():
    while 1:
        oled.fill(0)
        #print(sensor.read())
        oled.text(str(sensor.read()),0,0)
        oled.show()
_thread.start_new_thread(show_lux())