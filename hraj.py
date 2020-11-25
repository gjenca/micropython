from microbit import*
import neopixel,random,music

noty=[
    "C4:4",
    "D4:4",
    "E4:4",
    "F4:4",
]

trojfunkcie=[
    lambda x,y: x<=2 and x+1<=y<=6-x,
    lambda x,y: x>=5 and 8-x<=y<=x-1,
    lambda x,y: y<=2 and y+1<=x<=6-y,
    lambda x,y: y>=5 and 8-y<=x<=y-1,
]

farby=[
    (10,0,0),
    (0,10,0),
    (0,0,10),
    (10,0,10),
]

np=neopixel.NeoPixel(pin0,64)

np.clear()

def zahraj(nota):
    for i in range(64):
        x=i%8
        y=i//8
        if trojfunkcie[nota](x,y):
            np[i]=farby[nota]
    np.show()           
    sleep(150)
    music.play(noty[nota],pin2)
    np.clear()
    sleep(100)

hraj=[]

for i in range(5):
    hraj.append(random.randrange(4))

for nota in hraj:
    zahraj(nota)


"""
def zahraj(zoz):
    for nota in zoz:
        if nota==0:
           for i in range(64):
                 x=i%8
                 y=i//8
                 if x<=2 and x+1<=y<=6-x:
                      np[i]=(10,0,0)
           np.show()           
           sleep(150)
           music.play("C4:4",pin2)
           np.clear()
           sleep(100)
        elif nota==1:
            for i in range(64):
                x=i%8
                y=i//8
                if x>=5 and 8-x<=y<=x-1:
                    np[i]=(0,10,0)
            np.show()
            sleep(150) 
            music.play("D4:4",pin2)
            np.clear()
            sleep(100)
        elif nota==2:
            for i in range(64):
                x=i%8
                y=i//8
                if y<=2 and y+1<=x<=6-y:
                    np[i]=(0,0,10)
                    
            np.show()
            sleep(150)
            music.play("E4:4",pin2)
            np.clear()
            sleep(100)
        elif nota==3:
            for i in range(64):
                x=i%8
                y=i//8
                if y>=5 and 8-y<=x<=y-1:
                    np[i]=(10,0,10)

            np.show()
            sleep(150)
            music.play("F4:4",pin2)
            np.clear()
            sleep(100)
"""






