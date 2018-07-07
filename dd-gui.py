#!/usr/bin/python
# GUI front end to DD disk tool

from Tkinter import *
import tkFileDialog
from subprocess import *

import thread

app=Tk()

source = "/dev/mmcblk0"
dest = "~/backup.img"

def choosesource():
    source = tkFileDialog.askopenfilename()
def choosedest():
    dest = tkFileDialog.askopenfilename()


def StartDD():
    ddproc = subprocess.Popen(['dd', 'if='+source, 'of='+dest], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while ddproc.poll() is None:
                        time.sleep(1)
                        ddproc.send_signal(signal.SIGUSR1)
                        while 1:
                                l = ddproc.stderr.readline()
                                if 'records in' in l:
                                        progress = l[:l.index('+')]+' records '
                                if 'bytes' in l:
                                        temp = l.strip()
                                        temp = temp[temp.index('(')+1:temp.index(')')]
                                        status.insert(10, progress+" Copied: "+temp)
                                        break


def StartThread():
    thread.start_new_thread(self.StartDD, (1,))


label = Label(app,text="Read :").grid(row=0,column=0)
entrysrc = Entry(app)
entrysrc.grid(row=0,column=1)
button = Button(app,text="..",command=choosesource).grid(row=0,column=2)

label = Label(app,text="Write:").grid(row=1,column=0)
entrydest = Entry(app)
entrydest.grid(row=1,column=1)
button = Button(app,text="..",command=choosedest).grid(row=1,column=2)


label = Label(app,text="Status:").grid(row=2,column=0)
status = Entry(app)
status.grid(row=2,column=1)

entrysrc.insert(10,source)
entrydest.insert(10,dest)

button = Button(app,text="Start",command=StartThread).grid(row=3,column=2)

mainloop()
