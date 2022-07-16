from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #list comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_pwd():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
                data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            pwd = data[website]["pwd"]
            messagebox.showinfo(title=website, message=f"Email : {email}\n\n Password : {pwd}\n")
        else:
            messagebox.showinfo(title="Oops", message = f"No details for {website} exists")
        


def save_pwd():
    #Getting the input values
    website = website_input.get()
    email = email_input.get()
    pwd = password_input.get()
    new_data = {
        website:{
            "email": email,
            "pwd": pwd
        }
    }

    if len(website) == 0 & len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f" Confirm\n Email:{email}\n Password:{pwd}\n Save this info?")

        if is_ok:
            #Adding it to a file
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # f.write(f"{website} | {email} | {pwd}\n")
                # f.close()
                #Clearing the inputs on UI
                website_input.delete(0, END)
                # email_input.delete(0, END)
                password_input.delete(0, END)
        

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=mypass_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username", font=("Arial", 10, "bold"))
email_label.grid(column=0, row=2)

website_label = Label(text="Password", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=3)

#Entries
website_input = Entry(width = 40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width = 40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "abc@gmail.com")

password_input = Entry(width = 40)
password_input.grid(column=1, row=3, columnspan=2)

#Buttons
gen_pwd_button = Button(text = "Generate Password", width=14, command=generate_pwd)
gen_pwd_button.grid(column=2, row=3)

add_button = Button(text = "Add", width=35, command = save_pwd)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text = "Search", width=14, command=find_pwd)
search_button.grid(column=2, row=1)

window.mainloop()