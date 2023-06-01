
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import sqlite3

# Thay đổi ASSETS_PATH thành (""...\assets\frame0")
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Desktop\function\assets\frame0")

'''
Mở comment để tạo file database
Sau khi xuất hiện file database đóng comment lại để không lỗi
'''
#     # Create a database or connect to one
# conn = sqlite3.connect('DsTuLanh.db')
#     # Create cursor
# c = conn.cursor
#     # Create table
# conn.execute(''' CREATE TABLE addresses (
#                 brand text,
#                 model text,
#                 origin text,
#                 eco_mode text,
#                 capacity integer,
#                 price integer
#                 )''')

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("510x340")
window.configure(bg = "#FFC1ED")

canvas = Canvas(
    window,
    bg = "#FFC1ED",
    height = 340,
    width = 510,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('DsTuLanh.db')

    # Create cursor
    c = conn.cursor


    conn.execute ("INSERT INTO addresses VALUES (:brand, :model, :origin, :eco_mode, :capacity, :price)",
            {
                'brand' : brand.get(),
                'model' : model.get(),
                'origin' : origin.get(),
                'eco_mode' : eco_mode.get(),
                'capacity' : capacity.get(),
                'price' : price.get()
            })
    
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    brand.delete(0,END)
    model.delete(0,END)
    origin.delete(0,END)
    eco_mode.delete(0,END)
    capacity.delete(0,END)
    price.delete(0,END)
     
canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=submit,
    relief="flat",
)

button_1.place(
    x=203.0,
    y=275.0,
    width=116.0,
    height=44.0
)

canvas.create_text(
    31.0,
    21.0,
    anchor="nw",
    text="Brand",
    fill="#000000",
    font=("Impact", 30 * -1)
)

canvas.create_text(
    31.0,
    63.0,
    anchor="nw",
    text="Model",
    fill="#000000",
    font=("Impact", 30 * -1)
)

canvas.create_text(
    31.0,
    105.0,
    anchor="nw",
    text="Origin",
    fill="#000000",
    font=("Impact", 30 * -1)
)

canvas.create_text(
    31.0,
    145.0,
    anchor="nw",
    text="Eco Mode",
    fill="#000000",
    font=("Impact", 30 * -1)
)

canvas.create_text(
    310.0,
    140.0,
    anchor="nw",
    text="(Yes/No)",
    fill="#000000",
    font=("Impact", 25 * -1)
)

canvas.create_text(
    31.0,
    182.0,
    anchor="nw",
    text="Capacity",
    fill="#000000",
    font=("Impact", 30 * -1)
)

canvas.create_text(
    313.0,
    182.0,
    anchor="nw",
    text="L",
    fill="#000000",
    font=("Impact", 25 * -1)
)

canvas.create_text(
    423.0,
    222.0,
    anchor="nw",
    text="VND",
    fill="#000000",
    font=("Impact", 25 * -1)
)

canvas.create_text(
    31.0,
    222.0,
    anchor="nw",
    text="Price ",
    fill="#000000",
    font=("Impact", 30 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    330.0,
    34.5,
    image=entry_image_1
)
brand = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
brand.place(
    x=192.0,
    y=22.0,
    width=276.0,
    height=23.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    330.0,
    116.5,
    image=entry_image_2
)
model = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
model.place(
    x=192.0,
    y=104.0,
    width=276.0,
    height=23.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    244.0,
    157.5,
    image=entry_image_3
)
origin = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
origin.place(
    x=193.0,
    y=145.0,
    width=102.0,
    height=23.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    244.0,
    198.5,
    image=entry_image_4
)
eco_mode = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
eco_mode.place(
    x=193.0,
    y=186.0,
    width=102.0,
    height=23.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    298.5,
    238.5,
    image=entry_image_5
)
capacity = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
capacity.place(
    x=192.0,
    y=226.0,
    width=213.0,
    height=23.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    331.0,
    75.5,
    image=entry_image_6
)
price = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
price.place(
    x=193.0,
    y=63.0,
    width=276.0,
    height=23.0
)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))

def back():
    window.destroy()
    import main_menu

back_button = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
back_button.place(
    x=24.0,
    y=284.0,
    width=55.0,
    height=39.779876708984375
)

window.resizable(False, False)
window.mainloop()
