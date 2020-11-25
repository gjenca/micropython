from microbit import *
import neopixel

np = neopixel.NeoPixel(pin0, 64)

np.clear()

watercolor=(0,1,2)
drawcolor=(10,10,10)
#okolia bodu

def starnbh(poloha):
    if poloha%8==0:
        nbh=[poloha,poloha +1]
    elif poloha%8==7:
        nbh=[poloha-1,poloha]
    else:
        nbh=[poloha,poloha+1,poloha-1]
    if poloha +8 <64:
        nbh.append(poloha+8)
    if poloha-8 >=0:
        nbh.append(poloha-8)
    return nbh

def squarenbh(poloha):
    if poloha%8==0:
        nbh=[poloha,poloha+1]
        if poloha +8 <64:
            nbh.extend([poloha+8,poloha+9])
        if poloha -8 >= 0:
            nbh.extend([poloha-8,poloha-7])
 
    elif poloha%8==7:
        nbh=[poloha,poloha-1]
        if poloha +8 <64:
            nbh.extend([poloha+8,poloha+7])
        if poloha -8 >= 0:
            nbh.extend([poloha-8,poloha-9])
    else:
        nbh=[poloha,poloha+1,poloha-1]
        if poloha +8 <64:
            nbh.extend([poloha+8,poloha+7,poloha+9])
        if poloha -8 >= 0:
            nbh.extend([poloha-8,poloha-9,poloha-7])
    return nbh

# suvisla zafarbena oblast obsahujuca bod

def shape(poloha):
    tvar=[]
    if not truecolor[poloha][1]==watercolor:
        tvar.append(poloha)
        okolie=starnbh(poloha)
        while not okolie==[]:
            k=okolie.pop()
            if not truecolor[k][1]==watercolor:
                if k not in tvar:
                    tvar.append(k)
                    for p in starnbh(k):
                        if not p in okolie:
                            okolie.append(p)
    return tvar
            
        
        
        


#pociatocne zafarbenie



for i in range(64):
    np[i]=watercolor

truecolor=[[0,watercolor]]*64

x=0
y=0

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
 
    # zafarbi bod na bielo

    if pin16.read_digital()==0:
        truecolor[y*8+x]=[1, drawcolor]
               
            
   #zafarbi suvislu zafarbenu oblast na modrozeleno

    if pin15.read_digital()==0:
        for i in shape(y*8+x):
            truecolor[i]=[1,(0,10,10)]


    for i in range(64):
        np[i]= truecolor[i][1]
 
    x=x+dx
    x=x%8
    y=y+dy
    y=y%8

    np[y*8+x]=(5,5,5)
    np.show()
    sleep(150)


"""
    #pridaj bod

    if pin15.read_digital()==0:
        truecolor[y*8+x]=[1,(10,0,0)]
"""



