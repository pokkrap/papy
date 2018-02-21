#!/usr/bin/python2.7

from blinkt import set_pixel, set_brightness, show, clear
import time
from random import randint

# pixel jump 50 times
for i in xrange(50):
    # switch off all pixels
    clear()
    # use randint() to pick a random number from 0,1,2,3,4,5,6,7 
    pos = randint(0,7)
    # set chosen position with green light
    set_pixel(pos, 0, 255, 0)
    # show light
    show()
    # wait a bit (0.3s)
    time.sleep(0.5)
