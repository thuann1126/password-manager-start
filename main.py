from tkinter import *
import json

#json.dump (write the data)
#json.load (write the data)
#json.update (write the data)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Initialize variable for saving credentials


# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)


def saveData():
    website = website_box.get()
    email = username_box.get()
    password = password_box.get()

    new_data = {
        "website": website,
        "email": email,
        "password": password
    }
    try:
        with open("data.json", "r") as data_file:
            # load the file
            data = json.load(data_file)
            # update the file
            data.update(new_data)

    except FileNotFoundError:
        # create a new file if it is not found
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)


        website_box.delete(0, END)
        password_box.delete(0, END)


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

website_box = Entry( highlightthickness=0, width=38)
website_box.grid(column=1, row=1, columnspan=2)
username_box = Entry( highlightthickness=0, width=38)
username_box.grid(column=1, row=2, columnspan=2)
password_box = Entry( highlightthickness=0, width=38)
password_box.grid(column=1, row=3, columnspan=2)

generate_button = Button(text="Generate Password", highlightthickness=0)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=33, command=saveData)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()