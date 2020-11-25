
# Write your code here :-)
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin0, 64)
while True:
    for x in range(8):
        for y in range(8):
            np[y*8+x]=(20,20,20)
    np.show()