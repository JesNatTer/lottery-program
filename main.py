# login form for lottery program #
# calling modules
from tkinter import *
from tkinter import messagebox
from datetime import *
# setup
root = Tk()
# window size
root.geometry('500x500')
# background colour
root.config(bg='#e1ad01')
# window title
root.title("Login")

def age_verification():
    try: # error trapping
        age = int(age_lbl.get())
        if age >= 18:
            messagebox.showinfo("Success", "Welcome To The Lottery Game")
            root.destroy()
            import lotto
        else:
            return messagebox.showinfo("Failure", "You need to be at least 18 to play the game")
    except ValueError: # error trapping
        messagebox.showerror("Invalid input", "Please put Age in numbers.")

def clear_input():
    age_lbl.delete(0, END)

def exit_program():
    return root.destroy()

# label
entry_age_lbl = Label(root, text="Please Enter Your Age:", fg="black", bg="#e1ad01", font="Consolas 12 bold")
entry_age_lbl.place(x=70, y=150)

# entry label
age_lbl = Entry(root)
age_lbl.place(x=300, y=150)

# buttons
confirm_btn = Button(root, borderwidth="10", text="Verify", font="Consolas 15 bold", fg="white", bg="black", command=age_verification)
confirm_btn.place(x=206, y=200)
clear_btn = Button(root, borderwidth="10", text="Clear", font="Consolas 15 bold", fg="white", bg="black", command=clear_input)
clear_btn.place(x=70, y=200)
exit_btn = Button(root, borderwidth="10", text="Exit", font="Consolas 15 bold", fg="white", bg="black", command=exit_program)
exit_btn.place(x=347, y=200)

# to run the program
root.mainloop()
