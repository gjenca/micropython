from microbit import *
import neopixel


VODA=0
LOD=1
ZASAH=2


np = neopixel.NeoPixel(pin0, 64)
def red():
   for i in range(64):
        np[i]=(10,0,0)

x=0
y=0

watercolor=(0,0,0)
shipcolor=(10,0,0)
#forbidden=set()
status=[VODA]*64

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

    #pridaj bod

    if pin15.read_digital()==0:
        if y*8+x not in forbidden:
            status[y*8+x]=LOD
        else:   
            display.show("!")
            sleep(100)
            display.clear()

    # zmaz bod
    if pin16.read_digital()==0:
        if status[y*8+x]==LOD and y*8+x not in forbidden:
            np[y*8+x]= color
            status[y*8+x]=VODA

    # pridaj lod
    if button_b.is_pressed():
        for i in range(64):
            if status[i]==LOD:
                if i%8==0:
                    forbidden={i,i+1,i-8,i-7, i+9,i+8}|forbidden
                elif i%8==7:
                    forbidden={i-1,i, i-9,i-8, i+7,i+8}|forbidden
                else:
                    forbidden={i-1,i,i+1, i-9,i-8,i-7, i+7,i+8,i+9}|forbidden
        for i in forbidden:
            if i<0 or i >63:
                forbidden.remove(i)
        display.scroll("LOD")
        sleep(100)

    if status[y*8+x]==VODA:
        np[y*8+x]= color
    else:
        np[y*8+x]=(10,0,0)
   # for i in forbidden:
   #     np[i]=(0,10,10)
    x=x+dx
    x=x%8
    y=y+dy
    y=y%8

    np[y*8+x]=(10,10,10)
    np.show()
    sleep(150)
