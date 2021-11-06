import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=1000, height=500, bg="white")
canvas.pack()
lastX, lastY = 0,0
colour = "red"
def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y
def on_click(event):
    store_position(event)
def on_drag(event):
    global colour
    canvas.create_line(lastX, lastY, event.x, event.y, fill=colour, width=3)
    store_position(event)
canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)
red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill="blue")
black_id = canvas.create_rectangle(10, 60, 30, 80, fill="black")
white_id = canvas.create_rectangle(10, 85, 30, 105, fill="white")

def colour_event(c):
    def set_colour(event):
        global colour
        colour = c
    return set_colour

canvas.tag_bind(red_id, "<Button-1>", colour_event("red"))
canvas.tag_bind(blue_id, "<Button-1>", colour_event("blue"))
canvas.tag_bind(black_id, "<Button-1>", colour_event("black"))
canvas.tag_bind(white_id, "<Button-1>", colour_event("white"))

window.mainloop()
