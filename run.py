# -*- coding: cp1252 -*-
from pip._vendor.distlib.compat import raw_input

import aiml
import sys
import pyttsx3 as pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
#indice para voz [0] - Español-HELENA ; [1] Ingles-ZIRA;[2] Ingles-SABINA
engine.setProperty('voice', voices[2].id)


kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml es")

while True:
    answer = (kernel.respond(raw_input("Enter your message >> ")))
    print(answer)
    engine.say(answer)
    engine.runAndWait()