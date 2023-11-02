from tkinter import *

base = Tk()
base.geometry('500x500')
base.title("Registration Form")

label_0 = Label(base, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(base, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(base)
entry_1.place(x=240, y=130)

label_2 = Label(base, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)
entry_2 = Entry(base)
entry_2.place(x=240, y=180)

label_3 = Label(base, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(base, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(base, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

label_4 = Label(base, text="Age:", width=20, font=("bold", 10))
label_4.place(x=70, y=280)
entry_3 = Entry(base)
entry_3.place(x=240, y=280)

Button(base, text='Submit', width=20, bg='brown', fg='white').place(x=180, y=380)

# This will display the registration form onto the window
base.mainloop()

print("Registration form is created successfully...")
