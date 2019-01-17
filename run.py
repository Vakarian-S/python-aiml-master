#!/usr/bin/env python3
# -*- coding: cp1252 -*-
from pip._vendor.distlib.compat import raw_input
import speech_recognition as sr
import aiml
import sys
import pyttsx3 as pyttsx
import re

r = sr.Recognizer()

engine = pyttsx.init()

voices = engine.getProperty('voices')
#indice para voz [0] - Español-HELENA ; [1] Ingles-ZIRA;[2] Ingles-SABINA
engine.setProperty('voice', voices[2].id)

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml es")

while True:

    with sr.Microphone() as source:
        print("Habla tu mensaje >> "),

        audio = r.listen(source, phrase_time_limit=5)
    try:
        mensaje = r.recognize_sphinx(audio_data=audio, language='es-ES')
        print(mensaje)
    except sr.UnknownValueError:
        mensaje = 'error'
        print(mensaje)
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        mensaje = 'error'
        print(mensaje)
        print("No se logro realizar la consulta; {0}".format(e))

   # mensaje = raw_input("tu mensaje: ")
    answer = (kernel.respond(mensaje))
    print(answer)
    engine.say(answer.decode("utf8"))
    engine.runAndWait()

    if re.search('(adios|chao|me tengo que ir|hasta luego)',mensaje):
        break