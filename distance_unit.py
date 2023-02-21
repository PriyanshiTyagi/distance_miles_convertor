from tkinter import *


def calculate():
    distance = float(distance_entry.get()) * 1.60934
    answer_label.config(text=distance)


FONT = ("Arial", 10)

window = Tk()
window.title("MILES TO KM ")

window.config(padx=20, pady=20)

miles_label = Label(text="Miles", font=FONT)
miles_label.pack(padx=20)
miles_label.grid(row=0, column=2)

equals_to_label = Label(text="is equals to", font=FONT)
equals_to_label.grid(row=1, column=0)
km_label = Label(text="km")
km_label.grid(row=1, column=2)

answer_label = Label(text=0, font=FONT)
answer_label.grid(row=1, column=1)
answer_label.config(padx=10, pady=10)

distance_entry = Entry(width=10)
distance_entry.insert(END, string=0)
distance_entry.grid(row=0, column=1)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
