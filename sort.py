from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import sqlite3
import tkinter as tk 

# Thay đổi ASSETS_PATH thành (""...\assets1\frame0")
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Desktop\function\assets1\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("510x340")
window.configure(bg = "#FFC1ED")
sort_frame = tk.Frame(window)
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))


canvas = Canvas(
        window,
        bg = "#FFC1ED",
        height = 340,
        width = 510,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
        16.0,
        16.0,
        495.0,
        323.0,
        fill="#FFFCFC",
        outline="")


def query_increase():
        # Create a database or connect to one
        conn = sqlite3.connect('DsTuLanh.db')

        # Create cursor
        c = conn.cursor

        # Query the database
        res = conn.execute("SELECT *,oid FROM addresses")
        records = res.fetchall()

        # Sort increasing
        records.sort(key=lambda a: a[4])
        print(records)

        # Print on the screen
        print_records = ''
        i = 1
        for record in records:
            print_records += str(i) + '/ ' + str(record[0]) + ' - ID:' + str(record[6]) + '\n'
            i += 1
        
        canvas.create_text(
        31.0,
        21.0,
        anchor="nw",
        text=print_records,
        fill="#000000",
        font=("Impact", 15 * -1)
        )


        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

query_increase()

def back():
    window.destroy()
    import main_menu

back_button = Button(
    image=button_image_4,
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
