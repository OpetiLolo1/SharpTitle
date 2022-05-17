from tkinter import *

window = Tk()

window.title("a bunch of code")

window.geometry('350x200')

lbl = Label(window, text="Hello scrubs", bg="grey", fg="brown",font=("Arial Bold", 20)  )

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me lol", bg="orange", fg="red",font=("Arial Bold", 15)  )

btn.grid(column=1, row=0)

window.mainloop()