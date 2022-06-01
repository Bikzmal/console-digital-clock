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
        minutes = f'0{intmins}' if intmins < 10 else str(intmins)
    elif intsecs < 9:
        intsecs += 1
        seconds = f'0{intsecs}'
    else:
        intsecs += 1
        seconds = str(intsecs)

    if intmins == 60:
        minutes = '00'
        intmins = 0
        inthrs += 1
        hours = f'0{inthrs}' if inthrs < 10 else str(inthrs)
    if inthrs == 24:
        hours = '00'
        inthrs = 0

    time.sleep(1)
