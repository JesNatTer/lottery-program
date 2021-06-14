from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
# import mp3play

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
# playing sound
# f = mp3play.load('lotto-sound.mp3'); play = lambda: f.play()

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
    ran_labl1.config(text='', bg="#f9db17")
    ran_labl2.config(text='', bg="#f9db17")
    ran_labl3.config(text='', bg="#f9db17")
    ran_labl4.config(text='', bg="#f9db17")
    ran_labl5.config(text='', bg="#f9db17")
    ran_labl6.config(text='', bg="#f9db17")

def exit_program():
    return root.destroy()

# label and entry for user numbers
user_num_lbl = Label(root, text='Set 1:', bg="#f9db17", font="Consolas 12 bold") # set
user_num_lbl.place(x=270, y=300)
user_num_entry = Entry(root, width=5)
user_num_entry.place(x=340, y=300)
user_num_lbl2 = Label(root, text='Set 2:', bg="#f9db17", font="Consolas 12 bold") # set
user_num_lbl2.place(x= 270, y=330)
user_num_entry2 = Entry(root, width=5)
user_num_entry2.place(x= 340, y=330)
user_num_lbl3 = Label(root, text='Set 3:', bg="#f9db17", font="Consolas 12 bold") # set
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
user_instructions1 = Label(root, text='1. You have up to 3 sets to choose numbers', bg="#f9db17", font="Consolas 12 bold", fg="black")
user_instructions1.place(x=5, y=200)
user_instructions2 = Label(root, text='2. You have to choose 6 numbers ranging from 1-49', bg="#f9db17", font="Consolas 12 bold", fg="black")
user_instructions2.place(x=5, y=220)

# button
lotto_btn = Button(root, text="Check Numbers", bg="black", font="Consolas 12 bold", borderwidth="10", fg="white", highlightthickness=0)
lotto_btn.place(x= 585, y=320)
clear_btn = Button(root, text='Clear', command=clear_input, bg="black", font="Consolas 12 bold", borderwidth="10", fg="white", highlightthickness=0)
clear_btn.place(x=50, y=320)
exit_btn = Button(root, text='Exit', command=exit_program, bg="black", font="Consolas 12 bold", borderwidth="10", fg="white", highlightthickness=0)
exit_btn.place(x=150, y=320)

# display numbers header label
ran_header = Label(root, text='The Lotto Numbers Are:', bg='#f9db17', fg='black', font="Consolas 12 bold")
ran_header.place(x=300, y=400)


# display numbers label
ran_labl1 = Label(root, width=4, bg="white", text='1')
ran_labl1.place(x=310, y=450)
ran_labl2 = Label(root, width=4, bg="white", text='2')
ran_labl2.place(x=340, y=450)
ran_labl3 = Label(root, width=4, bg="white", text='3')
ran_labl3.place(x=370, y=450)
ran_labl4 = Label(root, width=4, bg="white", text='4')
ran_labl4.place(x=400, y=450)
ran_labl5 = Label(root, width=4, bg="white", text='5')
ran_labl5.place(x=430, y=450)
ran_labl6 = Label(root, width=4, bg="red", text='6')
ran_labl6.place(x=460, y=450)

# to run the program
root.mainloop()
