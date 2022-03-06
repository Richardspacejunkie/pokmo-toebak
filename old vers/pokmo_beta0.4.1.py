
"""

POKMO_BETA v0.4.1
---------------|
NEW!
- Just, look at the GUI
Changed
- New interface from console based to GUI
---------------|

"""

#libs

import pyautogui
import time
import win32api, win32con
from tkinter import *

#vars

screen_x, screen_y = pyautogui.size()
selected_move = 0
attack_times = 0
pp_dict = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
}

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

#start tk

root = Tk()
icon_img = PhotoImage(file = "icon_logo.png")
root.title("Pokmo beta v0.4.1")
root.iconphoto(False, icon_img)

#pack moves function

def gui_pack_moves():
    global move1_but, move2_but, move3_but, move4_but
    move1_but.grid_forget()
    move2_but.grid_forget()
    move3_but.grid_forget()
    move4_but.grid_forget()
    move1_but = Button(root, text=f"Update move 1 ({str(pp_dict.get(0))})", width=20, command=lambda: gui_set_pp(0))
    move2_but = Button(root, text=f"Update move 2 ({str(pp_dict.get(1))})", width=20, command=lambda: gui_set_pp(1))
    move3_but = Button(root, text=f"Update move 3 ({str(pp_dict.get(2))})", width=20, command=lambda: gui_set_pp(2))
    move4_but = Button(root, text=f"Update move 4 ({str(pp_dict.get(3))})", width=20, command=lambda: gui_set_pp(3))
    move1_but.grid(row=1, column=0)
    move2_but.grid(row=1, column=1)
    move3_but.grid(row=2, column=0)
    move4_but.grid(row=2, column=1)

#gui get pp function

def gui_set_pp(move):
    try:
        pp = int(pp_entry.get())
        pp_dict[move] = int(pp)
        gui_pack_moves()
    except ValueError:
        pass

#attack function

def attack():
    global selected_move
    global attack_times
    global pp_dict
    if pp_dict.get(selected_move) == 0:
        selected_move += 1
    if selected_move > 3:
        start_but = Button(root, text="Program end. Click to restart", command=main, bg="orange", width="40")
        start_but.grid_forget()
        start_but.grid(row=4, column=0, columnspan=2)
        root.update()
        selected_move = 0
        mainloop()
    if pp_dict.get(selected_move) - attack_times <= 0:
        attack_times = 0
        selected_move += 1
        start_but = Button(root, text="no pp", command=main, bg="orange", width="40")
        start_but.grid_forget()
        start_but.grid(row=4, column=0, columnspan=2)
        root.update()
    click_key(win_w)
    click_key(win_q)
    click_key(win_z)
    if pp_dict.get(selected_move) == 0:
        selected_move += 1
    if selected_move > 3:
        start_but = Button(root, text="Program end. Click to restart", command=main, bg="orange", width="40")
        start_but.grid_forget()
        start_but.grid(row=4, column=0, columnspan=2)
        root.update()
        selected_move = 0
        mainloop()
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
    start_but = Button(root, text=f"{attack_times} times attacked", command=main, bg="blue", width="40")
    start_but.grid_forget()
    start_but.grid(row=4, column=0, columnspan=2)
    root.update()
    time.sleep(3)

#move function

def move():
    start_but = Button(root, text="moving", command=main, bg="yellow", width="40")
    start_but.grid_forget()
    start_but.grid(row=4, column=0, columnspan=2)
    root.update()
    click_key(win_q)
    click_key(win_q)
    click_key(win_q)
    click_key(win_d)
    click_key(win_d)
    click_key(win_d)

#main function

def main():
    global screen_x
    global screen_y
    for i in range(0,6):
        start_but = Button(root, text=f"Start({i})", command=main, width="40")
        start_but.grid_forget()
        start_but.grid(row=4, column=0, columnspan=2)
        root.update()
        time.sleep(1)
    pyautogui.FAILSAFE = True
    scan_x = int(0.26 * screen_x)
    scan_y = int(0.27 * screen_y)
    start_but = Button(root, text=f"Start({i})", command=main, bg="green", width="40")
    start_but.grid_forget()
    start_but.grid(row=4, column=0, columnspan=2)
    while True:
        start_but = Button(root, text="Idle...", command=main, bg="white", width="40")
        start_but.grid_forget()
        start_but.grid(row=4, column=0, columnspan=2)
        root.update()
        R,G,B = pyautogui.pixel(scan_x, scan_y)
        if R == 0 and G == 0 and B == 0:
            if pyautogui.locateOnScreen("day_fight.PNG") or pyautogui.locateOnScreen("dawn_fight.PNG") or pyautogui.locateOnScreen("night_fight.PNG") != None:
                time.sleep(0.2)
                attack()
        else:
            move()

#tk stuff

pp_entry = Entry(root, width=40)
pp_entry.grid(row=0, column=0, columnspan=2)

move1_but = Button(root, text=f"Update move 1 ({str(pp_dict.get(0))})", width=20, command=lambda: gui_set_pp(0))
move2_but = Button(root, text=f"Update move 2 ({str(pp_dict.get(1))})", width=20, command=lambda: gui_set_pp(1))
move3_but = Button(root, text=f"Update move 3 ({str(pp_dict.get(2))})", width=20, command=lambda: gui_set_pp(2))
move4_but = Button(root, text=f"Update move 4 ({str(pp_dict.get(3))})", width=20, command=lambda: gui_set_pp(3))

moves = [move1_but, move2_but, move3_but, move4_but]

start_but = Button(root, text="Start", command=main, width=40)
start_but.grid_forget()
start_but.grid(row=4, column=0, columnspan=2)

gui_pack_moves()

root.mainloop()