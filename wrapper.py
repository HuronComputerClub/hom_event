import sys, random
if sys.version.startswith('2'):
    from tkMessageBox import *
    from Tkinter import *
    import Tkinter as tk
else:
    from tkinter.messagebox import *
    from tkinter import *
    import tkinter as tk

def create_window():
    root = Tk()
    root.title("Python Canvas")
    win = Window(root)
    return win

def run(win):
    win.mainloop()

class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self._setup()
    def _setup(self):
        """create a canvas"""
        self.width = 500
        self.height = 500
        self.can = Canvas(self, width=self.width, height = self.height, bg="#ffffff")
        self.can.grid(row = 0, column = 0)
        self.bind("<Key>", self._key)
    def _key(self, event):
        print ("pressed", repr(event.char))
    def draw_circle(self,x,y,r,color = "",border="black"):
        """draw a circle at point (x,y) with radius r"""
        y = self.height-y
        self.can.create_oval((x-r,y-r,x+r,y+r), fill=color, outline=border)
    def write(self,x,y,text,size=20,color="black"):
        """draw text at a point (x,y)"""
        y = self.height-y
        self.can.create_text((x,y), text=text, anchor=NW, font=("Arial",size), fill=color)
    def draw_rectangle(self, x, y, width, height, color = "", border="black"):
        y = self.height-y
        w = width/2
        h = height/2
        self.can.create_rectangle(x-w,y+h,x+w,y-h,fill=color, outline=border)


