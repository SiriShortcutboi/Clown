#Holden Anderson
#Alarm Clock
#9-21

#imports
import Alarm
import winsound
import datetime
import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
#timezones
GMT = 0
ECT = 1
EET = 2
ART = 3
NET = 4
PLT = 5
BST = 6
VST = 7
CTT = 8
JST = 9
AET = 10
SST = 11
NST = 12
MIT = -11
HST = -10
AST = -9
PST = -8
MST = -7
CST = -6
EST = -5
PRT = -4
CNT = -3
CAT = -1
dls = 1

#defining  variables
def gmtimenow(timeZone,dls):
    #calculate the current time from unix epoch down to the second
    seconds = calendar.timegm(time.gmtime())
    current_second = seconds % 60
    minutes = seconds//60
    current_min = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24

#set timezone
    current_hour = current_hour = timeZone+dls


    if current_hour >24:
        current_hour-=24

#converting to 12 hour cycle

    if current_hour >= 12:
        tag = " PM"
    else:
        tag = " AM"
    if current_hour > 12:
        current_hour -= 12

#set alarm
    a_hour,a_minute,a_seconds = time_input()
    if current_hour == a_hour and current_min == a_minute and current_second == a_seconds and tag == a_tag:
        alarm.Alarm()
        

#formatting the time output
    if current_hour < 10:
        current_hour = "0"+str(current_hour)
    else:
        current_hour=str(current_hour)
    if current_min <10:
        current_min="0"+str(current_min)
    else:
        current_min = str(current_min)
    if current_second < 10:
        current_second="0"+str(current_second)
    else:
        current_second = str(current_second)

    #display the time
    current_time = current_time = current_hour +":"+current_min+":"+current_second+tag
    return current_time

def show_time():
    time = gmtimenow(MST,dls)
    txt.set(time)
    root.after(1000, show_time)
    
    
    root.after(1000,show_time)
def quit(*args):
    root.destroy()


def time_input():
    a_hour = 9
    a_minute = 45
    a_seconds = 00
    a_tag = "AM"
    return (a_hour,a_minute,a_seconds)


#creating GUI
root = Tk()
root.attributes("-fullscreen",False)
root.configure(background = 'purple')
root.bind("x",quit)
root.after(1000,show_time)
fnt = font.Font(family = 'Century Gothic', size = 60, weight = "normal")
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt,font=fnt,foreground="aqua",background="pink")
lbl.place(relx=.5,rely=.5,anchor=CENTER)
root.mainloop()


                
