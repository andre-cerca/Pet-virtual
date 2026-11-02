from machine import Pin, I2C
import ssd1306
import framebuf
import time
import animations

while True:
    animations.standby()
    animations.wordNotFound()
