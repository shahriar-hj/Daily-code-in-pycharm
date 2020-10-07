# this code will produce an app that convert the height...
from tkinter import Tk, Button, Label, DoubleVar, Entry

# Define Function

def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    ft_value2.set("%.4f" % meter)


def clear():
    ft_value2.set("")
    ft_value.set("")



# build  GUI
window = Tk()
window.title("transform height in meter to feet")
window.configure(background="light blue")
window.geometry("320x220")
window.resizable(width=False, height=False)

ft_lbl1 = Label(window, text="Feet", bg="purple", fg="white", width=14)
ft_lbl1.grid(column=0, row=0, padx=15, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')

ft_lbl2 = Label(window, text="Meter", bg="Green", fg="white", width=14)
ft_lbl2.grid(column=0, row=1, padx=15, pady=30)

ft_value2 = DoubleVar()
ft_entry2 = Entry(window, textvariable=ft_value2, width=14)
ft_entry2.grid(column=1, row=1)
ft_entry2.delete(0, 'end')

convert_btn = Button(window, text="Convert", bg='blue', fg='white', width=14, command=convert)
convert_btn.grid(column=0, row=3, padx=15)

clear_btn = Button(window, text="Clear", bg='Red', fg='white', width=14, command=clear)
clear_btn.grid(column=1, row=3, padx=15)



window.mainloop()
