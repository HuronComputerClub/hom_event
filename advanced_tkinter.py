#pushing the limits of what the tkinter canvas wrapper can do!

from wrapper import * #import the library

window = create_window()

def len2(s):
    s = hex(s)[2:]
    if len(s) == 1:
        s = "0"+s
    return s

def printkey(key):
    print("pressed",key)
#window.bind_key(printkey)

#Draws a grid of colored squares
def grid():
    for y in range(0,500,10):
        for x in range(0,500,10):
            r=len2(random.randint(0,255))
            b=len2(random.randint(0,255))
            g=len2(random.randint(0,255))
            c = "#"+r+g+b

            window.draw_rectangle(x,y,8,8,c,"")

#draws a color gradient
def gradient():
    for y in range(0,500,3):
        for x in range(0,500,3):
            b=len2(int(y/3.92)+int((500-x)/3.92))
            g=len2(int((500-y)/3.92)+int((x)/3.92))
            r=len2(0)
            
            c = "#"+r+g+b
            
            window.draw_rectangle(x,y,3,3,c,"")

#draws concentric circles
def circles():            
    for rad in range(255,0,-2):
        r=len2(int(255))
        b=len2(int(rad))
        g=len2(int(rad))
        c = "#"+r+g+b
        
##        r = len2(random.randint(0,255))
##        g = len2(random.randint(0,255))
##        b = len2(random.randint(0,255))
##        c = "#"+r+g+b
        
        window.draw_circle(250,250,rad,c,"")

x = 20
def put(letter):
    global x
    window.write(x,250,letter)
    x+=20
def typing():
    window.write(10,250,"|")
    window.bind_key(put)

shade = 0
def change_shade():
    window.bind_key("w",inc_shade)
    window.bind_key("s",dec_shade)
    window.bind_key("c",window.clear)
def inc_shade():
    global shade
    if shade<255:
        shade+=1
    c="#0000"+len2(shade)
    window.draw_rectangle(250,250,400,400,c,"black")
def dec_shade():
    global shade
    if shade>0:
        shade-=1
    c="#0000"+len2(shade)
    window.draw_rectangle(250,250,400,400,c,"black")

def lines():
    for i in range(1000):
        r=len2(random.randint(0,255))
        b=len2(random.randint(0,255))
        g=len2(random.randint(0,255))
        color = "#"+r+g+b
        w=random.randint(0,500)
        x=random.randint(0,500)
        y=random.randint(0,500)
        z=random.randint(0,500)
        window.draw_line(w,x,y,z,color)
lines()
run(window)
