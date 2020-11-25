import microbit,radio,random

radio.on()
radio.send(str(random.randint(1,10)))

while True:
    r=radio.receive()
    if r:
        microbit.display.scroll(r,delay=90)

