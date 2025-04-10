from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if (not website or not email or not password):
        blank = messagebox.showinfo(
            title="Oops", message=f"Please don't leave any blank spots :(")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered:\n\n         Website: {website}\nEmail: {email}\nPassword: {password}\n\nIs it okay to save?")

        if is_ok:
            with open("password.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

canvas = Canvas(height=300, width=300)
logo_img = PhotoImage(file="keys.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, sticky="n")

website_label = Label(text="Website")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password")
password_label.grid(row=3, column=0, sticky="e")

website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
# email_entry.insert(0, "{username@mail.com}")  # Default Email
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")

generate_password_button = Button(
    text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2, sticky="w")
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()
