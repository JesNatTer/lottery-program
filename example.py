from tkinter import *
from tkinter import Listbox
from datetime import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")

# variables
now = datetime.now()
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()


def sel():
    # appending text
    f = open("details.txt", "a+")
    f.write(
        btn1.get() + " " + btn2.get() + " " + btn3.get() + " " + btn4.get() + " " + "Completed at:" + str(now) + "/n")
    f.close()
    selection = "You selected the option " + str(btn1.get())
    label.config(text=selection)

    def bank_number():
    f = open("details.txt", "a+")
    f.write(
        btn1.get() + " " + btn2.get() + " " + btn3.get() + " " + btn4.get() + " " + "Completed at:" + str(now) + "/n")
    f.close()
        try:
            if bank_number != 11:
                messagebox.showinfo("Failure", "Please Enter A 11 Digit Bank Account Number!")
            else:
                messagebox.showinfo("Success", "Please Check Your Email For Further Instructions")
        except ValueError:
            messagebox.showinfo("Invalid", "Please Use Digits Only")


R1 = Radiobutton(root, text="FNB", variable=btn1, value=1, command=sel)
R1.pack(anchor=W)
R2 = Radiobutton(root, text="Absa", variable=btn2, value=2, command=sel)
R2.pack(anchor=W)
R3 = Radiobutton(root, text="Standard Bank", variable=btn3, value=3, command=sel)
R3.pack(anchor=W)
R4 = Radiobutton(root, text="Capiteec", variable=btn4, value=4, command=sel)
R4.pack(anchor=W)
label = Label(root)
label.pack()

banks = {1: "FNB", 2: "Absa", 3: "StandardBank", 4: "Capitec"}
root.mainloop()
