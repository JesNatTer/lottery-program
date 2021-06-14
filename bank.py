from tkinter import *
from PIL import ImageTk, Image

# setting up the window
root = Tk()
root.geometry("500x500") # window size
root.title("Banking Details") # window title
root.config(bg="#f9db17")


# clear function
def clear_input():
    acc_name_entry.delete(0, END)
    acc_num_entry.delete(0, END)
    acc_bank_entry.delete(0, END)

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
submit_btn = Button(root, text="Submit", font="Consolas 12 bold", bg="black", fg="#f9db17", borderwidth=10)
submit_btn.place(x=205, y=400)
clear_btn = Button(root, text="Clear", font="Consolas 12 bold", bg="black", fg="#f9db17", borderwidth=10, command=clear_input)
clear_btn.place(x=305, y=400)
exit_btn = Button(root, text="Exit", font="Consolas 12 bold", bg="black", fg="#f9db17", borderwidth=10, command=exit_program)
exit_btn.place(x=122, y=400)

# to run the program
root.mainloop()