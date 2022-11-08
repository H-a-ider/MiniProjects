# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
engine.say("I like Python")
engine.runAndWait()