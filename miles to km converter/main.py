from tkinter import *

def miles_to_km():
    miles = input_miles.get()
    km = round(float(miles)*1.6)
    result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20,pady=20)

input_miles = Entry(width=5)
input_miles.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

result_label = Label(text="0")
result_label.grid(column=1,row=1)

km_label = Label(text="km")
km_label.grid(column=2,row=1)

calculate_button = Button(text="calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)



window.mainloop()