#!/usr/bin/python2.7

from blinkt import set_pixel, set_brightness, show, clear
import time

clear()
set_pixel(0, 255, 0, 0)
set_pixel(1, 0, 225, 0)
set_pixel(2, 0, 0, 225)
set_pixel(3, 255, 255, 0)
set_pixel(4, 0, 225, 255)
set_pixel(5, 255, 0, 225)
set_pixel(6, 180, 180, 180)
set_pixel(7, 50, 50, 50)
show()
time.sleep(1)
