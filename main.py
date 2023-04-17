# Script for the Roblox game 'Project Mugetsu' made by TheRealChicken#5230
# Features:
# - Auto Meditate puzzle
# - Assign own key for meditation
# - Auto re-enter Meditation
# - Auto Check for focus on Roblox window


import threading
import time

import pyautogui
import pydirectinputs
from win32gui import GetWindowText, GetForegroundWindow

# **!Change the values below to your liking!**
meditate_key = "k"  # The key to press for meditation
auto_enter_med = True  # Flag to enable/disable auto entering meditation **FLAG WORKING**
check_window = True  # Flag to enable/disable checking for focus on Roblox window **FLAG WORKING**
check_window_cooldown = .1  # Interval between window focused check. also the time for the script to start. **WORKING**

# **!Ignore anything below unless you know what you are doing!**
focused = threading.Event()  # Event to indicate if the Roblox window is in focus
focused.set()  # Set the event to true by default for the functions to work when check_window is disabled aka


# "spoofing" that the tab is focused.


def check_focus():
    """
    Thread function to check if the Roblox window is in focus
    """
    while True:
        if GetWindowText(GetForegroundWindow()) == "Roblox":
            focused.set()  # Set the event if the window is in focus
            time.sleep(.1)  # Sleep .1 second before clearing the event
        else:
            time.sleep(check_window_cooldown)
            print(f"Current Tab: {GetWindowText(GetForegroundWindow())} Please focus on the Roblox Tab.")
            focused.clear()  # Clear the event


def find_letter():
    """
    Function to find and press the letters W, A, S, D on the screen
    """
    letters = ["W", "A", "S", "D"]
    while True:
        if not focused.is_set():
            continue
        for letter in letters:
            location = pyautogui.locateOnScreen("Pictures\{}.png".format(letter), grayscale=True, confidence=0.8,
                                                region=(850, 450, 200,
                                                        200))  # Search for the letter image in the specified region
            if location is not None:
                press_letter(letter)  # Press the letter if found
            else:
                pass


def press_letter(letter):
    """
    Function to press a letter on the keyboard
    """
    pydirectinput.press(letter.lower())  # Press the letter in lowercase


def stay_menu():
    """
    Function to check if the menu is open and press the meditation key if not
    """
    time.sleep(check_window_cooldown + .5)  # Wait for Window check to run once to prevent pressing before.
    while True:
        if not focused.is_set():
            continue
        location = pyautogui.locateOnScreen("Pictures\menu.png", grayscale=True, confidence=0.8,
                                            region=(
                                                10, 300, 250, 250))  # Search for the menu image in the specified region
        if location is None:
            press_letter(meditate_key)  # Press the meditation key if the menu is not found
            time.sleep(1)

def main():
    """
    Main function to run the script
    """
    print("Now focus on the Roblox Tab.\nStarting in {} seconds..".format(check_window_cooldown))
    if check_window:
        check_focus_thread = threading.Thread(target=check_focus, daemon=True)  # Create thread to check for focus
        check_focus_thread.start()
    if auto_enter_med:
        stay_menu_thread = threading.Thread(target=stay_menu,
                                            daemon=True)  # Create thread to check if meditate menu is open
        stay_menu_thread.start()
    find_letter()  # Find and press letters


if __name__ == '__main__':
    main()

# Regions used for finding the letters, can be modified depending on resolution above
# letter_reg = (850,450,200,200)
# menu_reg = (10, 300, 250, 250)
