#!/usr/bin/python2.7
"""Print a swatch using all 256 colors of 256-color-capable terminals."""

__author__ = "Marius Gedminas <marius@gedmin.as>"
__url__ = "https://gist.github.com/mgedmin/2762225"
__version__ = '2.0'


def hrun(start, width, padding=0):
    x = [None] * padding + list(range(start, start + width)) + [None] * padding
    return x


def vrun(start, width, height, padding=0):
    return [hrun(s, width, padding)
            for s in range(start, start + width * height, width)]


layout = [
    vrun(0, 8, 2),                # 16 standard xterm colors
    vrun(16, 6, 6 * 6, 1),        # 6x6x6 color cube
    vrun(16 + 6 * 6 * 6, 8, 3),   # 24 grey levels
]


def fg_seq(color):
    return '\033[38;5;%dm' % color


def bg_seq(color):
    return '\033[48;5;%dm' % color

reset_seq = '\033[0m'


def color_bar(seq, color, trail):
    if color is None:
        return '%s    %s' % (reset_seq, trail)
    else:
        return '%s %03d%s' % (seq(color), color, trail)

def color_block(seq, color, trail):
    return '%s  %s' % (seq(color), reset_seq)

def showpalette():
    for block in layout:
        print("")
        for row in block:
            fg_bar = ''.join(color_bar(fg_seq, color, '') for color in row)
            bg_bar = ''.join(color_bar(bg_seq, color, ' ') for color in row)
            print('%s%s    %s%s ' % (fg_bar, reset_seq, bg_bar, reset_seq))


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
  max=31
  median=15
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

from random import randint
import time

def ansi_pixel(ptup):
    return 16 + (36 * int(ptup[0]*6.0/256.0) + 6 * int(ptup[1]*6.0/256.0) + int(ptup[2]*6.0/256.0))

def print_bar(l):
  bg_bar = ' '.join(color_block(bg_seq, color, ' ') for color in l)
  print(chr(27) + "[2J")
  print('[ %s%s ]\n' % (bg_bar, reset_seq))

def main():
  #showpalette()
  l = [45, 67, 89, 99, 120, 140, 245, 19]
  
  for r in xrange(10):
      print(chr(27) + "[2J")
      d = []
      for i in xrange(8):
          d.append(randint(0,5) - 2)
      for i in xrange(len(l)):
          l[i] = clamp(l[i] + d[i])
      bg_bar = ' '.join(color_block(bg_seq, color, ' ') for color in l)
      print('%s%s \n' % (bg_bar, reset_seq))
      print color
      time.sleep(0.3)

if __name__ == '__main__':
    main()
