from microbit import *
import neopixel

#hra lodicky

def isin(k,zoz):
    je=False
    for i in zoz:
        if i==k:
            je=True
    return je

#okoloie bodu 'poloha'


def starringnbh(poloha):
    nbh=bytearray()
    if poloha%8==0:
        nbh.append(poloha +1)
    elif poloha%8==7:
        nbh.append(poloha-1)
    else:
        nbh.append(poloha+1)
        nbh.append(poloha-1)
    if poloha +8 <64:
        nbh.append(poloha+8)
    if poloha-8 >=0:
        nbh.append(poloha-8)
    return nbh

#utvar obsahujuci 'poloha'

def shape(poloha):
    tvar=bytearray()
    if not truecolor[poloha]==0:
        tvar.append(poloha)
        okolie=starringnbh(poloha)
        for k in okolie:
            if not truecolor[k]==0:
                if not isin(k,tvar):
                    tvar.append(k)
                    for p in starringnbh(k):
                        if not isin(p,okolie) and not isin(p,tvar):
                            okolie.append(p)
    return tvar
            



np = neopixel.NeoPixel(pin0, 64)

np.clear()
x=0
y=0

#water=0, draw=1, ship>=2

shipcolor=(0,10,0)
drawcolor=(10,10,10)
watercolor=(0,1,2)

for i in range(64):
    np[i]=watercolor

truecolor=bytearray(64)

shipno=2

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
            truecolor[y*8+x]=1

    #zmaz bod

    
    if pin16.read_digital()==0:
        truecolor[y*8+x]= 0

    #pridaj lod

    if button_b.is_pressed():
        if not truecolor[y*8+x]==0:
            shipshape=shape(y*8+x)
            for i in shipshape:
                truecolor[i]=shipno
            shipno=shipno+1  


    if button_a.is_pressed():
        display.show(truecolor[y*8+x])


    #vykresli
    
    for i in range(64):
        if truecolor[i]==0:
            np[i]=watercolor
        elif truecolor[i]==1:
            np[i]=drawcolor
        else:
            np[i]=shipcolor
    
    x=x+dx
    x=x%8
    y=y+dy
    y=y%8

    np[y*8+x]=(5,5,5)
    np.show()
    sleep(150)





"""
    # zmaz bod
    if pin16.read_digital()==0:
        if not truecolor[y*8+x]==watercolor:
            truecolor[y*8+x]= watercolor
    

    # pridaj lod

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
    
    if truecolor[y*8+x]==0:
        np[y*8+x]=watercolor
    elif truecolor[y*8+x]=1:
        np[y*8+x]=drawcolor
    else:
        np[y*8+x]=shipcolor
    
    x=x+dx
    x=x%8
    y=y+dy
    y=y%8

    np[y*8+x]=(5,5,5)
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
"""
