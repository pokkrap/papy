#!/usr/bin/python

from blinkt import set_pixel, set_brightness, show, clear
import time
from random import randint

rs=[0,0,0,0,0,0,0,0]
bs=[0,0,0,0,0,0,0,0]
gs=[0,0,0,0,0,0,0,0]

# random color
def rc():
  #return (randint(0,256), randint(0,256), randint(0,256))
  r = randint(0,256)
  #g = randint(0,256)
  g = 5
  b = randint(0,256)
  return (r,g,b)

# random delta
def rd():
  max=101
  median=50
  dr = randint(0,max)-median
  dg = randint(0,max)-median
  db = randint(0,max)-median
  return (dr,dg,db)

def clamp(v):
  if v > 255:
    return 255
  elif v < 0:
    return 0
  return v

def runshow():
  for i in xrange(8):
    r,g,b = rc()
    #print("-==", r, g, b)
    rs[i] = r
    gs[i] = g
    bs[i] = b
    #print("x--", rs[i], gs[i], bs[i]),

  for rep in xrange(140):
    clear()
    for i in xrange(8):
      dr,dg,db = rd()
      #print(i, rs[i], dr, gs[i], dg, bs[i], db, " --> "), 
      rs[i] = clamp(rs[i]+dr)
      gs[i] = clamp(gs[i]+dg)
      bs[i] = clamp(bs[i]+db)
      set_pixel(i, rs[i], gs[i], bs[i], 0.05)
      #print(rs[i], gs[i], bs[i]),
    show()
    time.sleep(0.5)
    #print ""

runshow()
