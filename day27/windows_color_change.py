import tkinter as tk

window = tk.Tk()
window['background'] = '#255255255'
window.minsize(width=500, height=500)

def set_red_color(number):
    hex_number = str(hex(int(number)).lstrip('0x').zfill(3))
    # red_color = str(window['background'][1:4])
    green_color = str(window['background'][4:7])
    blue_color = str(window['background'][7:])
    color_to_set = '#' + hex_number + green_color + blue_color
    window['bg'] = color_to_set
    red_scale['bg'] = color_to_set
    green_scale['bg'] = color_to_set
    blue_scale['bg'] = color_to_set

def set_green_color(number):
    hex_number = str(hex(int(number)).lstrip('0x').zfill(3))
    red_color = str(window['background'][1:4])
    # green_color = str(window['background'][4:7])
    blue_color = str(window['background'][7:])
    color_to_set = '#' + red_color + hex_number + blue_color
    window['bg'] = color_to_set
    red_scale['bg'] = color_to_set
    green_scale['bg'] = color_to_set
    blue_scale['bg'] = color_to_set

def set_blue_color(number):
    hex_number = str(hex(int(number)).lstrip('0x').zfill(3))
    red_color = str(window['background'][1:4])
    green_color = str(window['background'][4:7])
    # blue_color = str(window['background'][7:])
    color_to_set = '#' + red_color + green_color + hex_number
    window['bg'] = color_to_set
    red_scale['bg'] = color_to_set
    green_scale['bg'] = color_to_set
    blue_scale['bg'] = color_to_set

red_scale = tk.Scale(
    window,
    from_=0, to=4095,
    command=set_red_color,
    label='RED',
    length=200,
    )
red_scale.pack(side='left', padx=5, pady=5)

green_scale = tk.Scale(
    window,
    from_=0, to=4095,
    command=set_green_color,
    label='GREEN',
    length=200,
    )
green_scale.pack(side='left', padx=5, pady=5)

blue_scale = tk.Scale(
    window,
    from_=0, to=4095,
    command=set_blue_color,
    label='BLUE',
    length=200,
    )
blue_scale.pack(side='left', padx=5, pady=5)

window.mainloop()