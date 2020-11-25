from microbit import *
import neopixel
import random

RED=(15,0,0)
GREEN=(0,15,0)
BLUE=(0,0,15)
MAGENTA=(15,0,15)
YELLOW=(15,15,0)
CYAN=(0,15,15)


COLORS=[RED,GREEN,BLUE,MAGENTA,YELLOW,CYAN]

np = neopixel.NeoPixel(pin0, 64)


def setpixel(x,y,color):

    np[y*8+x]=color

def square(x1,y1,x2,y2,color):

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            setpixel(x,y,color)

np.clear()
i=0
t=500
while True:
    np.clear()
    color=COLORS[i % len(COLORS)]
    i=i+1
    t=max(t-1,0)
    x1=random.randint(0,7)
    x2=random.randint(x1,7)
    y1=random.randint(0,7)
    y2=random.randint(y1,7)
    square(x1,y1,x2,y2,color)
    np.show()
    sleep(t)


