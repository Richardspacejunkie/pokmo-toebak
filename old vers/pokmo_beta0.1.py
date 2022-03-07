"""

POKMO_BETA v0.1
---------------|
basic pixel scanning auto battler not very accurate and broken
---------------|

"""

#libs

from glob import glob
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

#attack function

attack_times = 0
pp = 0

def attack():
    global attack_times
    global pp
    attack_times += 1
    if attack_times == pp:
        print("go to the pokemon center and re-enter your PP (press enter when in the grass)\n")
        attack_times = 0
        main()
    print(f"{attack_times}'s attacked")
    click_key(win_w)
    click_key(win_w)
    time.sleep(3)

#main app

def main():
    global pp
    pp = int(input("Give 1st move PP: "))
    print("Starting...\n")
    for i in range(0,10):
        print(i)
        time.sleep(1)
    pyautogui.FAILSAFE = True
    print("Done")
    while True:
        if pyautogui.pixel(1343, 453)[0] > 230:
            if pyautogui.pixel(350, 585)[0] > 250:
                time.sleep(1)
                attack()
        elif pyautogui.pixel(800, 425)[1] == 40:
            print("moving")
            click_key(win_q)
            time.sleep(0.3)
            click_key(win_q)
            time.sleep(0.3)
            click_key(win_q)
            time.sleep(0.3)
            click_key(win_d)
            time.sleep(0.3)
            click_key(win_d)
            time.sleep(0.3)
            click_key(win_d)
            time.sleep(0.3)

#run condition

if __name__ == '__main__':
    main()