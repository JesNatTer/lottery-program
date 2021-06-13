from tkinter import *
# import random
# from PIL import ImageTk, Image
# import mp3play

# setup
root = Tk()
# window size
root.geometry('500x500')
# background colour
root.config(bg='#e1ad01')
# window title
root.title("The National Lottery")
# for an image
# canvas = Canvas(root, width=300, height=300)
# canvas.place(x=5, y=5)
# img = ImageTk.PhotoImage(Image.open('lp-photo.png'))
# canvas.create_image(20, 20, anchor=N, image=img)
# playing sound
# f = mp3play.load('lotto-sound.mp3'); play = lambda: f.play()

# label and entry for user numbers
user_num_lbl = Label(root, text='Enter your numbers here:', bg="#e1ad01", font="Consolas 12 bold")
user_num_lbl.place(x=50, y=150)
user_num_entry = Entry(root)
user_num_entry.place(x=300, y=154)

# button
lotto_btn = Button(root, text="Check Your Lotto Numbers", bg="black", font="Consolas 12 bold", borderwidth="10", fg="white")
lotto_btn.place(x=120, y=200)



# to run the program
root.mainloop()