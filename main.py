from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_nums = [random.choice(numbers) for item in range(nr_numbers)]


    password_list = password_letters+password_nums+password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")

    pass_entry.delete(0,END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    print("Saving Details...")

    website = website_entry.get()
    email = email_entry.get()
    passwd = pass_entry.get()

    if len(website) == 0 or len(email) == 0 or len(passwd)==0:
        messagebox.showerror(title="Empty Input", message="Please fill all the fields!!!")
    else:
        isOk = messagebox.askokcancel(title=website, message=f"There are the details entered. \nEmail: {email}\nPassword:{passwd}\nIs it ok to Save?")

        if isOk:
            with open("./data.txt", "a") as file:
                file.write(f"{website} | {email} | {passwd}\n")

            website_entry.delete(0, len(website))
            email_entry.delete(0, len(email))
            pass_entry.delete(0, len(passwd))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# bg image
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=1)

# fields
website_label = Label(text="Website:", padx=5, pady=5)
website_label.grid(column=1, row=2)

website_entry = Entry(width=50)
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", padx=5, pady=5)
email_label.grid(column=1, row=3)

email_entry = Entry(width=50)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "snehalchodankar")

pass_label = Label(text="Password:", padx=5, pady=5)
pass_label.grid(column=1, row=4)

pass_entry = Entry(width=30)
pass_entry.grid(column=2, row=4)

pass_btn = Button(text="Generate Password", command=gen_pass)
pass_btn.grid(column=3, row=4)

add_btn = Button(text="Add", width=41, command=save_details)
add_btn.grid(column=2, row=5, columnspan=2)

window.mainloop()
