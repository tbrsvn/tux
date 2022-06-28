import tkinter as tk
import random
import time
from playsound import playsound


root = tk.Tk()

tux_loc_x=list(range(0, root.winfo_screenwidth()))
tux_loc_y=list(range(0, root.winfo_screenheight()))

# select a color as the transparent color
TRNAS_COLOR = '#abcdef'

tux = int(input("Which size of Tux do you want?\n1. Small\n2. Medium\n3. Large\n4. Extra Large\n"))

if tux == 1:
    root.overrideredirect(1)
    root.attributes('-transparentcolor', TRNAS_COLOR)

    image = tk.PhotoImage(file=r'tux1.png')
    tk.Label(root, image=image, bg=TRNAS_COLOR).pack()

    # support dragging window

    def start_drag(event):
        playsound('click.wav')
        global dx, dy
        dx, dy=event.x, event.y    

    def drag_window(event):
        root.geometry(f'+{event.x_root-dx}+{event.y_root-dy}')
        
    def move(event):
        playsound('move.wav')
        tux_pos_x=random.choice(tux_loc_x)
        tux_pos_y=random.choice(tux_loc_y)
        root.geometry(f'+{tux_pos_x}+{tux_pos_y}')
        
    root.bind('<Button-1>', start_drag)
    root.bind('<B1-Motion>', drag_window)
    root.bind('<Motion>', move)
    root.mainloop()
    
elif tux == 2:
    root.overrideredirect(1)
    root.attributes('-transparentcolor', TRNAS_COLOR)

    image = tk.PhotoImage(file=r'tux2.png')
    tk.Label(root, image=image, bg=TRNAS_COLOR).pack()

    # support dragging window

    def start_drag(event):
        playsound('click.wav')
        global dx, dy
        dx, dy=event.x, event.y

    def drag_window(event):
        root.geometry(f'+{event.x_root-dx}+{event.y_root-dy}')
        
    def move(event):
        playsound('move.wav')
        tux_pos_x=random.choice(tux_loc_x)
        tux_pos_y=random.choice(tux_loc_y)
        root.geometry(f'+{tux_pos_x}+{tux_pos_y}')
        
    root.bind('<Button-1>', start_drag)
    root.bind('<B1-Motion>', drag_window)
    root.bind('<Motion>', move)
    root.mainloop()

elif tux == 69:
    root.overrideredirect(1)
    root.attributes('-transparentcolor', TRNAS_COLOR)

    image = tk.PhotoImage(file=r'tux69.png')
    tk.Label(root, image=image, bg=TRNAS_COLOR).pack()
    
    # support dragging window

    def start_drag(event):
        global dx, dy
        dx, dy=event.x, event.y    

    def drag_window(event):
        root.geometry(f'+{event.x_root-dx}+{event.y_root-dy}')
        
    def move(event):
        playsound('move2.wav')
        
    root.bind('<Button-1>', start_drag)
    root.bind('<B1-Motion>', drag_window)
    root.bind('<space>', move)
    root.mainloop()

    

elif tux == 3:
    root.overrideredirect(1)
    root.attributes('-transparentcolor', TRNAS_COLOR)

    image = tk.PhotoImage(file=r'tux3.png')
    tk.Label(root, image=image, bg=TRNAS_COLOR).pack()

    # support dragging window

    def start_drag(event):
        playsound('click.wav')
        global dx, dy
        dx, dy=event.x, event.y    

    def drag_window(event):
        root.geometry(f'+{event.x_root-dx}+{event.y_root-dy}')
        
    def move(event):
        playsound('move.wav')
        tux_pos_x=random.choice(tux_loc_x)
        tux_pos_y=random.choice(tux_loc_y)
        root.geometry(f'+{tux_pos_x}+{tux_pos_y}')
        
    root.bind('<Button-1>', start_drag)
    root.bind('<B1-Motion>', drag_window)
    root.bind('<Motion>', move)
    root.mainloop()
    
elif tux == 4:
    root.overrideredirect(1)
    root.attributes('-transparentcolor', TRNAS_COLOR)

    image = tk.PhotoImage(file=r'tux4.png')
    tk.Label(root, image=image, bg=TRNAS_COLOR).pack()

    # support dragging window

    def start_drag(event):
        playsound('click.wav')
        global dx, dy
        dx, dy=event.x, event.y    

    def drag_window(event):
        root.geometry(f'+{event.x_root-dx}+{event.y_root-dy}')
        
    def move(event):
        playsound('move.wav')
        tux_pos_x=random.choice(tux_loc_x)
        tux_pos_y=random.choice(tux_loc_y)
        root.geometry(f'+{tux_pos_x}+{tux_pos_y}')
        
    root.bind('<Button-1>', start_drag)
    root.bind('<B1-Motion>', drag_window)
    root.bind('<Motion>', move)
    root.mainloop()