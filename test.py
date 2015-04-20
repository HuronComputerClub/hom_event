#This program is a sample which shows off the functions of my Tkinter wrapper
#It makes it extremely easy to draw on a Tkinter canvas

from wrapper import * #import the library

my_window = create_window() #create the window and run __init__

#draw stuff! Things are drawn in a standard xy coordinate plane
my_window.draw_circle(100,300,10)#(x,y,radius)
my_window.draw_circle(200,300,20)
my_window.draw_circle(300,300,30)
my_window.write(200,200,"Hello World")
my_window.write(200,150,"Goodbye World",size=8)
