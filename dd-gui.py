#!/usr/bin/python
# GUI front end to DD disk tool

from Tkinter import *
import tkFileDialog
import subprocess
import signal
import thread
import time

app=Tk()

source = "/dev/sdd"
dest = "backup.img"

def choosesource():
    source = tkFileDialog.askopenfilename()
def choosedest():
    dest = tkFileDialog.askopenfilename()


def StartDD(self):
    print source,dest
    ddproc = subprocess.Popen(['sudo','dd', 'if='+source, 'of='+dest], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
      line = ddproc.stderr.readline()
      if line != '':
        print line.rstrip()
      else:
        break

def startThread():
    thread.start_new_thread(StartDD,("",))


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

button = Button(app,text="Start",command=startThread).grid(row=3,column=2)

mainloop()
