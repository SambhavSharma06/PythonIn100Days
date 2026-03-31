# Solution + Shoutouts - Desktop Notification System in Python!!

import time
import winsound

REPEAT_INTERVAL = 6

while True:
    print("Hey Harry, Drink water")
    winsound.Beep(1000, 1000)  # sound alert
    time.sleep(REPEAT_INTERVAL)
