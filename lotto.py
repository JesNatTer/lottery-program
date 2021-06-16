from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from random import sample

# setup
root = Tk()
# window size
root.geometry('800x500')
# background colour
root.config(bg='#f9db17')
# window title
root.title("The National Lottery")
# for an image
canvas = Canvas(root, width=500, height=200, bg='#f9db17', borderwidth=0, highlightthickness=0)
canvas.place(x=135, y=5)
img = ImageTk.PhotoImage(Image.open('./Images/ITHUBA-NATIONAL-LOTTERY.png'))
canvas.create_image(20, 20, anchor=NW, image=img)

winnings = ["R0", "R20", "R100.50", "R2,384", "R8,584", "R10,000,000"]
lotto_list1 = []
lotto_list2 = []
lotto_list3 = []

def generate_list1():
    global lotto_list1
    num1 = int(user_num_entry.get())
    num2 = int(user_num_entry4.get())
    num3 = int(user_num_entry5.get())
    num4 = int(user_num_entry6.get())
    num5 = int(user_num_entry7.get())
    num6 = int(user_num_entry8.get())
    list_1 = [num1, num2, num3, num4, num5, num6]
    lotto_list1.append(list_1)
    return list_1


def generate_list2():
    num7 = user_num_entry2.get()
    num8 = user_num_entry9.get()
    num9 = user_num_entry10.get()
    num10 = user_num_entry11.get()
    num11 = user_num_entry12.get()
    num12 = user_num_entry13.get()
    list_2 = num7, num8, num9, num10, num11, num12
    return list_2


def generate_list3():
    num13 = user_num_entry3.get()
    num14 = user_num_entry14.get()
    num15 = user_num_entry15.get()
    num16 = user_num_entry16.get()
    num17 = user_num_entry17.get()
    num18 = user_num_entry18.get()
    list_3 = num13, num14, num15, num16, num17, num18
    return list_3


def generate_nums():
    lotto_nums = sample(range(1, 49), 7)
    lotto_nums.sort()
    lotto_num_lbl1.configure(text=lotto_nums[0], bg="white")
    lotto_num_lbl2.configure(text=lotto_nums[1], bg="white")
    lotto_num_lbl3.configure(text=lotto_nums[2], bg="white")
    lotto_num_lbl4.configure(text=lotto_nums[3], bg="white")
    lotto_num_lbl5.configure(text=lotto_nums[4], bg="white")
    lotto_num_lbl6.configure(text=lotto_nums[5], bg="red")

    count = 0
    for num in lotto_list1:
        if num in lotto_list1:
            count += 1
    if count <= 1:
        messagebox.showinfo("Bad Luck!", str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + winnings[0])
    elif count == 2:
        messagebox.showinfo("Congratulations!",
                            str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + winnings[1])
    elif count == 3:
        messagebox.showinfo("Congratulations!",
                            str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + winnings[2])
    elif count == 4:
        messagebox.showinfo("Congratulations!",
                            str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + winnings[3])
    elif count == 5:
        messagebox.showinfo("Congratulations!",
                            str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + winnings[4])
    elif count == 6:
        messagebox.showinfo("Congratulations!",
                            str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + winnings[5])
    return lotto_nums


def clear_input():
    user_num_entry.delete(0, END)
    user_num_entry2.delete(0, END)
    user_num_entry3.delete(0, END)
    user_num_entry4.delete(0, END)
    user_num_entry5.delete(0, END)
    user_num_entry6.delete(0, END)
    user_num_entry7.delete(0, END)
    user_num_entry8.delete(0, END)
    user_num_entry9.delete(0, END)
    user_num_entry10.delete(0, END)
    user_num_entry11.delete(0, END)
    user_num_entry12.delete(0, END)
    user_num_entry13.delete(0, END)
    user_num_entry14.delete(0, END)
    user_num_entry15.delete(0, END)
    user_num_entry16.delete(0, END)
    user_num_entry17.delete(0, END)
    user_num_entry18.delete(0, END)
    lotto_num_lbl1.config(text='', bg="#f9db17")
    lotto_num_lbl2.config(text='', bg="#f9db17")
    lotto_num_lbl3.config(text='', bg="#f9db17")
    lotto_num_lbl4.config(text='', bg="#f9db17")
    lotto_num_lbl5.config(text='', bg="#f9db17")
    lotto_num_lbl6.config(text='', bg="#f9db17")


def exit_program():
    return root.destroy()


# label and entry for user numbers
user_num_lbl = Label(root, text='Set 1:', bg="#f9db17", font="Consolas 12 bold")  # set
user_num_lbl.place(x=270, y=300)
user_num_entry = Entry(root, width=5)
user_num_entry.place(x=340, y=300)
user_num_lbl2 = Label(root, text='Set 2:', bg="#f9db17", font="Consolas 12 bold")  # set
user_num_lbl2.place(x=270, y=330)
user_num_entry2 = Entry(root, width=5)
user_num_entry2.place(x=340, y=330)
user_num_lbl3 = Label(root, text='Set 3:', bg="#f9db17", font="Consolas 12 bold")  # set
user_num_lbl3.place(x=270, y=360)
user_num_entry3 = Entry(root, width=5)
user_num_entry3.place(x=370, y=300)
user_num_entry4 = Entry(root, width=5)
user_num_entry4.place(x=400, y=300)
user_num_entry5 = Entry(root, width=5)
user_num_entry5.place(x=430, y=300)
user_num_entry6 = Entry(root, width=5)
user_num_entry6.place(x=460, y=300)
user_num_entry7 = Entry(root, width=5)
user_num_entry7.place(x=490, y=300)
user_num_entry8 = Entry(root, width=5)
user_num_entry8.place(x=370, y=330)
user_num_entry9 = Entry(root, width=5)
user_num_entry9.place(x=400, y=330)
user_num_entry10 = Entry(root, width=5)
user_num_entry10.place(x=430, y=330)
user_num_entry11 = Entry(root, width=5)
user_num_entry11.place(x=460, y=330)
user_num_entry12 = Entry(root, width=5)
user_num_entry12.place(x=490, y=330)
user_num_entry13 = Entry(root, width=5)
user_num_entry13.place(x=340, y=360)
user_num_entry14 = Entry(root, width=5)
user_num_entry14.place(x=370, y=360)
user_num_entry15 = Entry(root, width=5)
user_num_entry15.place(x=400, y=360)
user_num_entry16 = Entry(root, width=5)
user_num_entry16.place(x=430, y=360)
user_num_entry17 = Entry(root, width=5)
user_num_entry17.place(x=460, y=360)
user_num_entry18 = Entry(root, width=5)
user_num_entry18.place(x=490, y=360)

# instructions
user_instructions = Label(root, text='Instructions:', bg="#f9db17", font="Consolas 12 bold")
user_instructions.place(x=5, y=180)
user_instructions1 = Label(root, text='1. You have up to 3 sets to enter 6 different numbers', bg="#f9db17",
                           font="Consolas 12 bold", fg="black")
user_instructions1.place(x=5, y=200)
user_instructions2 = Label(root, text='2. You have to choose 6 different numbers ranging from 1-49', bg="#f9db17",
                           font="Consolas 12 bold", fg="black")
user_instructions2.place(x=5, y=220)
user_instructions3 = Label(root, text='3. Click Check Numbers to view the winning Lotto Numbers', bg="#f9db17",
                           font="Consolas 12 bold", fg="black")
user_instructions3.place(x=5, y=242)

# button
lotto_btn = Button(root, text="Check Numbers", bg="black", font="Consolas 12 bold", borderwidth="10", fg="white",
                   highlightthickness=0, command=generate_nums)
lotto_btn.place(x=585, y=320)
clear_btn = Button(root, text='Clear', command=clear_input, bg="black", font="Consolas 12 bold", borderwidth="10",
                   fg="white", highlightthickness=0)
clear_btn.place(x=50, y=320)
exit_btn = Button(root, text='Exit', command=exit_program, bg="black", font="Consolas 12 bold", borderwidth="10",
                  fg="white", highlightthickness=0)
exit_btn.place(x=150, y=320)

# display numbers header label
lotto_num_header = Label(root, text='The Lotto Numbers Are:', bg='#f9db17', fg='black', font="Consolas 12 bold")
lotto_num_header.place(x=300, y=400)

# display numbers label
lotto_num_lbl1 = Label(root, width=4, bg="#f9db17", text='')
lotto_num_lbl1.place(x=310, y=450)
lotto_num_lbl2 = Label(root, width=4, bg="#f9db17", text='')
lotto_num_lbl2.place(x=340, y=450)
lotto_num_lbl3 = Label(root, width=4, bg="#f9db17", text='')
lotto_num_lbl3.place(x=370, y=450)
lotto_num_lbl4 = Label(root, width=4, bg="#f9db17", text='')
lotto_num_lbl4.place(x=400, y=450)
lotto_num_lbl5 = Label(root, width=4, bg="#f9db17", text='')
lotto_num_lbl5.place(x=430, y=450)
lotto_num_lbl6 = Label(root, width=4, bg="#f9db17", text='')
lotto_num_lbl6.place(x=460, y=450)

# to run the program
root.mainloop()
