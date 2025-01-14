from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
from tkcalendar import DateEntry

db = Database("project.db")
root = Tk()
root.title("Student Details")
root.geometry("1366x700+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = StringVar()
dob = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Students Details", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=5, pady=5, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=5, pady=5, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=20)
txtName.grid(row=1, column=1, padx=5, pady=5, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2, padx=5, pady=5, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=20)
txtAge.grid(row=1, column=3, padx=5, pady=5, sticky="w")

lbldob = Label(entries_frame, text="D.O.B", font=("Calibri", 16), bg="#535c68", fg="white")
lbldob.grid(row=2, column=0, padx=5, pady=5, sticky="w")
txtDob = DateEntry(entries_frame, textvariable=dob, font=("Calibri", 16), width=20, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
txtDob.grid(row=2, column=1, padx=5, pady=5, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=2, padx=5, pady=5, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=20)
txtEmail.grid(row=2, column=3, padx=5, pady=5, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
lblGender.grid(row=3, column=0, padx=5, pady=5, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=18, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=5, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2, padx=5, pady=5, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=20)
txtContact.grid(row=3, column=3, padx=5, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0, padx=5, pady=5, sticky="w")

txtAddress = Text(entries_frame, width=85, height=5, font=("Calibri", 16))
txtAddress.grid(row=5, column=0, columnspan=4, padx=5, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for rows in db.fetch(): 
        cleaned_row = [val.strip() if isinstance(val, str) else val for val in rows]
        tv.insert("", END, values=cleaned_row)

def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return 
    db.insert(txtName.get(),txtAge.get(), txtDob.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()

def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return 
    db.update(row[0],txtName.get(), txtAge.get(), txtDob.get(), txtEmail.get(), comboGender.get(), txtContact.get(),txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()

def delete_employee():
    try:
        if not row:
            messagebox.showerror("Error", "No record selected")
            return

        # Debugging to confirm ID
        print("ID to delete:", row[0])

        db.remove(int(row[0]))  # Convert to int to ensure proper SQL execution
        messagebox.showinfo("Success", "Record Deleted")
        clearAll()
        dispalyAll()
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete record: {e}")

def clearAll():
     name.set("")
     age.set("")
     dob.set("")
     gender.set("")
     email.set("")
     contact.set("")
     txtAddress.delete(1.0, END)

btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9", bd=0).grid(row=0, column=1, padx=5)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",  bd=0).grid(row=0, column=2, padx=5)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#f39c12", bd=0).grid(row=0, column=3, padx=5)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=400, width=1366, height=350)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 16),
                rowheight=25)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.column("2", width=25)
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="D.O.B")
tv.column("4", width=25)
tv.heading("5", text="Email")
tv.column("5", width=100)
tv.heading("6", text="Gender")
tv.column("6", width=15)
tv.heading("7", text="Contact")
tv.column("7", width=20)
tv.heading("8", text="Address")
tv.column("8", width=300)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=BOTH, expand=True)


dispalyAll()
root.mainloop()