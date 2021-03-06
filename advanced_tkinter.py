#pushing the limits of what the tkinter canvas wrapper can do!

from wrapper import * #import the library

window = create_window()

def printkey(key):
    print("pressed",key)
#window.bind_key(printkey)

#Draws a grid of colored squares
def grid():
    for y in range(0,500,10):
        for x in range(0,500,10):
            r=random.randint(0,255)
            b=random.randint(0,255)
            g=random.randint(0,255)

            window.draw_rectangle(x,y,8,8,(r,g,b),"")

#draws a color gradient
def gradient():
    for y in range(0,500,3):
        for x in range(0,500,3):
            b=int(y/3.92)+int((500-x)/3.92)
            g=int((500-y)/3.92)+int((x)/3.92)
            r=0
            
            window.draw_rectangle(x,y,4,4,(r,g,b),"")

#draws concentric circles
def circles():
    for rad in range(255,0,-2):
        r=255
        b=rad
        g=rad
        
        window.draw_circle(250,250,rad,(r,g,b),"")

#types on the canvas
x = 20
def put(letter):
    global x
    window.write(x,250,letter)
    x+=20
def typing():
    window.write(10,250,"|")
    window.bind_key(put)

#change the color of a square with w and s
shade = 0
def change_shade():
    window.bind_key("w",inc_shade)
    window.bind_key("s",dec_shade)
    window.bind_key("c",window.clear)
def inc_shade():
    global shade
    if shade<254:
        shade+=2
    window.draw_rectangle(250,250,400,400,(0,0,shade),"black")
def dec_shade():
    global shade
    if shade>1:
        shade-=2
    window.draw_rectangle(250,250,400,400,(0,0,shade),"black")

#draw a bunch of random lines
def lines():
    for i in range(500):
        r=random.randint(0,255)
        b=random.randint(0,255)
        g=random.randint(0,255)

        w=random.randint(0,500)
        x=random.randint(0,500)
        y=random.randint(0,500)
        z=random.randint(0,500)
        window.draw_line(w,x,y,z,(r,g,b))

#move a square with wasd
mv_x = 250
mv_y = 250
def mv_draw():
    global mv_x
    global mv_y
    window.clear()
    window.draw_rectangle(mv_x,mv_y,20,20,"red","black")
def move():
    window.bind_key("w",mv_u)
    window.bind_key("a",mv_l)
    window.bind_key("s",mv_d)
    window.bind_key("d",mv_r)
    mv_draw()
def mv_u():
    global mv_y
    mv_y+=3
    mv_draw()
def mv_d():
    global mv_y
    mv_y-=3
    mv_draw()
def mv_l():
    global mv_x
    mv_x-=3
    mv_draw()
def mv_r():
    global mv_x
    mv_x+=3
    mv_draw()
    
gradient()
run(window)
