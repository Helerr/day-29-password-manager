from tkinter import *
from tkinter import messagebox
from random import choice,randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_list = []
    password_list += [choice(letters) for _ in range(randint(8,10))]
    password_list += [choice(symbols) for _ in range(randint(2,4))]
    password_list += [choice(numbers) for _ in range(randint(2,4))]


    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    email = account_input.get()
    password = password_input.get()

    if len(website) > 0 and len(email) > 0 and len(password)>0:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n{email}\n{password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
    else:
        messagebox.askretrycancel(title="Ooops", message="You left some empty fields.\nPlease fill the empty fields "
                                                         "before submitting.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
account_label = Label(text="Email/Username:")
password_label = Label(text="Password")


website_label.grid(row=1, column=0)
account_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_input = Entry(width=52)
account_input = Entry(width=52)
password_input = Entry(width=34)

website_input.focus()
account_input.insert(0, "alex@gmail.com")


website_input.grid(row=1, column=1, columnspan=2)
account_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)


generate_button = Button(text="Generate Password", padx=0, command=generate_password)
generate_button.grid(row=3, column=2)


add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()
