from microbit import *
import radio
radio.on()
radio.send("syn")
while True:
    rcv=radio.receive()
    if rcv=="syn":
        radio.send("ack")
        prvost=1
        display.show(1)
    if rcv=="ack":
        prvost=2
        display.show(2)


