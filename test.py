#This program is a sample which shows off the functions of my Tkinter wrapper
#It makes it extremely easy to draw on a Tkinter canvas

from wrapper import * #import the library

my_window = create_window() #create the window and run __init__

#draw stuff! Things are drawn in a standard xy coordinate plane
my_window.write(150,450,"Hello World",size=30)
my_window.write(170,400,"Goodbye World",size=10)

my_window.draw_circle(100,300,10,color="red")#(x,y,radius)
my_window.draw_circle(200,300,20,color="green")
my_window.draw_circle(300,300,30,color="blue")
my_window.draw_circle(400,300,40,color="yellow")

for y in range(10,250,20):
    for x in range(10,500,20):
        my_window.draw_rectangle(x,y,10,10)

run(my_window)
