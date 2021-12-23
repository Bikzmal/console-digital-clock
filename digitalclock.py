import time
import os

seconds = '00'
intsecs = int(seconds)

minutes = '00'
intmins = int(minutes)

hours = '00'
inthrs = int(hours)

clear = "cls" if os.name in ('nt', 'dos') else "clear"

while True:
    os.system(clear)
    print(f"{hours}:{minutes}:{seconds}")

    if intsecs == 59:
        seconds = '00'
        intsecs = 0
        intmins += 1
        if intmins < 10:
            minutes = '0' + str(intmins)
        else:
            minutes = str(intmins)
    elif intsecs < 9:
        intsecs += 1
        seconds = '0' + str(intsecs)
    else:
        intsecs += 1
        seconds = str(intsecs)

    if intmins == 60:
        minutes = '00'
        intmins = 0
        inthrs += 1
        if inthrs < 10:
            hours = '0' + str(inthrs)
        else:
            hours = str(inthrs)

    if inthrs == 24:
        hours = '00'
        inthrs = 0

    time.sleep(1)
