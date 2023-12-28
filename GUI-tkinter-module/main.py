import tkinter
# from tkinter import *   --- if you use one class the use it

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=600)
window.config(padx=19, pady=18)
# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text here.."
# my_label.config(text="It's me TKINTER", background="purple")

my_label.config(padx=9, pady=4)

# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(row=0, column=0)

# BUTTON


def button_clicked():
    print("I got clicked")
    my_label["text"] = "Button Clicked"
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", border=1, command=button_clicked)
# button.pack()
button.grid(row=1, column=3)

# Entry
input = tkinter.Entry(width=18)
# input.pack()
input.grid(row=0, column=3)
# print(input.get())

entry = tkinter.Entry(width=30)
entry.insert(1, string="Some text to begin with.. ")
print(entry.get())
# entry.pack()
entry.grid(row=1, column=0)


# Text Entry Box   -- used to write multiple line of text
text = tkinter.Text(height=5, width=30)
# put cursor in text
text.focus()
# add some text to begin with...
text.insert(tkinter.END, "Examples of multi-line text entry here...")
print(text.get("1.0", tkinter.END))
# text.pack()
text.grid(row=5, column=1)

# Spinbox    -- counter i.e. go up and down
def spinbox_used():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
spinbox.grid(row=0, column=1)

# Scale --- basically a slider, move along xis to change value
# called with current scale value
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
scale.grid(row=1, column=4)


# Checkbox -- on/off
def checkbutton_used():
    print(checked_state.get())


checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is ON?", variable=checked_state, command=checkbutton_used)
# checkbutton.pack()
checkbutton.grid(row=1, column=1)

# Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)

# radiobutton2.pack()
# radiobutton1.pack()
radiobutton2.grid(row=3, column=0)
radiobutton1.grid(row=4, column=0)

# Listbox

def listbox_used(event):
    # get current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pears", "Orange", "Mango"]

for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)

# listbox.pack()
listbox.grid(row=5, column=3)


window.mainloop()
