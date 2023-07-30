from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyclip

# PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyclip.copy(password)

# SAVE PASSWORD
def save():
    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Missing Info", message="Field Empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Site Info: \nEmail: {email}\nPassword: {password}\nSave?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)

# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(width=200, height=200, padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ", bg="white")
website_label.grid(column=0, row=1)
email_user_label = Label(text="Email/Username: ", bg="white")
email_user_label.grid(column=0, row=2)
password_label = Label(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

# Inputs
website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_user_input = Entry(width=52)
email_user_input.grid(column=1, row=2, columnspan=2)

with open("default_email.txt") as data:
    lines = 0
    content = data.readlines()
    for i in content:
        if i:
            lines += 1
    if lines == 2:
        default_email = content[1]
    else:
        default_email = ""
email_user_input.insert(0, default_email)

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", bg="white", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)









window.mainloop()
