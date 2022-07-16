from tkinter import *
from typing import Text

def miles_to_kms():
    miles = float(input.get())
    kms = miles * 1.609
    my_label4.config(text=f"{kms}")


window = Tk()
window.title("Mile to Kms Converter")
window.config(padx=20, pady=20)

input = Entry(width = 10)
input.grid(column=1, row=0)

my_label1 = Label(text="Miles", font=("Arial", 24, "bold"))
my_label1.grid(column=2, row=0)

my_label2 = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label2.grid(column=0, row=1)

my_label3 = Label(text="Kms", font=("Arial", 24, "bold"))
my_label3.grid(column=2, row=1)

my_label4 = Label(text="0", font=("Arial", 24, "bold"))
my_label4.grid(column=1, row=1)


button = Button(text = "Calculate", command=miles_to_kms)
button.grid(column=1, row=3)


window.mainloop()