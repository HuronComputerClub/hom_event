import sys
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
    def draw_circle(self,x,y,r):
        """draw a circle at point (x,y) with radius r"""
        y = self.height-y
        self.can.create_oval((x-r,y-r,x+r,y+r))
    def write(self,x,y,text,size=20):
        """draw text at a point (x,y)"""
        y = self.height-y
        self.can.create_text((x,y), text=text, anchor=NW, font=("Arial",size))


