import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Do not press this button", width=40)
button.pack(padx=10, pady=10)
clickCount = 0
def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text=f"this is the {clickCount}st time you pressed this button")
    elif clickCount == 2:
        button.configure(text=f"NO BUTTON!")
    elif clickCount == 3:
        button.configure(text="tut tut tut")
    else:
        button.configure(text=f"You clicked this button {clickCount} times!")
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()