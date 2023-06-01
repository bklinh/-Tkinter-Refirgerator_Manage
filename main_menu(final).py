from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Thay đổi ASSETS_PATH thành (""...\asset\frame0")
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Desktop\function\asset\frame0")


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

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    23.0,
    17.0,
    487.0,
    286.0,
    fill="#FF6AB1",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    145.17095947265625,
    140.71795654296875,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    363.0,
    86.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    363.0,
    196.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    363.0,
    251.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    363.0,
    141.0,
    image=image_image_5
)

def add_navi():
    window.destroy()
    import add

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
add_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_navi,
    relief="flat"
)
add_button.place(
    x=254.72349548339844,
    y=74.95639038085938,
    width=209.2307586669922,
    height=29.059829711914062
)

def sort_navi():
    window.destroy()
    import sort

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
sort_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sort_navi,
    relief="flat"
)
sort_button.place(
    x=254.72349548339844,
    y=130.8790283203125,
    width=209.2307586669922,
    height=27.9119873046875
)

def count_navi():
    window.destroy()
    import count

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
count_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=count_navi,
    relief="flat"
)
count_button.place(
    x=251.44998168945312,
    y=185.59571838378906,
    width=218.0,
    height=33.5042724609375
)

def search_navi():
    window.destroy()
    import find_delete

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
search_button = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=search_navi,
    relief="flat"
)
search_button.place(
    x=251.0,
    y=241.0,
    width=218.0,
    height=33.5042724609375
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=282.0,
    y=20.0,
    width=162.55003356933594,
    height=38.45002746582031
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=12.0,
    y=297.0,
    width=487.0,
    height=37.0
)
window.resizable(False, False)
window.mainloop()
