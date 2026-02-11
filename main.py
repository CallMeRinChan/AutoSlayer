from PIL import Image, ImageGrab
from matplotlib import pyplot as plt
import keyboard
import numpy as np
import cv2
import time
import os
import random
import sys

def getScreenshot():
    return ImageGrab.grab()

active = False
counter = 0
print("starting AutoSlayer...")

while True:
    if(keyboard.read_key() == "="):
        active = not active
        time.sleep(0.1)
        print("AutoSlayer is now active")

    if(keyboard.read_key() == "-"):
        print("AutoSlayer turning off...")
        time.sleep(0.25)
        sys.exit()

        
    
    if(active):
        randID = random.randint(0,12345)
        getScreenshot().save(f"./images_test/image_{randID}.png")
        print(f"Image has been saved as image_{randID}.png")
        
        # image = cv2.imread(f"./images_test/image_{randID}.png")
        # imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # plt.imshow(imageGray)
        # plt.show()
        # active = False
        # TODO: haar cascade xml file(s) for image detection.

        counter += 1
        if(counter > 99):
            active = False
            print("100 screenshots have been taken")

        time.sleep(5)
    



