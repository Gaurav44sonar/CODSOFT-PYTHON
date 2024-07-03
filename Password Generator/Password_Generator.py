from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generatePassword():
    length = int(len_txt.get())
    if len_txt.get() == "" or length<3:
        messagebox.showerror("Invalid Length","Please enter valid length of password")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))

        messagebox.showinfo('Password', "Password="+password, parent=root)
          

root = Tk()

root.title("Password Generator")
root.geometry("400x400+550+150")
root.resizable(False, False)
root.config(background="skyblue")
root.iconbitmap("C:\\My Programs\\CodSoft Tasks\\Python\\Password Generator\\password.ico")

lbl_title = Label(root, text='Password Generator', font=('times new roman', 24, 'bold'), fg='red', bg='white')
lbl_title.place(x=10, y=10, width=380, height=50)

lbl_len = Label(root, text='Enter password length', font=('times new roman', 18, 'bold'), fg='black', bg='skyblue')
lbl_len.place(x=80, y=120, width=250, height=50)

len_txt = ttk.Entry(root, width=22, font=("arial", 18, "bold"), justify="center")
len_txt.place(x=100, y=180, width=200, height=40)

generate_btn = Button(root, text="Generate", command=generatePassword, font=("arial", 18, "bold"), width=20, bg='blue', fg='white')
generate_btn.grid(row=0, column=3, padx=5)
generate_btn.place(x=125, y=260, width=150, height=40)

root.mainloop()


