import rsaidnumber
from tkinter import *
from tkinter import messagebox
from datetime import *
from datetime import timedelta

root = Tk()
root.geometry('500x500')



def qualify():
    try:
        id_number = rsaidnumber.parse(age_lbl.get())
        age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
        if int(age) >= 18:
            messagebox.showinfo("Success", "Let's Play")
        else:
            messagebox.showinfo('Failure', "You Are Too Young To Play")
    except ValueError:
        messagebox.showinfo("Failure", "Please Enter A Valid 13 Digit ID Number)




age_lbl = Entry(root)
age_lbl.place(x=5, y=5)
age_btn = Button(root, command=qualify, text="Check")
age_btn.place(x=5, y=50)


root.mainloop()
