# -*- coding: cp1252 -*-
from pip._vendor.distlib.compat import raw_input

import aiml
import sys
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml es")

while True:
    print (kernel.respond(raw_input("Enter your message >> ")))
