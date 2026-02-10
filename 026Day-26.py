#Exercise 2: Solution & Shoutouts!!
import time

t = time.strftime('%H:%M:%S')
hour = int(time.strfttime('%H'))

if(hour >=0 and hour <12):
    print("GM")
elif(hour >=12 and hour <16):
    print("GA")
elif(hour >=16 and hour <21):
    print("GN")
