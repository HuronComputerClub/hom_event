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
        self.can = Canvas(self, width=500, height = 500, bg="#ffffff")
        self.can.grid(row = 0, column = 0)
    def draw_circle(self,x,y,r):
        """draw a circle a circle"""
        self.can.create_oval((x-r,y-r,x+r,y+r))


