import tkinter as tk
from tkinter import messagebox
import csv
import os

# File name
FILENAME = "contacts.csv"

# Function to save data
def save_contact():
    name = name_var.get()
    email = email_var.get()
    phone = phone_var.get()
    address = address_entry.get("1.0", tk.END).strip()

    if not name or not email or not phone or not address:
        messagebox.showerror("Error", "All fields are required!")
        return

    file_exists = os.path.isfile(FILENAME)

    with open(FILENAME, "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Full Name", "Email", "Phone", "Address"])
        writer.writerow([name, email, phone, address])

    messagebox.showinfo("Success", "Contact saved successfully!")
    clear_fields()

# Function to clear all fields
def clear_fields():
    name_var.set("")
    email_var.set("")
    phone_var.set("")
    address_entry.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Form")

# Variables
name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()

# Labels and Entries
tk.Label(root, text="Full Name").grid(row=0, column=0, padx=10, pady=5, sticky='w')
tk.Entry(root, textvariable=name_var, width=30).grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5, sticky='w')
tk.Entry(root, textvariable=email_var, width=30).grid(row=1, column=1)

tk.Label(root, text="Phone").grid(row=2, column=0, padx=10, pady=5, sticky='w')
tk.Entry(root, textvariable=phone_var, width=30).grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5, sticky='nw')
address_entry = tk.Text(root, width=22, height=4)
address_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Submit", command=save_contact).grid(row=4, column=0, pady=10)
tk.Button(root, text="Clear", command=clear_fields).grid(row=4, column=1)

# Run GUI
root.mainloop()