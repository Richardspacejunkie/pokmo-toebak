
debug_console_message = """

POKMO_BETA v0.6.1
---------------|
NEW!
GUI change
Changed
-debug console
---------------|

"""

print(debug_console_message)

#libs

import pyautogui
import time
import win32api, win32con
import psutil

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import DictProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

print(f"\n-imported libs")

#configuring kivy

Config.set('graphics', 'resizable', False)
Config.write()
Builder.load_file("design.kv")

print(f"\n-configured kivy")

#vars

screen_x, screen_y = pyautogui.size()
selected_move = 0
attack_times = 0
pp_dict = {
    0: "",
    1: "",
    2: "",
    3: ""
}

print(f"\n-set vars")

#win32api key values

win_w = 0x57
win_s = 0x53
win_q = 0x51
win_d = 0x44
win_z = 0x5A

print(f"\n-set key values")

#setting up grid layout

class MyGridLayout(Widget):
    global pp_dict

    move_pp = DictProperty(pp_dict)

    move1_value = ObjectProperty(None)
    move2_value = ObjectProperty(None)
    move3_value = ObjectProperty(None)
    move4_value = ObjectProperty(None)


    def update(self):
        global pp_dict

        pp_dict[0] = self.move1_value.text
        pp_dict[1] = self.move2_value.text
        pp_dict[2] = self.move3_value.text
        pp_dict[3] = self.move4_value.text

        self.move1_value.text = pp_dict[0]
        self.move2_value.text = pp_dict[1]
        self.move3_value.text = pp_dict[2]
        self.move4_value.text = pp_dict[3]

        self.move_pp[0] = pp_dict[0]
        self.move_pp[1] = pp_dict[1]
        self.move_pp[2] = pp_dict[2]
        self.move_pp[3] = pp_dict[3]

        print(pp_dict)

print(f"\n-setup grid layout")

#declaring kivy app

class PokmoApp(App):
    def build(self):
        Window.size = (260, 330)
        return MyGridLayout()

print(f"\n-declared kivy app")

#win api key click function

def click_key(x):
    win32api.keybd_event(x,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(x,0,win32con.KEYEVENTF_KEYUP,0)

print(f"\n-setup win32 api function")

print(f"\n-setup get pp function")

#attack function

def attack():
    global selected_move
    global attack_times
    global pp_dict
    if pp_dict.get(selected_move) == 0:
        print("next move")
        selected_move += 1
    if selected_move > 3:
        print("out of pp")
        selected_move = 0
        main()
    if pp_dict.get(selected_move) - attack_times <= 0:
        print("no pp")
        attack_times = 0
        selected_move += 1
    click_key(win_w)
    click_key(win_q)
    click_key(win_z)
    if selected_move == 0:
        print("attack move 1")
        click_key(win_w)
        click_key(win_w)
        attack_times += 1
    elif selected_move == 1:
        print("attack move 2")
        click_key(win_d)
        click_key(win_w)
        click_key(win_w)
        attack_times += 1
    elif selected_move == 2:
        print("attack move 3")
        click_key(win_s)
        click_key(win_w)
        click_key(win_w)
        attack_times += 1
    elif selected_move == 3:
        print("attack move 4")
        click_key(win_s)
        click_key(win_d)
        click_key(win_w)
        click_key(win_w)
        attack_times += 1
    time.sleep(3)

print(f"\n-setup attack function")

#move function

def move():
    click_key(win_q)
    click_key(win_q)
    click_key(win_q)
    click_key(win_d)
    click_key(win_d)
    click_key(win_d)

print(f"\n-setup move function")

#main function

def main():
    global screen_x
    global screen_y
    print("starting countdown")
    for i in range(0,6):
        time.sleep(5-i)
    pyautogui.FAILSAFE = True
    scan_x = int(0.26 * screen_x)
    scan_y = int(0.27 * screen_y)
    print("entered loop")
    while True:
        R,G,B = pyautogui.pixel(scan_x, scan_y)
        if R == 0 and G == 0 and B == 0:
            print("combat mode")
            if pyautogui.locateOnScreen("fight.PNG", confidence=(0.8)) != None:
                print("attack")
                time.sleep(0.2)
                attack()
        else:
            print("move")
            move()

print(f"\n-setup main function")

if __name__ == '__main__':
    PokmoApp().run()

# print("PokeMMO.exe" in (i.name() for i in psutil.process_iter()))