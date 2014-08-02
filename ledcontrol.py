# MicroPython example for controlling one WS2812 LED.
# Method similar to http://www.espruino.com/WS2811
# Attribution to Markus Gritsch

from pyb import SPI

spi = SPI(1, SPI.MASTER, baudrate=6400000, polarity=0, phase=1)
spi.send(chr(0x00))

def byte2bits(byte):
    b0 = chr(0x03)
    b1 = chr(0x0F)
    bits = ''
    mask = 0x80
    while mask != 0:
        bits += b0 if ( byte & mask ) == 0 else b1
        mask >>= 1
        return bits

def sendColor(red, green, blue):
    spi.send(byte2bits(green)+byte2bits(red)+byte2bits(blue))

import math

n = 0
while True:
    r = int((1 + math.sin(n * 0.1324)) * 127)
    g = int((1 + math.sin(n * 0.1654)) * 127)
    b = int((1 + math.sin(n * 0.1)) * 127)
    sendColor(r, g, b)
    n += 1
    pyb.delay(20)


