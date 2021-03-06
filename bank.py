from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox
from playsound import playsound
import smtplib
from main import return_email
# setting up the window
root = Tk()
root.geometry("500x500")  # window size
root.title("Banking Details")  # window title
root.config(bg="#f9db17")

emails_id = return_email


# bank function
def bank_number():
    try:
        bank_num = acc_num_entry.get()
        branch = branch_num_entry.get()
        if len(bank_num) == 11 and len(branch) == 6:
            f = open("details.txt", "a+")
            f.write(
                acc_num_entry.get() + " " + acc_num_entry.get() + " " + branch_num_entry.get() + " " + combo_box_banks.get() + "\n")
            f.close()
            # creates SMTP session
            import smtplib
            s = smtplib.SMTP('smtp.gmail.com', 587)
            sender_email_id = 'jeandre.lotto@gmail.com'
            receiver_email_id = emails_id
            password = "lifechoices2021"
            # start TLS for security
            s.starttls()
            # Authentication
            s.login(sender_email_id, password)
            # message to be sent
            message = "Congratulations\n"
            message = message + "How was your saturday"
            # sending the mail
            s.sendmail(sender_email_id, receiver_email_id, message)
            # terminating the session
            s.quit()
            playsound("./Audio/submit.mp3")
            messagebox.showinfo("Success", "Please Check Your Email For Further Instructions")
        else:
            messagebox.showinfo("Failure", "Please Enter A 11 Digit Bank Account Number and A 6 Digit Branch Code")
    except ValueError:
        messagebox.showinfo("Invalid", "Please Use Digits Only")


#     # send email function
# def send_email():


# clear function
def clear_input():
    acc_name_entry.delete(0, END)
    acc_num_entry.delete(0, END)
    branch_num_entry.delete(0, END)


# exit function
def exit_program():
    return root.destroy()


# for an image
canvas = Canvas(root, width=450, height=200, bg='#f9db17', borderwidth=0, highlightthickness=0)
canvas.place(x=-15, y=5)
img = ImageTk.PhotoImage(Image.open('./Images/ITHUBA-NATIONAL-LOTTERY.png'))
canvas.create_image(20, 20, anchor=NW, image=img)

# account labels
acc_name = Label(root, text="Account Holder:", font="Consolas 12 bold", bg="#f9db17")
acc_name.place(x=50, y=180)
acc_num = Label(root, text="Account Number:", font="Consolas 12 bold", bg="#f9db17")
acc_num.place(x=50, y=230)
branch_num = Label(root, text="Branch Code:", font="Consolas 12 bold", bg="#f9db17")
branch_num.place(x=50, y=280)
acc_bank = Label(root, text="Select Your Bank:", font="Consolas 12 bold", bg="#f9db17")
acc_bank.place(x=50, y=330)

# account entries
acc_name_entry = Entry(root)
acc_name_entry.place(x=250, y=180)
acc_num_entry = Entry(root)
acc_num_entry.place(x=250, y=230)
branch_num_entry = Entry(root)
branch_num_entry.place(x=250, y=280)

# buttons
submit_btn = Button(root, text="Submit", font="Consolas 12 bold", bg="black", fg="#f9db17", borderwidth=10,
                    command=bank_number)
submit_btn.place(x=177, y=400)
clear_btn = Button(root, text="Clear", font="Consolas 12 bold", bg="black", fg="#f9db17", borderwidth=10,
                   command=clear_input)
clear_btn.place(x=320, y=400)
exit_btn = Button(root, text="Exit", font="Consolas 12 bold", bg="black", fg="#f9db17", borderwidth=10,
                  command=exit_program)
exit_btn.place(x=50, y=400)

# ComboBox
combo_box_banks = Combobox(root)
combo_box_banks["values"] = "FNB", "Absa", "Standard Bank", "Capitec"
combo_box_banks.place(x=250, y=330)
combo_box_banks.set("Select Your Bank")
combo_box_banks['state'] = 'readonly'

# to run the program
root.mainloop()
