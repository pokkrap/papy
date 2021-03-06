"""
A simulator for Pimoroni's Blink!
https://shop.pimoroni.com/products/blinkt

Simulates the Blink! library.
https://github.com/pimoroni/blinkt

Uses Pygame for the UI.
https://www.pygame.org/news
"""

import sys
import colors

NUM_PIXELS = 8
PIXEL_BOUNDARY = 50

clear_on_exit = True
pixels = [(0, 0, 0, 0.2)] * NUM_PIXELS

def _exit():
    """Placeholder for compatibility."""
    pass

def set_brightness(brightness):
    """Set the brightness of all pixels
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """

    if brightness < 0 or brightness > 1:
        raise ValueError("Brightness should be between 0.0 and 1.0")

    for x in range(NUM_PIXELS):
        pixels[x][3] = int(255.0 * brightness)

def clear():
    """Clear the pixel buffer"""
    set_all(0, 0, 0, 0)

def show():
    _draw()

def set_all(r, g, b, brightness=None):
    """Set the RGB value and optionally brightness of all pixels
    If a brightness value is not supplied,
    the last value set for each pixel is kept
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    for x in range(NUM_PIXELS):
        set_pixel(x, r, g, b, brightness)

def get_pixel(x):
    """Get the RGB and brightness value of a specific pixel
    :param x: The horizontal position of the pixel: 0 to 7
    """
    r, g, b, brightness = pixels[x]
    brightness = brightness * (1.0 / 255.0)
    return r, g, b, round(brightness, 3)

def set_pixel(x, r, g, b, brightness=None):
    """Set the RGB value, and optionally brightness, of a single pixel
    If you don't supply a brightness value, the last value will be kept.
    :param x: The horizontal position of the pixel: 0 to 7
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    if brightness is None:
        brightness = pixels[x][3]
    else:
        brightness = int(255.0 * brightness)

    pixels[x] = [int(r), int(g), int(b), brightness]

def set_clear_on_exit(value=True):
    """Placeholder for compatability.
    :param value: True or False (default True)
    """
    clear_on_exit = value

def draw_bar(l):
    colors.print_bar(l)

def _draw():
    y_position = int(PIXEL_BOUNDARY / 2)
    radius = int(PIXEL_BOUNDARY / 3)  # Leave some space around each 'LED'

    termcolors = map(colors.ansi_pixel, pixels)
    draw_bar(termcolors)

    #for x in range(NUM_PIXELS):
    #    color = pixels[x]
