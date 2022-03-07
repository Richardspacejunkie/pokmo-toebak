"""

POKMO_BETA v0.3
---------------|
NEW!
- new PP system with multiple move functionallity
Changed
- Runs faster than v0.2
---------------|

"""

#libs

import pyautogui
import time
import win32api, win32con

#win32api key values

win_w = 0x57

win_s = 0x53
win_q = 0x51
win_d = 0x44
win_z = 0x5A

#win api key click function

def click_key(x):
    win32api.keybd_event(x,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(x,0,win32con.KEYEVENTF_KEYUP,0)

#game time check function

# def game_time_check():
#     if pyautogui.locateOnScreen("night_char_grass_down.PNG") or pyautogui.locateOnScreen("night_char_grass_up.PNG") or pyautogui.locateOnScreen("night_char_grass_left.PNG") or pyautogui.locateOnScreen("night_char_grass_right.PNG") != None:
#         return "night"
#     elif pyautogui.locateOnScreen("dawn_char_grass_down.PNG") or pyautogui.locateOnScreen("dawn_char_grass_up.PNG") or pyautogui.locateOnScreen("dawn_char_grass_left.PNG") or pyautogui.locateOnScreen("dawn_char_grass_right.PNG") != None:
#         return "dawn"
#     elif pyautogui.locateOnScreen("day_char_grass_down.PNG") or pyautogui.locateOnScreen("day_char_grass_up.PNG") or pyautogui.locateOnScreen("day_char_grass_left.PNG") or pyautogui.locateOnScreen("day_char_grass_right.PNG") != None:
#         return "day"

#Set PP function

def set_pp():
    global pp_dict
    global attack_times
    global selected_move
    selected_move = 0
    attack_times = 0
    for i in range(len(pp_dict)):
        pp = input(f"Give pp value for move {i}(leave empty if you dont use this move)\n")
        if pp == "":
            print("olm")
            continue
        else:
            pp_dict[i] = int(pp)
        print(pp_dict)

#attack function

selected_move = 0
attack_times = 0
pp_dict = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
}

def attack():
    global selected_move
    global attack_times
    global pp_dict
    if pp_dict.get(selected_move) == 0:
        selected_move += 1
    if selected_move > 3:
        print("absolutely no PP left, go to a pokecenter!\n restarting program")
        main()
    if pp_dict.get(selected_move) - attack_times <= 0:
        print("this move has no PP")
        attack_times = 0
        selected_move += 1
    click_key(win_w)
    click_key(win_q)
    click_key(win_z)
    if pp_dict.get(selected_move) == 0:
        selected_move += 1
    if selected_move > 3:
        print("absolutely no PP left, go to a pokecenter!\n restarting program")
        main()
    if selected_move == 0:
        click_key(win_w)
        click_key(win_w)
        attack_times += 1
    elif selected_move == 1:
        click_key(win_d)
        click_key(win_w)
        click_key(win_w)
        attack_times += 1
    elif selected_move == 2:
        click_key(win_s)
        click_key(win_w)
        click_key(win_w)
        attack_times += 1
    elif selected_move == 3:
        click_key(win_s)
        click_key(win_d)
        click_key(win_w)
        click_key(win_w)
        attack_times += 1
    print(f"{attack_times} times attacked")
    time.sleep(3)

#move function

def move():
    print("moving")
    click_key(win_q)
    click_key(win_q)
    click_key(win_d)
    click_key(win_d)
    click_key(win_d)

#main app

def main():
    set_pp()
#    game_time = game_time_check()
#    print(f"In game time: {game_time}")
    print("Starting...\n")
    for i in range(0,5):
        print(i)
        time.sleep(1)
    pyautogui.FAILSAFE = True
    print("Done")
    while True:
        R,G,B = pyautogui.pixel(500, 300)
        if R == 0 and G == 0 and B == 0:
            if pyautogui.locateOnScreen("day_fight.PNG") or pyautogui.locateOnScreen("dawn_fight.PNG") or pyautogui.locateOnScreen("night_fight.PNG") != None:
                time.sleep(0.2)
                attack()
        else:
            move()

#run condition

if __name__ == '__main__':
    main()