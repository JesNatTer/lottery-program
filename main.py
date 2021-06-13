# calling modules
from tkinter import *
from tkinter import messagebox
from datetime import *
# login form for lottery
# setup
root = Tk()
# window size
root.geometry('300x150')
# background colour
root.config(bg='#e1ad01')
# window title
root.title("Login")

def age_verification():
    try: # error trapping
        age = int(age_lbl.get())
        if age >= 18:
            messagebox.showinfo("Success", "Welcome To The Lotto Program")
            root.destroy()
            import lotto

        else:
           return messagebox.showinfo("Failure", "You need to be at least 18 to play the game")
    except ValueError: # error trapping
        messagebox.showerror("Invalid input", "Please put Age in numbers.")

# label
entry_age_lbl = Label(root, text="Please Enter Your Age Below:", fg="white", bg="black")
entry_age_lbl.place(x=80, y=5)

# entry label
age_lbl = Entry(root, text="YYYY/MM/DD")
age_lbl.place(x=95, y=30)

# button
confirm_btn = Button(root, borderwidth="10", text="Verify Age", font="Consolas 15 bold", fg="white", bg="black", command=age_verification)
confirm_btn.place(x=85, y=55)

# to run the program
root.mainloop()
