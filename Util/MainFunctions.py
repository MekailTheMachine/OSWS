import time
import random as rnd
import pyautogui as pag

def sleep(c = .01 , x = .005, z = 0.005): #C is a constant. X and Z are both multiplied by a number between 0-1.
    time.sleep(c + rnd.random() *x + rnd.random() *z) #Set variables so sleep() is viable for a .01 ~ .05 second sleep

def sleepif(x=0.01):
    if (rnd.random() > 0.0383):
        time.sleep(rnd.random() *0.001 + 0.001)
        if (rnd.random() > 0.0504):
            time.sleep(rnd.random() *0.001 + 0.001)
        if (rnd.random() > 0.008284):
            time.sleep(rnd.random() *0.001 + 0.001)
            if (rnd.random() > 0.09420):
                time.sleep(rnd.random() * x + 0.005)
            if (rnd.random() > 0.263):
                time.sleep(rnd.random() * x + 0.01)
            if (rnd.random() > 0.381251):
                time.sleep(rnd.random() * (x * 2) + 0.01)
            if (rnd.random() > 0.591251):  
                time.sleep(rnd.random() * (x * 2) + 0.01)
            if (rnd.random() > 0.793):
                time.sleep(rnd.random() * (x * 3) + 0.02)
            if (rnd.random() > 0.891251):
                time.sleep(rnd.random() * (x * 4) + 0.02)
            if (rnd.random() > 0.9180251):  
                time.sleep(rnd.random() * (x * 28) + 0.02)
            if (rnd.random() > 0.981251):  
                time.sleep(rnd.random() * (x * 9) + 0.04)
                if (rnd.random() > 0.89):
                    time.sleep(rnd.random() *0.09 + 0.04) 
                    if (rnd.random() > 0.871251):
                        time.sleep(rnd.random() *0.05 + 0.05)
                        print(" Long click!")
    if (rnd.random() > 0.981251):  
        time.sleep(rnd.random() *0.3 + 0.01)

#Define a more human like click.
def click(hold = 0):
    pag.mouseDown(button='left')  # Press the right button down
    sleep(hold)
    sleepif()
    pag.mouseUp(button='left') # Lift right button up (Finish click)
    sleep()

def quick_click(): #Another Left Click variant
    pag.mouseDown(button='left')  # press the right button down
    sleepif()
    pag.mouseUp(button='left')
    #Hold the mouse down for a period of time rather a simple click
    sleep()

def right_click(hold =0.01):
    pag.mouseDown(button='right')  # Press the right button down
    sleepif()
    sleep(hold)
    pag.mouseUp(button='right') # Lift right button up (Finish click)
    sleep()

def upkey(hold = 2): #Hold the up key to adjust the camera view
    pag.keyDown('up')
    sleep(hold, .01, .001)
    pag.keyUp('up')
    sleep()

#Define downkey function

def downkey(hold =2): #Hold the down key to adjust camera view
    pag.keyDown('down')
    sleep(hold, .01, .001)
    pag.keyUp('down')
    sleep()

#Define a function that will push down the left key for 3 seconds, then release it.

def leftkey(x = 1):
    pag.keyDown('left')
    sleep(x, .001, .001)
    pag.keyUp('left')
    sleep()

def spacekey(x = .05):
    pag.keyDown('space')
    sleep(x, .1, .1)
    pag.keyUp('space')
    sleep() 

