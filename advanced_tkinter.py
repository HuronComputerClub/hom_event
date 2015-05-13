#pushing the limits of what the tkinter canvas wrapper can do!

from wrapper import * #import the library

window = create_window()

def len2(s):
    s = hex(s)[2:]
    if len(s) == 1:
        s = "0"+s
    return s

##for y in range(10,500,10):
##    for x in range(10,500,10):
##        r = random.randint(16,255)
##        g = random.randint(16,255)
##        b = random.randint(16,255)
##
##        c = "#"+hex(r)[2:]+hex(g)[2:]+hex(b)[2:]
##
##        window.draw_rectangle(x,y,10,10,c)
       
for y in range(0,500,3):
    for x in range(0,500,3):
        b=len2(int(y/4)+int((500-x)/4))
        r=len2(0)
        g=len2(0)
        
        c = "#"+r+g+b
        
        window.draw_rectangle(x,y,3,3,c)



