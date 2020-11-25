from microbit import*
import music
hudba=[]
cdur=["C4:4","D4:4","E4:4","F4:4","G4:4","A4:4",'H4:4']
amol=["A4:4",'H4:4',"C5:4","D5:4","E5:4","F5:5","G5:5","A5:5"]
stupnica=[]
def nahraj():
    while True:
        if button_b.is_pressed():
            stupnica=amol[:]
            display.scroll("A mol")
            break
        if button_a.is_pressed():
            stupnica=cdur[:]
            display.scroll("C dur")
            break
    while True:
        if button_a.is_pressed()and button_b.is_pressed():
                display.scroll("ZACIATOK NAHRAVANIA",delay=100)
                while True:
                    if pin8.read_digital()==0:
                        music.play(stupnica[1],pin2)
                        hudba.append("C4:4")
                    if pin13.read_digital()==0:
                        music.play(stupnica[2],pin2)
                        hudba.append("D4:4")
                    if pin14.read_digital()==0:
                        music.play(stupnica[3] ,pin2)
                        hudba.append("E4:4")
                    if pin12.read_digital()==0:
                        music.play(stupnica[4],pin2)
                        hudba.append("F4:4")
                    if pin15.read_digital()==0:
                        music.play(stupnica[5],pin2)
                        hudba.append("G4:4")
                    if pin16.read_digital()==0:
                        music.play(stupnica[6],pin2)
                        hudba.append("A4:4")
                    if button_a.is_pressed():
                        music.play=(stupnica[7],pin2)
                        hudba.append("H4:4")
                    if button_b.is_pressed():
                        music.play(stupnica[8],pin2)
                        hudba.append("C5:4")
                    if pin15.read_digital()==0 and pin16.read_digital()==0:
                        hudba.pop()
                        hudba.pop()
                        return()
nahraj()

while True:
    if pin15.read_digital()==0 and pin16.read_digital()==0:
        for tone in hudba:
           music.play(tone,pin2)
