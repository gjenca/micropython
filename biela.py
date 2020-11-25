from microbit import *
import neopixel



np = neopixel.NeoPixel(pin0, 64)

def red():
    for i in range(64):
        np[i]=(0,0,i*2)
    np.show()
    
red()

