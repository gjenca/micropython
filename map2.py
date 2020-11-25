from microbit import *
import neopixel


VODA=0
LOD=1
ZASAH=2


np = neopixel.NeoPixel(pin0, 64)

np.clear()
x=0
y=0


shipcolor=[(10,10,0),(10,0,10), (10,5,0), (0,10,0)]
clr=0

watercolor=(0,1,2)

#status=[VODA]*64
for i in range(64):
    np[i]=watercolor

truecolor=[watercolor]*64

boat=Image("00000:"
            "00000:"
            "00990:"
            "00000:"
            "00000")

kriznik=Image("00000:"
            "00000:"
            "09990:"
            "00000:"
            "00000")

liet=Image("00000:"
            "00090:"
            "09990:"
            "00000:"
            "00000")

uboat=Image("00000:"
            "00900:"
            "09990:"
            "00000:"
            "00000")
bl=Image()

ships=[boat,bl, boat,bl, boat,bl, kriznik,bl, kriznik,bl, liet,bl, liet,bl, uboat,bl]

display.show(ships,delay=700,wait=False, loop=True, clear=True)


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
            truecolor[y*8+x]=shipcolor[clr]

    # zmaz bod
    if pin16.read_digital()==0:
        if not truecolor[y*8+x]==watercolor:
            truecolor[y*8+x]= watercolor
    

    #zmen farbu
    if button_a.is_pressed():
        clr=(clr+1)%4
        

    # skonci
    if button_b.is_pressed():
        kolko=truecolor.count(watercolor)
        if kolko ==40:
            display.scroll("hotovo",delay=100)
            sleep(100)
            break
        elif kolko >40:
            display.scroll("to je malo", delay=70)
            display.show(ships,delay=700,wait=False, loop=True, clear=True)
        else:   
            display.scroll("to je vela", delay=70)
            display.show(ships,delay=700,wait=False, loop=True, clear=True)
    
    np[y*8+x]= truecolor[y*8+x]
    
    x=x+dx
    x=x%8
    y=y+dy
    y=y%8

    np[y*8+x]=(10,10,10)
    np.show()
    sleep(150)


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
    

    np[y*8+x]= truecolor[y*8+x]

    x=x+dx
    x=x%8
    y=y+dy
    y=y%8

    np[y*8+x]=(10,10,10)
    np.show()
    sleep(150)
