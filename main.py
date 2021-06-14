# login form for lottery program #
# calling modules
import datetime
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import *
import rsaidnumber


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

def age_verification():
    # appending text
    f = open("details.txt", "a+")
    f.write(full_name_lbl2.get() + " " + age_lbl.get() + " " + e_address_lbl2.get() + " " + physical_lbl2.get() + " " + "Logged into App at:" + str(now) + "/n")
    f.close()
    try:
        id_number = rsaidnumber.parse(age_lbl.get())
        age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
        if int(age) >= 18:
            messagebox.showinfo("Success", "Let's Play")
        else:
            messagebox.showinfo('Failure', "You Are Too Young To Play")
    except ValueError:
        messagebox.showinfo("Failure", "Please Enter A Valid 13 Digit ID Number")

def clear_input():
    age_lbl.delete(0, END)
    physical_lbl2.delete(0, END)
    e_address_lbl2.delete(0, END)
    full_name_lbl2.delete(0, END)

def exit_program():
    return root.destroy()


# label
entry_age_lbl = Label(root, text="Please Enter Your ID Numbers:", fg="black", bg="#f9db17", font="Consolas 12 bold")
entry_age_lbl.place(x=70, y=200)
full_name_lbl = Label(root, text="Please Enter Your Full Name:", fg="black", bg="#f9db17", font="Consolas 12 bold")
full_name_lbl.place(x=70, y=170)
e_address_lbl = Label(root, text="Please Enter Your Email Address:", fg="black", bg="#f9db17", font="Consolas 12 bold")
e_address_lbl.place(x=70, y=230)
physical_lbl = Label(root, text="Please Enter Your Physical Address:", fg="black", bg="#f9db17", font="Consolas 12 bold")
physical_lbl.place(x=70, y=260)
t_c = Label(root, text="Terms & Conditions:", bg="#f9db17", font="Consolas 12 bold", fg="red")
t_c.place(x=5, y=500)



# entry label
age_lbl = Entry(root)
age_lbl.place(x=450, y=200)
full_name_lbl2 = Entry(root)
full_name_lbl2.place(x=450, y=170)
e_address_lbl2 = Entry(root)
e_address_lbl2.place(x=450, y=230)
physical_lbl2 = Entry(root)
physical_lbl2.place(x=450, y=260)

# buttons
confirm_btn = Button(root, borderwidth="10", text="Verify", font="Consolas 15 bold", fg="white", bg="black", command=age_verification)
confirm_btn.place(x=296, y=320)
clear_btn = Button(root, borderwidth="10", text="Clear", font="Consolas 15 bold", fg="white", bg="black", command=clear_input)
clear_btn.place(x=70, y=320)
exit_btn = Button(root, borderwidth="10", text="Exit", font="Consolas 15 bold", fg="white", bg="black", command=exit_program)
exit_btn.place(x=523, y=320)

# to run the program
root.mainloop()
