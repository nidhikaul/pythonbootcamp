from tkinter import *
from typing import Text
window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height=300)

#Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


#Buttons

def button_clicked():
    print("I got clicked")
    input2 = input.get()
    my_label["text"] = input2

button = Button(text = "Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text = "Do Not Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
input = Entry(width = 10)
input.grid(column=3, row=2)
    
 
window.mainloop()