#Exercise 9 - Shoutouts to Everyone in Python ANS!!

from gtts import gTTS
import os
mytext = input("Enter your text: ")
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")
