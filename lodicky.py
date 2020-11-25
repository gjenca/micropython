from microbit import *
import neopixel

#hra lodicky

#pridavanie lodi: 3*cln xx, 2*kriz xxx, 2*liet xxX, 1*uboat xxXx 


def kolko(k,zoz):
    kol=0
    for i in zoz:
        if i==k:
            kol=kol+1
    return kol

#okolie bodu 'poloha'


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
                if kolko(k,tvar)==0:
                    tvar.append(k)
                    for p in starringnbh(k):
                        if kolko(p,okolie)==0 and kolko(p,tvar)==0:
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
hit=(10,0,0)
drowned=(10,10,0)

for i in range(64):
    np[i]=watercolor

truecolor=bytearray(64)

hitcolor=bytearray(64)

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
        water=kolko(0,truecolor)
        draw=kolko(1,truecolor)
        ships=64-water-draw
        if draw>0:
            display.scroll("neulozene")
        elif ships<25:
            display.scroll("malo")
        elif ships>25:
            display.scroll("vela")
        else:
            display.scroll("lode nacitane")
            break




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

np.clear()



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
     
    if pin15.read_digital()==0:
        if truecolor[y*8+x]==0:
            display.scroll("voda")
            hitcolor[y*8+x]=1
        elif truecolor[y*8+x]==200:
            display.scroll("old hit")
        else:
            eshipno=truecolor[y*8+x]
            hitcolor[y*8+x]=eshipno
            truecolor[y*8+x]=200
            if kolko(eshipno,truecolor)==0:
                display.scroll("drowned")
                for i in range(64):
                    if hitcolor[i]==eshipno:
                        hitcolor[i]=200
            else:
                display.scroll("hit")
                
                
    for i in range(64):
        if hitcolor[i]==0:
            np[i]=(0,0,0)
        elif hitcolor[i]==1:
            np[i]=watercolor
        elif hitcolor[i]==200:
            np[i]=drowned
        else:
            np[i]=hit


    x=x+dx
    x=x%8
    y=y+dy
    y=y%8

    np[y*8+x]=(5,5,5)
    np.show()
    sleep(150)



