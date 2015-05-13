#pushing the limits of what the tkinter canvas wrapper can do!

from wrapper import * #import the library

window = create_window()

for y in range(10,500,20):
    for x in range(10,500,20):
        r = random.randint(16,255)
        g = random.randint(16,255)
        b = random.randint(16,255)

        c = "#"+hex(r)[2:]+hex(g)[2:]+hex(b)[2:]

        window.draw_rectangle(x,y,10,10,c)
