
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
from threading import Thread

from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.write()

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import DictProperty
from kivy.lang import Builder
from kivy.core.window import Window


print(f"\n-imported libs")

#configuring kivy

Builder.load_file("design.kv")

print(f"\n-configured kivy")

#setting up grid layout class

class MyGridLayout(Widget):
    
    #vars

    active_thread = False
    screen_x, screen_y = pyautogui.size()
    selected_move = 0
    attack_times = 0
    pp_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0
    }

    print(f"\n-set vars")

    #script thread object
    class Script(Thread):

        #win32api key values

        win_w = 0x57
        win_s = 0x53
        win_q = 0x51
        win_d = 0x44
        win_z = 0x5A

        print(f"\n-set key values")
        
        #win api key click function

        def click_key(self, x):
            win32api.keybd_event(x,0,0,0)
            time.sleep(0.1)
            win32api.keybd_event(x,0,win32con.KEYEVENTF_KEYUP,0)

        print(f"\n-setup win32 api function")

        def selected_move_update(self):
            print(MyGridLayout.pp_dict)
            if MyGridLayout.pp_dict[MyGridLayout.selected_move] - MyGridLayout.attack_times == 0:
                MyGridLayout.attack_times = 0
                MyGridLayout.pp_dict[MyGridLayout.selected_move] = 0
            if MyGridLayout.selected_move > 3:
                print("out of range moves")
                MyGridLayout.selected_move = 0
            if MyGridLayout.pp_dict[0] == 0 and MyGridLayout.pp_dict[1] == 0 and MyGridLayout.pp_dict[2] == 0 and MyGridLayout.pp_dict[3] == 0:
                print("no pp")
                return "no pp"
            if MyGridLayout.pp_dict[MyGridLayout.selected_move] == 0:
                print("empty selecting next move")
                MyGridLayout.selected_move += 1
            if MyGridLayout.selected_move > 3:
                MyGridLayout.selected_move = 0

        #attack function

        def attack(self):
            self.click_key(self.win_w)
            self.click_key(self.win_q)
            self.click_key(self.win_z)
            if MyGridLayout.selected_move == 0:
                print("attack move 1")
                self.click_key(self.win_w)
                self.click_key(self.win_w)
                MyGridLayout.attack_times += 1
            elif MyGridLayout.selected_move == 1:
                print("attack move 2")
                self.click_key(self.win_d)
                self.click_key(self.win_w)
                self.click_key(self.win_w)
                MyGridLayout.attack_times += 1
            elif MyGridLayout.selected_move == 2:
                print("attack move 3")
                self.click_key(self.win_s)
                self.click_key(self.win_w)
                self.click_key(self.win_w)
                MyGridLayout.attack_times += 1
            elif MyGridLayout.selected_move == 3:
                print("attack move 4")
                self.click_key(self.win_s)
                self.click_key(self.win_d)
                self.click_key(self.win_w)
                self.click_key(self.win_w)
                MyGridLayout.attack_times += 1
            time.sleep(3.5)

        print(f"\n-setup attack function")

        #move function

        def move(self):
            self.click_key(self.win_q)
            self.click_key(self.win_q)
            self.click_key(self.win_q)
            self.click_key(self.win_d)
            self.click_key(self.win_d)
            self.click_key(self.win_d)

        print(f"\n-setup move function")


        #main function

        def run(self):
            time.sleep(5)
            print("running main")
            pyautogui.FAILSAFE = True
            scan_x = int(0.26 * MyGridLayout.screen_x)
            scan_y = int(0.27 * MyGridLayout.screen_y)
            print("entered loop")
            looping = True
            while looping:
                if MyGridLayout.active_thread == False:
                    print("killing thread")
                    break
                R,G,B = pyautogui.pixel(scan_x, scan_y)
                if self.selected_move_update() == "no pp":
                    print("quitting no pp")
                    looping = False
                elif R == 0 and G == 0 and B == 0:
                    print("combat mode")
                    if pyautogui.locateOnScreen("fight.PNG", confidence=(0.8)) != None:
                        self.selected_move_update()
                        print("attack")
                        self.attack()
                else:
                    print("move")
                    self.move()
            print("stopping")
            MyGridLayout.active_thread = False

        print(f"\n-setup run function")

    print(f"\n-setup Script")

    #start/threading function

    def start(self):
        if MyGridLayout.active_thread:
            print("Thread already running")
            print("Stoping thread")
            for i in self.pp_dict:
                self.pp_dict[i] = 0
            self.selected_move = 0
            self.attack_times = 0
            MyGridLayout.active_thread = False
            self.ids.start_button.background_color = 1, 1, 1, 1
            self.ids.start_button.text = "Start"
        else:
            MyGridLayout.active_thread = True
            self.selected_move = 0
            self.attack_times = 0
            print("starting countdown")
            self.ids.start_button.background_color = 0, 1, 0, 1
            self.ids.start_button.text = "Running ... (click to stop)"
            poke_script = self.Script()
            poke_script.start()
        print(MyGridLayout.active_thread)

    #object values

    move_pp = DictProperty(pp_dict)

    move1_value = ObjectProperty(None)
    move2_value = ObjectProperty(None)
    move3_value = ObjectProperty(None)
    move4_value = ObjectProperty(None)

    print(f"\n-set object values")

    def update(self):
        if self.move1_value.text == "":
            self.pp_dict[0] = 0
        else:
            self.pp_dict[0] = int(self.move1_value.text)
        if self.move2_value.text == "":
            self.pp_dict[1] = 0
        else:
            self.pp_dict[1] = int(self.move2_value.text)
        if self.move3_value.text == "":
            self.pp_dict[2] = 0
        else:
            self.pp_dict[2] = int(self.move3_value.text)
        if self.move4_value.text == "":
            self.pp_dict[3] = 0
        else:
            self.pp_dict[3] = int(self.move4_value.text)

        self.move1_value.text = str(self.pp_dict[0])
        self.move2_value.text = str(self.pp_dict[1])
        self.move3_value.text = str(self.pp_dict[2])
        self.move4_value.text = str(self.pp_dict[3])

        self.move_pp[0] = str(self.pp_dict[0])
        self.move_pp[1] = str(self.pp_dict[1])
        self.move_pp[2] = str(self.pp_dict[2])
        self.move_pp[3] = str(self.pp_dict[3])

        print(self.pp_dict)

print(f"\n-setup grid layout")

#declaring kivy app

class PokmoApp(App):
    def build(self):
        self.icon = "icon_logo.png"
        Window.size = (260, 330)
        return MyGridLayout()

print(f"\n-declared kivy app")

if __name__ == '__main__':
    PokmoApp().run()

# print("PokeMMO.exe" in (i.name() for i in psutil.process_iter()))