#pushing the limits of what the tkinter canvas wrapper can do!

from wrapper import * #import the library

window = create_window()

def len2(s):
    s = hex(s)[2:]
    if len(s) == 1:
        s = "0"+s
    return s
#Draws a grid of colored squares
for y in range(0,500,10):
    for x in range(0,500,10):
        r=len2(random.randint(0,255))
        b=len2(random.randint(0,255))
        g=len2(random.randint(0,255))
        c = "#"+r+g+b

        window.draw_rectangle(x,y,8,8,c,"")

#draws a color gradient       
##for y in range(0,500,3):
##    for x in range(0,500,3):
##        g=len2(int(y/3.92)+int((500-x)/3.92))
##        r=len2(0)
##        b=g
##        
##        c = "#"+r+g+b
##        
##        window.draw_rectangle(x,y,3,3,c,"")

#draws concentric circles
##for rad in range(255,0,-2):
##    r=len2(int(255))
##    b=len2(int(rad))
##    g=len2(int(rad))
##    c = "#"+r+g+b
##    
####    r = len2(random.randint(0,255))
####    g = len2(random.randint(0,255))
####    b = len2(random.randint(0,255))
####    c = "#"+r+g+b
##    
##    window.draw_circle(250,250,rad,c,"")

