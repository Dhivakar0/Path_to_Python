from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    generated_password = "".join(password_list)

    password_entry.insert(0,generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'username':username,
            'password':password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!",message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website,message=f"You have entered the below details.\n"
                                                             f"username:{username}\npassword:{password}\nIs it ok to save?")
        if is_ok:
            try:
                # Reading old data in the json file
                with open("password data.json",mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("password data.json","w") as file:
                    json.dump(new_data,file,indent=4)
            else:
            # updating json file with new data
                data.update(new_data)
            # saving new data in the json file
                with open("password data.json","w") as file:
                    json.dump(data,file,indent=4)
            finally:
                website_entry.delete(0,'end')
                password_entry.delete(0,'end')

# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("password data.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="oops",message=f"No details for the {website} exists.")
    else:
        if website in data:
            details = data[website]
            username = details['username']
            password = details['password']
            messagebox.showinfo(title=website, message=f"Username:{username}\nPassword:{password}")
        else:
            messagebox.showinfo(title='oops', message="No Data file found.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry = Entry(width=17)
website_entry.grid(column=1,row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"dhivakar@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(column=1,row=3)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add",width=30,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",command=find_password,width=10)
search_button.grid(column=2,row=1)


window.mainloop()
