from microbit import *
import neopixel
np = neopixel.NeoPixel(pin0, 64)

x=0
y=0

while True:
    # UP
    dx,dy=0,0
    if pin8.read_digital()==0:
        dy=-1
    if pin14.read_digital()==0:
        dy=1
    if pin12.read_digital()==0:
        dx=-1
    if pin13.read_digital()==0:
        dx=1
    np[y*8+x]=(0,0,0)
    x=x+dx
    x=max(0,x)
    x=min(7,x)
    y=y+dy
    y=max(0,y)
    y=min(7,y)
    np[y*8+x]=(20,20,20)
    np.show()
    sleep(200)
