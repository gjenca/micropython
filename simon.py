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
    sleep(150)

display.scroll("opakuj po mne")

sim=0
hraj=[]

while True:
    ja=0
    k=0
    hraj.append(random.randrange(4))
    for nota in hraj:
        zahraj(nota)
    while ja<=sim and k<100:
        k=10
        if pin8.read_digital()==0:
            k=2
        if pin14.read_digital()==0:
            k=3
        if pin12.read_digital()==0:
            k=0
        if pin13.read_digital()==0:
            k=1
        if k<10:
            zahraj(k)
            if not k==hraj[ja]:
                display.show(Image.SAD)
                k=100
                break
            else: 
                ja=ja+1
    if k==100:
        break
    else:
        display.show(Image.HAPPY)
        sleep(500)
        display.clear()
        sim=sim+1

sleep(1000)
display.scroll(sim)


