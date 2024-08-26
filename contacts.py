import tkinter as tk
from tkinter import messagebox

class ContactManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.contacts = {}
        self.root.minsize(800,400)
        self.root.configure(bg="#fcf3cf")

        self.frame1 = tk.Frame(self.root,bg="#fcf3cf")
        self.frame1.pack(padx=10,pady=20)
        self.frame2 = tk.Frame(self.root,bg="#fcf3cf")
        self.frame2.pack(padx=10,pady=20)
        self.frame3 = tk.Frame(self.root,bg="#fcf3cf")
        self.frame3.pack(padx=10,pady=20)

        tk.Label(self.frame1, text="Name:",bg="#fcf3cf").pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.pack(side=tk.LEFT)

        tk.Label(self.frame1, text=" Phone Number:",bg="#fcf3cf").pack(side=tk.LEFT)
        self.phone_entry = tk.Entry(self.frame1)
        self.phone_entry.pack(side=tk.LEFT)

        tk.Label(self.frame1, text=" Email:",bg="#fcf3cf").pack(side=tk.LEFT)
        self.email_entry = tk.Entry(self.frame1)
        self.email_entry.pack(side=tk.LEFT)

        tk.Label(self.frame1, text=" Address:",bg="#fcf3cf").pack(side=tk.LEFT)
        self.address_entry = tk.Entry(self.frame1)
        self.address_entry.pack(side=tk.LEFT)

        tk.Button(self.frame2, text="Add Contact", command=self.add_contact,bg="#f4d03f",activebackground="#d4ac0d").pack(side=tk.LEFT,padx=5,pady=5)
        tk.Button(self.frame2, text="View Contact List", command=self.view_contacts,bg="#f4d03f",activebackground="#d4ac0d").pack(side=tk.LEFT,padx=5,pady=5)
        tk.Button(self.frame2, text="Search Contact", command=self.search_contact,bg="#f4d03f",activebackground="#d4ac0d").pack(side=tk.LEFT,padx=5,pady=5)
        tk.Button(self.frame2, text="Update Contact", command=self.update_contact,bg="#f4d03f",activebackground="#d4ac0d").pack(side=tk.LEFT,padx=5,pady=5)
        tk.Button(self.frame2, text="Delete Contact", command=self.delete_contact,bg="#f4d03f",activebackground="#d4ac0d").pack(side=tk.LEFT,padx=5,pady=5)

        self.listbox = tk.Listbox(self.frame3, width=100)
        self.listbox.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.listbox.insert(tk.END, f"{name} -- {phone} -- {email} -- {address}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.listbox.insert(tk.END, f"{name} -- {details['phone']} -- {details['email']} -- {details['address']}")

    def search_contact(self):
        search_term = self.name_entry.get()
        self.listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details["phone"]:
                self.listbox.insert(tk.END, f"{name} -- {details['phone']} -- {details['email']} -- {details['address']}")

    def update_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            name = self.listbox.get(selected_index)
            name = name.split(" -- ")[0]
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address

            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, f"{name} -- {self.contacts[name]['phone']} -- {self.contacts[name]['email']} -- {self.contacts[name]['address']}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            name = self.listbox.get(selected_index)
            name = name.split(" -- ")[0]
            del self.contacts[name]
            self.listbox.delete(selected_index)
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagementSystem(root)
    root.mainloop()