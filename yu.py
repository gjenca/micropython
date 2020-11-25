from microbit import *
import music

while True:
    try:
        music.pitch(accelerometer.get_y(), 10,pin2)
    except ValueError:
        pass

