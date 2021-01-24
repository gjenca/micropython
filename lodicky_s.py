from microbit import *
import radio, neopixel, random, music

#nahodne lodicky, synchronizacia

np = neopixel.NeoPixel(pin0, 64)
np.clear()

shipcolor=(0,10,0)
watercolor=(0,1,2)
enemy_watercolor=(0,10,10)
hit=(10,0,0)
#drowned=(10,10,0)

# funkcia prirad moje pole

def draw_my(field):
    for i in range(64):
        if field[i]==0:
            np[i]=watercolor
        if field[i]==1:
            np[i]=shipcolor
        if field[i]==2:
            np[i]=hit


# FUNKCIA prirad superovo pole

def draw_enemy(field):
    for i in range(64):
        if field[i]==0:
            np[i]=(0,0,0)
        if field[i]==1:
            np[i]=enemy_watercolor
        if field[i]==2:
            np[i]=hit


x=0
y=0

myfield=bytearray(64)
opfield=bytearray(64)

for i in range(64):
    opfield[i]=0
    myfield[i]=0

for i in range(20):
    kde=random.randrange(64)
    myfield[kde]=1 

#vykresli svoje pole

draw_my(myfield)
np.show()


display.scroll("Press A if ready",wait=False,loop=True)

while True:
    if button_a.is_pressed():
        display.clear()
        break

prvost=0
radio.on()
radio.send("syn")
#
#
##poradie hracov
#
while not prvost:
    rcv=radio.receive()
    if rcv=="syn":
        radio.send("ack")
        prvost=1
        display.show(1)
    if rcv=="ack":
        prvost=2
        display.show(2)

while True:
##########   hrac na tahu

    if prvost==1:
        display.show(prvost)
        #display.scroll("Your turn. Press A.",wait=False)
        while True:
            if button_a.is_pressed():
                #display.scroll("Enemy field",wait=False)
                draw_enemy(opfield)
                np.show()
                break

        while prvost==1:
   
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
             
            
            rec=0

    #posli bod

            if pin15.read_digital()==0:
                radio.send(chr(y*8+x)) 
                while not rec:
                    rcv=radio.receive()
                    if rcv=='water':       #miss
                        rec=1
                        #music.play(music.POWER_DOWN,pin=pin2,wait=False)
                        prvost=2
                    if rcv=='hit':       #hit
                        rec=2
                        #music.play(music.POWER_UP,pin=pin2,wait=False)
                    if rcv=='znova':
                        pass
                opfield[y*8+x]=rec

            draw_enemy(opfield)
            x=x+dx
            x=x%8
            y=y+dy
            y=y%8

            if rec==0:
                np[y*8+x]=(5,5,5)
            
            
            np.show()
            display.show(prvost)

            sleep(200)

    else:  #######     druhy hrac
        draw_my(myfield)
        np.show()

        #sleep(200)


        while prvost==2:
            zasah=False
            rcv=radio.receive()
            if rcv is None:
                continue
            rcv=ord(rcv)
           # display.show(rcv)
            if myfield[rcv]==0:
                np[rcv]=(20,10,0)
                np.show()
                sleep(1000)
                radio.send('water')
                prvost=1
            if myfield[rcv]==1:
                myfield[rcv]=2
                radio.send('hit')
                zasah=True    
            if myfield[rcv]==2:
                radio.send('znova')

            #if zasah:
                #music.pitch(440,1000,pin=pin2,wait=False)
                #pin1.write_digital(1)
                #sleep(500)
                #pin1.write_digital(0)
            draw_my(myfield)

            np.show()
           # sleep(1000)
                   
    


    

