import neopixel,random,music,radio
from microbit import *
np=neopixel.NeoPixel(pin0,64)
krzr=[]
startmusic=["C4:6","C4:6","A4:8"]
spapane=["A4:4"]
zjedene=0
pochod=2
dx,dy=0,0
natahu=False
def vykresli(x,y,r,g,b):
    np[y*8+x]=(r,g,b)
def kurzor(x,y,z):
    zoz=[]
    z=z//2
    for i in range(x,x+z):
        for e in range(y,y+z):
            zoz.append((i,e))
    return(zoz)
def generate(count):
    zoz=[]
    for i in range(count):
        zoz.append((random.randrange(count),random.randrange(count)))
    return(zoz)
zozbodiek=generate(8)
np.show()
music.play(startmusic,pin2)
radio.on()
radio.send("syn")
while True:
    if radio.receive():
        if radio.receive()=="syn":
            natahu=False
            radio.send("ACK")
            break
        elif radio.receive()=="ACK":
            natahu=True
            break
        elif radio.receive()=="prehral som":
            display.scroll("You win!")
            break
       # else:
      #      try:
      #          int(radio.receive())
       #     except:
        #        zozbodiek=list(radio.receive()).remove(',')
         #   else:
          #      zjedene=int(radio.receive())
          #      

if natahu:
    for i in range (random.randint(100,200)):
        if pin8.read_digital()==0:
            if dy>0:
                 np.clear()
                 dy-=1
        if pin13.read_digital()==0:
            if dx<8-pochod//2:
                np.clear()
                dx+=1

        if pin14.read_digital()==0:
            if dy<8-pochod//2:
               np.clear()
               dy+=1
        if pin12.read_digital()==0:
            if dx>0:
                np.clear()
                dx-=1
        if accelerometer.current_gesture()=="shake":
            radio.on()
            radio.send(str(zozbodiek).replace("[","").replace("]",""))
            radio.send(str(zjedene))
            natahu=False
       
        for i in zozbodiek:
            for x in krzr:
                if i==x:
                    zjedene+=1
                    music.play(spapane,pin2)
                    zozbodiek.remove(i)
                    if pochod<8 and dx<8-pochod//2 and dy<8-pochod//2:
                        pochod+=1
                    elif pochod>1:
                        pochod-=1
                        np.clear()
                    
        krzr=kurzor(dx,dy,pochod)
        for i in krzr:
            vykresli(i[0],i[1],10,20,5)
            np.show()
        for i in zozbodiek:
            vykresli(i[0],i[1],5,10,20)
        if len(zozbodiek)==0:
            zozbodiek=generate(8)
        sleep((100-zjedene)*2)
    else:
        radio.send("prehral som")
        display.scroll("Game over")











    







    
