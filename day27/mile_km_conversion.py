import tkinter as tk
from turtle import bgcolor

from pyparsing import col

window = tk.Tk()
window.title('Conversion tool miles to km')
window.config(padx=10, pady=10)

def convert():
    miles_value = float(meter_input.get()) * 1.6
    output_label_value['text'] = miles_value

# main_frame = tk.Frame(window)
# main_frame.grid(padx=5, pady=5)

meter_input = tk.Entry(width=10)
meter_input.grid(row=0, column=1, padx=5, pady=5)
meter_input.focus()
meter_input.insert(tk.FIRST, string='0')

input_label = tk.Label(text='miles')
input_label.grid(row=0, column=2, padx=5, pady=5)

output_label_prefix = tk.Label(text='is_equal_to')
output_label_prefix.grid(row=1, column=0, padx=5, pady=5)

output_label_value = tk.Label(text='0')
output_label_value.grid(row=1, column=1, padx=5, pady=5)

output_label_unit = tk.Label(text='km')
output_label_unit.grid(row=1, column=2, padx=5, pady=5)

conversion_button = tk.Button(text='Conversion', command=convert)
conversion_button.grid(row=2, column=1, padx=5, pady=5)

quit_button = tk.Button(text='Exit', command=window.destroy)
quit_button.grid(row=2, column=2, padx=5, pady=5)


window.mainloop()