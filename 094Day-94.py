# Drink water exercise in Python!!

# We import tools we need
from win10toast import ToastNotifier   # for showing notifications
import time                            # for waiting


# This creates our "notification buddy"
toaster = ToastNotifier()

# What your reminder will say (feel free to change tone!)
title = "Hey you 👀"
message = "Take a sip of water 💧 Stay sharp."

# How often you want the reminder (in minutes)
interval_minutes = 10

# Convert minutes to seconds (Python works in seconds)
seconds = interval_minutes * 60

print("\nYour water buddy is now active 💧")
print("I'll remind you every 10 minutes.")
print("Don't ignore me 😄")
print("Press CTRL + C anytime to stop.\n")

while True:

    # Send the notification
    toaster.show_toast(
        title,
        message,
        duration=7,     # stays on screen for 7 seconds
        threaded=True   # allows code to continue smoothly
    )

    # Wait while the notification is still showing
    # (so we don't stack multiple notifications)
    while toaster.notification_active():
        time.sleep(0.1)

    # Now we chill for 10 minutes before the next reminder
    time.sleep(seconds)
