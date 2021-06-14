from tkinter import *
# import random
from PIL import ImageTk, Image
# import mp3play

# setup
root = Tk()
# window size
root.geometry('800x400')
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

# label and entry for user numbers
user_num_lbl = Label(root, text='Enter your numbers here:', bg="#f9db17", font="Consolas 12 bold")
user_num_lbl.place(x=190, y=250)
user_num_entry = Entry(root)
user_num_entry.place(x=440, y=250)

# button
lotto_btn = Button(root, text="Check Your Lotto Numbers", bg="black", font="Consolas 12 bold", borderwidth="10", fg="white", highlightthickness=0)
lotto_btn.place(x=255, y=300)



# to run the program
root.mainloop()
