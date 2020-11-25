from microbit import *
import neopixel



np = neopixel.NeoPixel(pin0, 64)
def red():
   for i in range(64):
        np[i]=(10,0,0)

x=0
y=0
svieti=set()


while True:
    # pohyb kurzora
    dx,dy=0,0

    if pin8.read_digital()==0:
        dy=-1
    if pin14.read_digital()==0:
        dy=1
    if pin12.read_digital()==0:
        dx=-1
    if pin13.read_digital()==0:
        dx=1

    #pridaj do svieti

    if pin15.read_digital()==0:
        svieti.add(y*8+x)

    # zmaz vsetko

    if button_b.is_pressed():
        np.clear()
        svieti=set()

    # zasviet vsetko

    if button_a.is_pressed():
        svieti=set(range(64))
        red()

    # zmaz
    if pin16.read_digital()==0:
        if y*8+x in svieti:
            np[y*8+x]=(0,0,0)
            svieti.remove(y*8+x)

    if y*8+x not in svieti:
        np[y*8+x]=(0,0,0)
    else:
        np[y*8+x]=(10,0,0)

    x=x+dx
    x=x%8
    y=y+dy
    y=y%8

    np[y*8+x]=(10,10,10)
    np.show()
    sleep(150)