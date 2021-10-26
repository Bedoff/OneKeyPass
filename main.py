from os import read
import time
import pyautogui
import ctypes
import tkinter
import tkinter as tk
from win10toast import ToastNotifier
import App
import secure

try:
    f = open("password.txt")
except IOError:
    App.passwin()

with open('password.txt', 'r') as file:
    password = file.read().replace('\n', '')


def get_capslock_state():
    hllDll1 = ctypes.WinDLL ("User32.dll")
    VK_NUMLOCK = 0x90
    return hllDll1.GetKeyState(VK_NUMLOCK)

def get_END_state():
    hllDll2 = ctypes.WinDLL ("User32.dll")
    VK_END = 0x23
    return hllDll2.GetKeyState(VK_END)

if get_END_state==1:
    pyautogui.press('END')


while True:
    time.sleep(1)
    if(get_capslock_state()==0):
        toaster = ToastNotifier()
        toaster.show_toast("OneKeyPass İs Ready","Be careful")
        while True:
            if(get_END_state()==1):
                pyautogui.typewrite(secure.decode(password))
                pyautogui.press('END')
                break
   
