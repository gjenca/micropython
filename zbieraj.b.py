import neopixel,random
from microbit import *
np=neopixel.NeoPixel(pin0,64)
kurzor=[[0,0],[0,1],[1,0],[1,1]]
def vykresli(x,y,r,g,b):
    np[y*8+x]=(r,g,b)
    np.show()
while True:
     if pin8.read_digital()==0:
        for x in kurzor:
            if x[0]==0:
                pass
            else: 
                x[0]-=1
     if pin16.read_digital()==0:
        for x in kurzor:
            if x[0]==7:
                pass
            else: 
                x[0]+=1 
     if pin13.read_digital()==0:
        for x in kurzor:
            if x[1]==7:
                pass
            else: 
                x[1]+=1
     if pin12.read_digital()==0:
        for x in kurzor:
            if x[1]==0:
                pass
            else: 
                x[1]+=1
   


    

     for i in kurzor:
        vykresli(i[1],i[0],random.randrange(20),random.randrange(20),random.randrange(20))




















    







    
