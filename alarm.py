#!/usr/bin/python3

import datetime
from playsound import playsound

while True:
    x = datetime.datetime.now()
    x = x.strftime("%H"+":"+"%M")
    if x == '22:23':
        print('wake up')
        playsound('')
        break
