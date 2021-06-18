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

winnings = [0, 20, 100.50, 2, 384, 8, 584, 10, 000, 000]
lotto_list1 = []
lotto_list2 = []
lotto_list3 = []


def generate_list1():
    lotto_list1.append(user_num_entry.get())
    lotto_list1.append(user_num_entry4.get())
    lotto_list1.append(user_num_entry5.get())
    lotto_list1.append(user_num_entry6.get())
    lotto_list1.append(user_num_entry7.get())
    lotto_list1.append(user_num_entry8.get())


def generate_list2():
    lotto_list2.append(user_num_entry2.get())
    lotto_list2.append(user_num_entry8.get())
    lotto_list2.append(user_num_entry9.get())
    lotto_list2.append(user_num_entry10.get())
    lotto_list2.append(user_num_entry11.get())
    lotto_list2.append(user_num_entry12.get())


def generate_list3():
    lotto_list3.append(user_num_entry3.get())
    lotto_list3.append(user_num_entry14.get())
    lotto_list3.append(user_num_entry15.get())
    lotto_list3.append(user_num_entry16.get())
    lotto_list3.append(user_num_entry17.get())
    lotto_list3.append(user_num_entry18.get())


def generate_nums():
    winnings_won1 = []
    # f = open("details.txt", "a+")
    # f.write("Your Winnings Were:" + " " + winnings_won)
    # f.close()
    lotto_list1.append(int(user_num_entry.get()))
    lotto_list1.append(int(user_num_entry3.get()))
    lotto_list1.append(int(user_num_entry4.get()))
    lotto_list1.append(int(user_num_entry5.get()))
    lotto_list1.append(int(user_num_entry6.get()))
    lotto_list1.append(int(user_num_entry7.get()))
    lotto_nums = sample(range(1, 49), 6)
    lotto_nums.sort()
    lotto_num_lbl1.configure(text=lotto_nums[0], bg="white")
    lotto_num_lbl2.configure(text=lotto_nums[1], bg="white")
    lotto_num_lbl3.configure(text=lotto_nums[2], bg="white")
    lotto_num_lbl4.configure(text=lotto_nums[3], bg="white")
    lotto_num_lbl5.configure(text=lotto_nums[4], bg="white")
    lotto_num_lbl6.configure(text=lotto_nums[5], bg="red")

    count = 0
    try:
        for x in lotto_nums:
            if x in lotto_list1 or lotto_list2 or lotto_list3:
                count += 1
        if count <= 1:
            messagebox.showinfo("Bad Luck!",
                                str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                    winnings[0]))
            str(winnings_won1.append(winnings[0]))
        elif count == 2:
            messagebox.showinfo("Congratulations!",
                                str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                    winnings[1]))
            str(winnings_won1.append(winnings[1]))
        elif count == 3:
            messagebox.showinfo("Congratulations!",
                                str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                    winnings[2]))
            str(winnings_won1.append(winnings[2]))
        elif count == 4:
            messagebox.showinfo("Congratulations!",
                                str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + str(winnings[3]))
            str(winnings_won1.append(winnings[3]))
        elif count == 5:
            messagebox.showinfo("Congratulations!",
                                str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + str(
                                    winnings_won1.append(winnings[4])))
        elif count == 6:
            messagebox.showinfo("Congratulations!",
                                str(count) + " " + "Numbers" + "\n" + "Your Winnings Are:" + str(
                                    winnings_won1.append(winnings[5])))
            print(winnings_won1)
        return lotto_nums
    except ValueError:
        messagebox.showinfo("Failure", "Please Enter Digits Only")


def banking_details():
    messagebox.showinfo("Success", "Please Enter Your Bank Details In The Next Window")
    root.destroy()
    import bank


def currency_convertor():
    messagebox.showinfo("Success", "Welcome To The Currency Convertor")
    root.destroy()
    import currency


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
clear_btn.place(x=5, y=320)
exit_btn = Button(root, text='Exit', command=exit_program, bg="black", font="Consolas 12 bold", borderwidth="10",
                  fg="white", highlightthickness=0)
exit_btn.place(x=150, y=320)

claim_btn = Button(root, text="Claim Prize", bg="Black", font="Consolas 12 bold", fg="white", command=banking_details,
                   borderwidth=10)
claim_btn.place(x=592, y=400)

currency_btn = Button(root, text="Currency Convertor", bg="Black", font="Consolas 12 bold", fg="white",
                      command=currency_convertor, borderwidth=10)
currency_btn.place(x=5, y=400)

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
