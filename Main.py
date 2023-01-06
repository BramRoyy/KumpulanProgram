from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x110")
root.title("JADWAL By Bram")

username = "admin"
password = "admin"

def login():
    user = masuk1.get()
    pas = masuk2.get()

    if(username == user and password == pas):
        messagebox.showinfo("Success", "Selamat Anda Berhasil Login!")
    else:
        messagebox.showwarning("Error", "Maaf Anda Gagal Login!")

# Membuat Label/Judul
label = Label(root, text="Login TEL-U")
label.pack()

# Membuat Kotak Input
masuk1 = Entry(root)
masuk1.pack()
masuk1.insert(0, "Username..")

masuk2 = Entry(root)
masuk2.pack()
masuk2.insert(0, "Password..")

# Membuat Tombol Login
tombol = Button(root, text="Login", command=login)
tombol.pack()

root.mainloop()