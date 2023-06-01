from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import sqlite3
from collections import Counter

# Thay đổi ASSETS_PATH thành (""...\assets1\frame0")
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Desktop\function\assets1\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("510x340")
window.configure(bg = "#FFC1ED")
frame = Frame(window)
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


def count():
        # Create a database or connect to one
        conn = sqlite3.connect('DsTuLanh.db')

        # Create cursor
        c = conn.cursor

        # Query the database
        res = conn.execute("SELECT *,oid FROM addresses")
        records = res.fetchall()

        # Count brands
        counter = Counter(elem[0] for elem in records)
        results = ''
        for i in counter.elements():
            if i not in results:
                results += "% s : % s" % (i, counter[i]) + "\n"

        # Print on the screen
        
        canvas.create_text(
        31.0,
        21.0,
        anchor="nw",
        text=results,
        fill="#000000",
        font=("Impact", 15 * -1)
        )


        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

count()

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
