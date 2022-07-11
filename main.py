from tkinter import *


def calculate():
    input_kilo["text"] = float(input_mile.get()) * 1.609


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=25, pady=25)


# ## First row
input_mile = Entry(width=10)
input_mile.insert(END, string="0")
input_mile.grid(row=0, column=1)

label_mile = Label(text="Miles")
label_mile.grid(row=0, column=2)


# ## Second row
label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0)

input_kilo = Label(text="0")
input_kilo.grid(row=1, column=1)

label_equal = Label(text="Km")
label_equal.grid(row=1, column=2)


# ## Third row
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)


# The main loop
window.mainloop()