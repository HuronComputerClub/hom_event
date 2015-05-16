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
    root.withdraw()
    win.protocol('WM_DELETE_WINDOW', root.destroy)
    return win

def run(win):
    win.mainloop()

class Window(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.grid()
        self._setup()
    def _setup(self):
        """create a canvas"""
        self.width = 500
        self.height = 500
        self.can = Canvas(self, width=self.width, height = self.height, bg="#ffffff")
        self.can.grid(row = 0, column = 0)
        self.bind("<Key>", self._key)
        self.bindings = {}
        self.idle()
    def idle(self):
        self.after(100, self.idle)
    def _key(self, event):
        import inspect
        funcs = self.bindings.get('', []) + self.bindings.get(event.char, [])
        for i, f in enumerate(funcs):
            try:
                if len(inspect.getargspec(f).args) == 1:
                    f(event.char)
                else:
                    f()
            except Exception as e:
                print('Error in callback #%i: %s' % (i, e))

    def bind_key(self, *args):
        if len(args) == 1 and hasattr(args[0], '__call__'):
            if not '' in self.bindings:
                self.bindings[''] = []
            self.bindings[''].append(args[0])
        elif len(args) == 2 and isinstance(args[0], str) and hasattr(args[1], '__call__'):
            if not args[0] in self.bindings:
                self.bindings[args[0]] = []
            self.bindings[args[0]].append(args[1])
        else:
            raise TypeError('Invalid argument types: %s' % ', '.join(str(type(a)) for a in args))
    def draw_circle(self,x,y,r,color = "",border="black"):
        """draw a circle at point (x,y) with radius r"""
        y = self.height-y
        self.can.create_oval((x-r,y-r,x+r,y+r), fill=color, outline=border)
    def write(self,x,y,text,size=20,color="black"):
        """draw text at a point (x,y)"""
        y = self.height-y
        self.can.create_text((x,y), text=text, anchor=NW, font=("Arial",size), fill=color)
    def draw_rectangle(self, x, y, width, height, color = "", border="black"):
        #ALL QUESTIONABLE STUFF UNDER HERE
        rgb = self.winfo_rgb(color)
        red, green, blue = rgb[0]/256, rgb[1]/256, rgb[2]/256
        def rgb_to_hex(rgb):
            return '#%02x%02x%02x' % rgb
        color = rgb_to_hex((red, green, blue))
        #END OF QUESTIONABLE STUFF
        y = self.height-y
        w = width/2
        h = height/2
        self.can.create_rectangle(x-w,y+h,x+w,y-h,fill=color, outline=border)
    def draw_line(self,x1,y1,x2,y2,color="black"):
        y1 = self.height - y1
        y2 = self.height - y2
        self.can.create_line(x1,y1,x2,y2,fill=color,width=2)
    def clear(self,*args):
        self.can.delete("all")


