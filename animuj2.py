from microbit import*
import neopixel,random
i=500

np=neopixel.NeoPixel(pin0,64)

for b in range (500):
    for x in range(random.randint(10,64)):
        inde=random.randrange(64)
        np[inde]=(random.randint(1,10),random.randint(1,10),random.randint(1,10))
    np.show()

    sleep(i)
    np.clear()
    i=max(i-1,0)
display.clear()