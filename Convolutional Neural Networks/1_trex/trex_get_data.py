# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:21:41 2021

@author: asus
"""

import keyboard
import uuid # this library allows recording on the screen
import time 
from PIL import Image # Python Image Library
from mss import mss


"""
http://www.trex-game.skipser.com/

"""


mon = {"top":410, "left":720, "width":250, "height":100}
sct = mss() # mss ; crop ROI, convert to frame


i = 0

def record_screen(record_id, key):
    
    global i
    
    i += 1
    print("{}: {}".format(key, i)) # key is what we press on the keyboard, i is how many times we press
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./img/{}_{}_{}.png".format(key, record_id, i)) #create a img folder and when you run this code and play the game it fills images into this file
    
is_exit = False 

# if we press the esc key, it quits from the function


def exit():
    
    global is_exit
    is_exit = True
    
keyboard.add_hotkey("esc", exit)

record_id = uuid.uuid4()

while True:
    
    if is_exit: break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            record_screen(record_id, "up")
            time.sleep(0.1)
            
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            record_screen(record_id, "down")
            time.sleep(0.1)
            
        elif keyboard.is_pressed("right"):
            record_screen(record_id, "right")
            time.sleep(0.1)
            
    except RuntimeError: continue
            

