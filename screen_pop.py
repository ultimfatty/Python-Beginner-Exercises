from tkinter import *
window=Tk()
# add widgets here
# this is the button widget
btn = Button(window, text = "This is the blue button", fg = 'blue')
btn.place(x=50, y=100)

# this is the label widget
label = Label(window, text = "This is the label widget", fg = 'red', font = ("Helvetica",18))
label.place(x=150, y=100)

window.title('Hello Python')
window.geometry("500x400+100+100")
window.mainloop()


