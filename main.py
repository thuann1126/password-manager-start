import random
from tkinter import *
import json
import pyperclip
import messagebox #used for showing the message

#json.dump (write the data)
#json.load (write the data)
#json.update (write the data)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Initialize variable for saving credentials
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)

    #join() function join the elements in the list or dict with the joined string
    password = "".join(password_list)
    #insert function, the beginning index, the string want to insert
    password_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveData():
    website = website_box.get()
    email = username_box.get()
    password = password_box.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title="Ops!", message="Please make sure you have not left any fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                # load the file
                data = json.load(data_file)


        except FileNotFoundError:
            # create a new file if it is not found
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # update the file
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_box.delete(0, END)
            password_box.delete(0, END)

# ---------------------------- SEARCH ENGINE ------------------------------- #


def searchData():
    website = website_box.get()
    with open("data.json", "r") as data_file:
        data_dict = json.load(data_file)

        if website in data_dict:
            email = data_dict[website]["email"]
            password = data_dict[website]["password"]
            messagebox.showinfo(title="Credential", message=f"Your email: {email} \n Your password: {password}")
        else:
            messagebox.showinfo(title="Opps!~", message="Can not find your data")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
# Image
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", highlightthickness=0)
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username", highlightthickness=0)
username_label.grid(column=0, row=2)
password_label = Label(text="Password", highlightthickness=0)
password_label.grid(column=0, row=3)

website_box = Entry( highlightthickness=0, width=19)
website_box.grid(column=1, row=1)
username_box = Entry( highlightthickness=0, width=38)
username_box.grid(column=1, row=2, columnspan=2)
password_box = Entry( highlightthickness=0, width=38)
password_box.grid(column=1, row=3, columnspan=2)

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=33, command=saveData)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", highlightthickness=0,width=15, command=searchData)
search_button.grid(column=2, row=1)


window.mainloop()