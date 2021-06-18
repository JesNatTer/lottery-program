from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import requests
from playsound import playsound

# setting up window
root = Tk()
# window size
root.geometry("500x500")
# window color
root.config(bg="#f9db17")
# window title
root.title("Currency Convertor")
# for an image
canvas = Canvas(root, width=500, height=200, bg='#f9db17', borderwidth=0, highlightthickness=0)
canvas.place(x=-15, y=5)
img = ImageTk.PhotoImage(Image.open('./Images/ITHUBA-NATIONAL-LOTTERY.png'))
canvas.create_image(20, 20, anchor=NW, image=img)

# calling API
response = requests.get("https://v6.exchangerate-api.com/v6/48fdd8d31b8c3c5e6b84fa6f/latest/ZAR")
response = response.json()

conversion_rate = response["conversion_rates"]

currency_options = []
for i in conversion_rate.keys():
    currency_options.append(i)


def convert_currency():
    f = open("details.txt", "a+")
    f.write("\n" + "Converted Winnings:" + " " + str(display_amount.cget("text")))
    playsound("./Audio/counting-money.mp3")
    amount_entered = float(amount_entry.get())
    formula = round(amount_entered * response["conversion_rates"][currency_2_cb.get()], 2)
    display_amount.config(text=float(formula))
    messagebox.showinfo("Success", "Please Enter Your Banking Details In The Next Window")
    root.destroy()
    import bank


# exit function
def exit_program():
    return root.destroy()


# clear function
def clear_program():
    amount_entry.delete(0, END)
    display_amount.config(text="", bg="#f9db17")


# labels
amount = Label(root, text="Your Amount Won:", font="Consolas 12 bold", bg="#f9db17")
amount.place(x=5, y=180)
currency_1 = Label(root, text="From Currency:", font="Consolas 12 bold", bg="#f9db17")
currency_1.place(x=5, y=230)
currency_2 = Label(root, text="To Currency:", font="Consolas 12 bold", bg="#f9db17")
currency_2.place(x=5, y=280)
converted_amount = Label(root, text="Converted Amount:", font="Consolas 12 bold", bg="#f9db17")
converted_amount.place(x=5, y=330)
display_amount = Label(root, text="", bg="#f9db17")
display_amount.place(x=190, y=330)
currency_value = Label(root, text="Default Currency is set to Rands(ZAR)", bg="#f9db17", font="Consolas 10 bold")
currency_value.place(x=190, y=230)

# entry
amount_entry = Entry(root)
amount_entry.place(x=190, y=180)

# combo box
currency_2_cb = Combobox(root)
currency_2_cb['values'] = currency_options
currency_2_cb['state'] = 'readonly'
currency_2_cb.set('Select Currency')
currency_2_cb.place(x=190, y=280)
# currency_2_cb.config(bg="#f9db17")
display_amount.config(text='')

# buttons
exit_btn = Button(root, borderwidth="10", text="Exit", font="Consolas 15 bold", fg="white", bg="black",
                  command=exit_program)
exit_btn.place(x=400, y=400)
clear_btn = Button(root, borderwidth="10", text="Clear", font="Consolas 15 bold", fg="white", bg="black",
                   command=clear_program)
clear_btn.place(x=5, y=400)
convert_btn = Button(root, borderwidth="10", text="Convert", font="Consolas 15 bold", fg="white", bg="black",
                     command=convert_currency)
convert_btn.place(x=203, y=400)
# to run the program
root.mainloop()
