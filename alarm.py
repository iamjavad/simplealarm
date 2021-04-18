#!/usr/bin/python3

import datetime
from playsound import playsound

wakeup = input(str("Enter the wake-up time(HH:MM):"))

while True:
    x = datetime.datetime.now()
    x = x.strftime("%H"+":"+"%M")
    if x == wakeup:
        print('wake up')
        playsound('Hans Zimmer - Cornfield Chase.mp3')
        break
