# login form for lottery program #
# calling modules
import datetime
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import *
import rsaidnumber
import re
from playsound import playsound

# regular expression for validating email
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# setup
root = Tk()
# window size
root.geometry('800x600')
# background colour
root.config(bg='#f9db17')
# window title
root.title("Login")
# variables
now = datetime.now()

# for an image
canvas = Canvas(root, width=500, height=200, bg='#f9db17', borderwidth=0, highlightthickness=0)
canvas.place(x=135, y=5)
img = ImageTk.PhotoImage(Image.open('./Images/ITHUBA-NATIONAL-LOTTERY.png'))
canvas.create_image(20, 20, anchor=NW, image=img)


class AgeAndSound:
    def __init__(self, master):
        # label
        self.entry_age_lbl = Label(master, text="Please Enter Your ID Number:", fg="black", bg="#f9db17",
                                   font="Consolas 12 bold")
        self.entry_age_lbl.place(x=70, y=200)
        self.full_name_lbl = Label(master, text="Please Enter Your Full Name:", fg="black", bg="#f9db17",
                                   font="Consolas 12 bold")
        self.full_name_lbl.place(x=70, y=170)
        self.e_address_lbl = Label(master, text="Please Enter Your Email Address:", fg="black", bg="#f9db17",
                                   font="Consolas 12 bold")
        self.e_address_lbl.place(x=70, y=230)
        self.physical_lbl = Label(master, text="Please Enter Your Physical Address:", fg="black", bg="#f9db17",
                                  font="Consolas 12 bold")
        self.physical_lbl.place(x=70, y=260)
        self.t_c = Label(master, text="Terms & Conditions:", bg="#f9db17", font="Consolas 12 bold", fg="red")
        self.t_c.place(x=5, y=500)
        self.legal_age = Label(master, text="1. You Must Be 18 Years or Older To Enter", bg="#f9db17", fg="black",
                               font="Consolas 8 bold")
        self.legal_age.place(x=5, y=530)
        self.legal_age2 = Label(master, text="2. You Must Have A Valid ID", bg="#f9db17", fg="black",
                                font="Consolas 8 bold")
        self.legal_age2.place(x=5, y=550)
        self.legal_age3 = Label(master, text="3. User Must Be A SA Citizen", bg="#f9db17", fg="black",
                                font="Consolas 8 bold")
        self.legal_age3.place(x=5, y=570)
        # entry label
        self.age_lbl = Entry(master)
        self.age_lbl.place(x=450, y=200)
        self.full_name_lbl2 = Entry(master)
        self.full_name_lbl2.place(x=450, y=170)
        self.e_address_lbl2 = Entry(master)
        self.e_address_lbl2.place(x=450, y=230)
        self.physical_lbl2 = Entry(master)
        self.physical_lbl2.place(x=450, y=260)

        # buttons
        self.confirm_btn = Button(master, borderwidth="10", text="Verify", font="Consolas 15 bold", fg="white", bg="black", command=self.age_verification)
        self.confirm_btn.place(x=296, y=320)
        self.clear_btn = Button(master, borderwidth="10", text="Clear", font="Consolas 15 bold", fg="white", bg="black", command=self.clear_input)
        self.clear_btn.place(x=70, y=320)
        self.exit_btn = Button(master, borderwidth="10", text="Exit", font="Consolas 15 bold", fg="white", bg="black", command=self.exit_program)
        self.exit_btn.place(x=523, y=320)

    def age_verification(self):
        # appending text
        f = open("details.txt", "a+")
        f.write(
            self.full_name_lbl2.get() + " " + self.age_lbl.get() + " " + self.e_address_lbl2.get() + " " + self.physical_lbl2.get() + " " + "Logged into App at:" + str(
                now) + "/n")
        f.close()
        playsound("./Audio/lotto-sound.mp3")
        try:
            id_number = rsaidnumber.parse(self.age_lbl.get())
            age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
            if int(age) >= 18:
                messagebox.showinfo("Success", "Let's Play")
                root.destroy()
                import lotto
            else:
                messagebox.showinfo('Failure', "You Are Too Young To Play")
        except ValueError:
            messagebox.showinfo("Failure", "Please Enter A Valid 13 Digit ID Number")
        email = self.e_address_lbl2.get()
        if re.search(regex, email):
            messagebox.showinfo("Success", "Valid Email")
        else:
            messagebox.showinfo("Failure", "Invalid Email")

    def clear_input(self):
        self.age_lbl.delete(0, END)
        self.physical_lbl2.delete(0, END)
        self.e_address_lbl2.delete(0, END)
        self.full_name_lbl2.delete(0, END)
    def exit_program(self):
        return root.destroy()




AgeAndSound(root)
# to run the program
root.mainloop()
