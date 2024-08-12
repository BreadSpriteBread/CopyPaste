import keyboard as kbd
import os
import time

while True:
    kbd.wait('F1')
    f = open("clipboard.txt", "r")
    data = f.read()
    kbd.write(data)
    print("pasted")
