from tkinter import *

window = Tk()
window.minsize(width=400, height=300)
window.title("Miles to Kilometer Convertor")


def calculate():
    dist_in_miles = float(user_input.get())
    dist_in_km = dist_in_miles * 1.60934
    # value_label["text"] = abs(round(dist_in_km, 1))
    value_label.config(text=f"{round(dist_in_km, 1)}")


# Label
label = Label(text="Distance here: ")
label.grid(row=0, column=0)

# Entry from user
user_input = Entry(width=8, font=("Arial", 14, "bold"))
user_input.grid(row=0, column=1)

mile_label = Label(text="Miles", pady=17, font=("Arial", 14, "bold"))
mile_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", pady=17, font=("Arial", 14, "bold"))
equal_label.grid(row=1, column=0)

km_label = Label(text="Km", pady=17, font=("Arial", 14, "bold"))
km_label.grid(row=1, column=2)

value_label = Label(text="0", pady=17, font=("Arial", 14, "bold"))
value_label.grid(row=1, column=1)


button = Button(text="Calculate", command=calculate, background="skyBlue", padx=8, pady=4, font=("Arial", 11, "bold"), border=4)
button.grid(row=2, column=1)

window.mainloop()
