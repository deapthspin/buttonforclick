from tkinter import *
import pyautogui
import sys




def go():
    x = 0
    while x < 5:
        pyautogui.click(clicks=100000, interval= 0.0001)
        pyautogui.doubleClick()
        pyautogui.tripleClick()
        if stop == True:
            break
        


def stop():
    exit()
    
      

root = Tk()
Speed = Entry(root, width=20)
Interval = Entry(root, width=20)
autoclick = Button(root, text='go', command=go)
stop = Button(root, text='stop', command=stop)
autoclick.pack()
stop.pack()
Speed.pack()
Interval.pack()



root.mainloop()
