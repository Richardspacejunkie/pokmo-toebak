"""

POKMO_BETA v0.2
---------------|
image recognition version for more accuracy and works at night and morning and day!
---------------|

"""

#libs

import re
import pyautogui
import time
import random
import win32api, win32con

#win32api key values

win_down = 0x28
win_up = 0x26
win_left = 0x25
win_right = 0x27
win_w = 0x57
win_q = 0x51
win_d = 0x44

#win api key click function

def click_key(x):
    win32api.keybd_event(x,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(x,0,win32con.KEYEVENTF_KEYUP,0)

#game time check function

def game_time_check():
    if pyautogui.locateOnScreen("night_char_grass_down.PNG") or pyautogui.locateOnScreen("night_char_grass_up.PNG") or pyautogui.locateOnScreen("night_char_grass_left.PNG") or pyautogui.locateOnScreen("night_char_grass_right.PNG") != None:
        return "night"
    elif pyautogui.locateOnScreen("dawn_char_grass_down.PNG") or pyautogui.locateOnScreen("dawn_char_grass_up.PNG") or pyautogui.locateOnScreen("dawn_char_grass_left.PNG") or pyautogui.locateOnScreen("dawn_char_grass_right.PNG") != None:
        return "dawn"
    elif pyautogui.locateOnScreen("day_char_grass_down.PNG") or pyautogui.locateOnScreen("day_char_grass_up.PNG") or pyautogui.locateOnScreen("day_char_grass_left.PNG") or pyautogui.locateOnScreen("day_char_grass_right.PNG") != None:
        return "day"

#attack function

attack_times = 0
pp = 0

def attack():
    global attack_times
    global pp
    if attack_times == pp:
        print("go to the pokemon center and re-enter your PP (press enter when in the grass)\n")
        attack_times = 0
        main()
    attack_times += 1
    print(f"{attack_times} times attacked")
    click_key(win_w)
    time.sleep(0.2)
    click_key(win_w)
    time.sleep(3)

#move function

def move():
    print("moving")
    click_key(win_q)
    time.sleep(0.1)
    click_key(win_q)
    click_key(win_d)
    time.sleep(0.1)
    click_key(win_d)
    time.sleep(0.1)
    click_key(win_d)

#main app

def main():
    global pp
    pp = int(input("Give 1st move PP: "))
    game_time = game_time_check()
    print(f"In game time: {game_time}")
    print("Starting...\n")
    for i in range(0,5):
        print(i)
        time.sleep(1)
    pyautogui.FAILSAFE = True
    print("Done")
    while True:
        if game_time == "day":
            if pyautogui.locateOnScreen("day_fight.PNG") != None:
                time.sleep(0.2)
                attack()
            elif pyautogui.locateOnScreen("day_char_grass_down.PNG") or pyautogui.locateOnScreen("day_char_grass_up.PNG") or pyautogui.locateOnScreen("day_char_grass_left.PNG") or pyautogui.locateOnScreen("day_char_grass_right.PNG") != None:
                move()
        elif game_time == "night":
            if pyautogui.locateOnScreen("night_fight.PNG") != None:
                time.sleep(0.2)
                attack()
            elif pyautogui.locateOnScreen("night_char_grass_down.PNG") or pyautogui.locateOnScreen("night_char_grass_up.PNG") or pyautogui.locateOnScreen("night_char_grass_left.PNG") or pyautogui.locateOnScreen("night_char_grass_right.PNG") != None:
                move()
        elif game_time == "dawn":
            if pyautogui.locateOnScreen("dawn_fight.PNG") != None:
                time.sleep(0.2)
                attack()
            elif pyautogui.locateOnScreen("dawn_char_grass_down.PNG") or pyautogui.locateOnScreen("dawn_char_grass_up.PNG") or pyautogui.locateOnScreen("dawn_char_grass_left.PNG") or pyautogui.locateOnScreen("dawn_char_grass_right.PNG") != None:
                move()

#run condition

if __name__ == '__main__':
    main()