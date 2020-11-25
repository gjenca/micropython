from microbit import *
import neopixel

#hra lodicky, privelka

np = neopixel.NeoPixel(pin0, 64)

np.clear()

#farby


#tvary

els=[[1,8,8],[1,7,8],[8,7,1],[8,8,1],[6,1,1],[8,1,1],[1,1,8],[1,1,6]]
uboot=[[7,1,8,8],[8,1,7,8],[8,7,1,8],[8,8,1,7],[6,1,1,1],[1,1,1,7],[7,1,1,1],[1,1,1,6]]


watercolor=(0,0,0)
drawcolor=(10,10,10)

shipcolor=[drawcolor,(10,0,10),(0,0,20), (10,5,0), (0,10,0)]

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

def starringnbh(poloha):
    if poloha%8==0:
        nbh=[poloha +1]
    elif poloha%8==7:
        nbh=[poloha-1]
    else:
        nbh=[poloha+1,poloha-1]
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
        okolie=starringnbh(poloha)
        while not okolie==[]:
            k=okolie.pop()
            if not truecolor[k][1]==watercolor:
                if k not in tvar:
                    tvar.append(k)
                    for p in starringnbh(k):
                        if not p in okolie:
                            okolie.append(p)
    return tvar
            
        

# tvar lode??

def tvarlode(poloha):
    tvar=0
    shipshape=shape(poloha)
    shipshape.sort()
    if len(shipshape)==2:
        tvar=1
    elif len(shipshape)==3:
        if shipshape[1]-shipshape[0]==shipshape[2]-shipshape[1]:
            tvar=2       
    elif len(shipshape)==4:
        rozdiely=[ shipshape[1]-shipshape[0], shipshape[2]-shipshape[1], shipshape[3]-shipshape[2]]
        if rozdiely in els:
            tvar=3
            
    elif len(shipshape)==5:
        rozdiely=[ shipshape[1]-shipshape[0], shipshape[2]-shipshape[1], shipshape[3]-shipshape[2],shipshape[4]-shipshape[3]]
        if rozdiely in uboot:
            tvar=4 
    return [tvar,shipshape]
        


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
        t=tvarlode(y*8+x)
        for i in t[1]:
            truecolor[i]=[1,shipcolor[t[0]]]
           
           
    if pin15.read_digital()==0:
        if not truecolor[y*8+x][1]==watercolor:
            shipshape=shape(y*8+x)
            truecolor[y*8+x][1]=watercolor
            t=tvarlode(shipshape[1])
            for i in t[1]:
                truecolor[i]=[1,shipcolor[t[0]]]

   

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

"""
 elif len(shipshape)==4:
            rozdiely=[ shipshape[1]-shipshape[0], shipshape[2]-shipshape[1], shipshape[3]-shipshape[2]]
            if rozdiely in els:
                for i in shipshape:
                    truecolor[i]=[1,shipcolor[2]] 
        elif len(shipshape)==5:
            rozdiely=[ shipshape[1]-shipshape[0], shipshape[2]-shipshape[1], shipshape[3]-shipshape[2],shipshape[4]-shipshape[3]]
            if rozdiely in uboot:
                for i in shipshape:
                    truecolor[i]=[1,shipcolor[3]] 

      elif len(shipshape)==3:
            if shipshape[1]-shipshape[0]==shipshape[2]-shipshape[1]:
                if shipshape[1]-shipshape[0] in [1,8]:
                    for i in shipshape:
                        truecolor[i]=[1,shipcolor[1]]
                   
                
"""            


