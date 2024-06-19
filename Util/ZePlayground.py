import threading
import time
import pyautogui as pag
import random as rnd
from pynput import keyboard

from ItemSlots import *
from MainFunctions import *
from MouseMovement import *
from Welcome import *

welcome()

# Global variables to control the clicker state
running = False
running_lock = threading.Lock()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Walker Program
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def walker():
    """Loop that performs clicks at a fixed interval while running is True."""
    global running
    while True:
        with running_lock:
            if not running:
                break
        bank_near_inv()
        sleepif()
        click()
        sleep()
        deposit_all()
        sleep()
        sleepif() 
        click()
        bank_slot(7)
        sleepif()
        click()
        bank_slot(8)
        sleep(.5, .5)
        get_x_items()
        sleepif()
        sleep(.5, .5)
        exit_bank()
        sleep(.01, .5)
        sleepif()
        click()
        sleep(3) 
        inv_slot(1)
        sleepif()
        click()
        inv_slot(2)
        sleepif()
        click()
        sleep(.5, 3)
        spacekey()
        sleep(30 ,30)
        

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Program
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def toggle_program():
    """Toggle the running state and start/stop the program."""
    global running
    with running_lock:
        running = not running
        if running:
            threading.Thread(target=walker, daemon=True).start()
        print("Program running" if running else "Program stopped")

def exit_program():
    """Exit the program by setting running to False and printing a message."""
    global running
    with running_lock:
        running = False
    print("Exiting program")
    exit(0)

def on_press(key):
    """Handle key press events to toggle the clicker or exit the program."""
    if key == keyboard.Key.ctrl_l:
        toggle_program()
    elif key == keyboard.Key.ctrl_r:
        exit_program()

def main():
    """Main function to start the keyboard listener."""
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
