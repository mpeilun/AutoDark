import os
import time
import threading
from unicodedata import name
from PIL import Image

import numpy as np

import pystray
from pystray import MenuItem as item

import screen_brightness_control as sbc

from mss import mss

def quit(icon):
    print('stop')
    icon.stop()
    long_thread.do_run = False

image=Image.open("image.ico")
icon=pystray.Icon(name='AutoDark', icon=image, title='AutoDark', menu=[item('Quit', quit)])

def switch(status):
    monitors = sbc.list_monitors()
    monitorLight = sbc.get_brightness(display=monitors[1])[0]
    if(status == 0):
        if(monitorLight != 0):
            sbc.set_brightness(0, display=monitors[1])
            print("turn off")
    else:
        if(monitorLight == 0):
            sbc.set_brightness(100, display=monitors[1])
            print("turn on")

def run(arg):
    with mss() as sct:
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            monitor = sct.monitors[2]
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    
            try:
                color = img.getcolors()[0][1]
                if(color == (0,0,0)):
                    switch(0)
                else:
                    switch(1)
            except:
                switch(1)
            finally:
                time.sleep(1)

long_thread = threading.Thread(target=run, args=("task",))
long_thread.start()

icon.run()