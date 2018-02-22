#!/usr/bin/python2.7
from blinkt import set_pixel, set_brightness, show, clear
import time
from random import randint


def simple_demo():
    clear()
    set_pixel (1,0,255,0)
    show()
    time.sleep(1)


def show_primary_colors():
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

def jumpy():
    for i in xrange(2):
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

def scrolly():
    for i in xrange(500):
        # switch off all pixels
        clear()
        # use randint() to pick a random number from 0,1,2,3,4,5,6,7
        pos = i%8
        # set chosen position with blue light
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        set_pixel(pos, r, g, b)
        # show light
        show()
        # wait a bit (0.3s)
        time.sleep(0.12)

def bouncy():
    for i in xrange(500):
        # switch off all pixels
        clear()
        # use randint() to pick a random number from 0,1,2,3,4,5,6,7
        l = [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0]
        pos = l[i%14]
        # set chosen position with blue light
        set_pixel(pos, 0, 0, 255)
        # show light
        show()
        # wait a bit (0.3s)
        time.sleep(0.11)


def bouncer():
    for i in xrange(500):
        # switch off all pixels
        clear()
        # use randint() to pick a random number from 0,1,2,3,4,5,6,7
        l = [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0]
        pos = l[i%14]
        # set chosen position with blue light
        r=255-pos*32
        g=0
        b=pos*32
        set_pixel(pos, r, g, b)
        #set_pixel(pos, 0, 0, 255)
        # show light
        show()
        # wait a bit (0.3s)
        time.sleep(0.01)


#simple_demo()
#show_primary_colors()
#show_primary_colors()
#scrolly()
#bouncy()
bouncer()
