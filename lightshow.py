#!/usr/bin/python2.7
from blinkt import set_pixel, set_brightness, show, clear
import time
from random import randint


def simple_demo():
    clear()
    set_pixel (1,50,195,100)
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
    for i in xrange(50):
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
        time.sleep(0.1)

def bouncy():
    for i in xrange(50):
        # switch off all pixels
        clear()
        # use randint() to pick a random number from 0,1,2,3,4,5,6,7
        l = [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0]
        pos = l[i%14]
        # set chosen position with blue light

        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        set_pixel(pos, r, g, b)
        #set_pixel(pos, 0, 0, 255)
        # show light
        show()
        # wait a bit (0.3s)
        time.sleep(0.1)

def bouncer():
    for i in xrange(50):
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
        time.sleep(0.1)

def dance():
    for i in xrange(100):
        clear()
        l= [[0, 2, 4, 6], [1, 3, 5, 7]]
        poslist=l[i%2]
        for pos in poslist:
        #poslist is a set of positions of pixels
            r=0
            g=255-pos*32
            b=pos*32
            set_pixel(pos, r, g, b)
        show()
        time.sleep(0.1)



def blackscrolly():
    for i in xrange(50):
        # switch off all pixels
        clear()
        bpos = i%8
        for pos in xrange(8):
            if bpos == pos:
                set_pixel(pos, 255, 255, 255)
            else:
                set_pixel(pos, 240, 100, 0)
        # show light
        show()
        # wait a bit (0.3s)
        time.sleep(0.05)

def dancy():
    for i in xrange(50):
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
        time.sleep(0.1)

def double():
    for i in xrange(32):
        # switch off all pixels
        clear()
        # use randint() to pick a random number from 0,1,2,3,4,5,6,7
        pos = i%4
        for pos in xrange(8):
            if pos%4-i%4 == 0:
                set_pixel(pos, 255, 255, 255, 0.05)
            elif pos%4-i%4 == 1:
                set_pixel(pos, 255, 0, 0, 0.05)
            elif pos%4-i%4 == 2:
                set_pixel(pos, 0, 255, 0.05)
            elif pos%4-i%4 == 3:
                set_pixel(pos, 0, 0, 255, 0.05)
            elif pos%4-i%4 == -1:
                set_pixel(pos, 255, 0, 0, 0.05)
            elif pos%4-i%4 == -2:
                set_pixel(pos, 0, 255, 0, 0.05)
            elif pos%4-i%4 == -3:
                set_pixel(pos, 0, 0, 255, 0.05)
        show()
        time.sleep(0.5)

def scrollyd():
    for i in xrange(50):
        # switch off all pixels
        clear()
        # use randint() to pick a random number from 0,1,2,3,4,5,6,7
        pos = 7-i%8
        # set chosen position with blue light
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        set_pixel(pos, r, g, b)
        # show light
        show()
        print (pos, r, g, b)
        # wait a bit (0.3s)
        time.sleep(0.5)

def scrollytwoway():
    for i in xrange(50):
        clear()
        pos = i%8
        spos = 7-i%8
        set_pixel(pos, 0, 200, 50)
        set_pixel(spos, 64, 132, 255)
        show()
        time.sleep(0.1)

def build_random_list():

    l = []
    for i in xrange(8):
        l.insert(0, randint(0,10))
        print l
    return l

def colorlist(numcolors):
    l = []
    for i in xrange(numcolors):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        l.append((r, g, b))
    return l

def scrollrandom():
    l = colorlist(8)
    for a in xrange(50):
        clear()
        for i in xrange(8):
            c = l[i]
            set_pixel( i, c[0], c[1], c[2])
        show()
        time.sleep(0.2)
        last_l = l.pop()
        l.insert(0, last_l)






#simple_demo()
#show_primary_colors()
#show_primary_colors()
#scrolly()
#double()
#bouncy
#bouncer
#blackscrolly
#scrollyd()
#scrollytwoway()
#print "the list is : ", newlist
scrollrandom()