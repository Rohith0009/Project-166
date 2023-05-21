from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Canvas")
root.geometry("1000x600")
root.configure(bg="pale turquoise")

canvas = Canvas(
    root, width=990, height=490, bg="white", highlightbackground="light gray"
)
canvas.pack()

LabelCC = Label(root, text="Choose Colour")
Colors = ["Blue", "Red", "Green", "Yellow", "Pink", "Purple"]
CCComboBox = ttk.Combobox(root, state="readonly", values=Colors, width=10)
LabelCC.place(anchor=CENTER, relx=0.45, rely=0.86)
CCComboBox.place(anchor=CENTER, relx=0.54, rely = 0.86)

cords = [10, 50, 100, 200, 300, 400, 500, 600, 800, 900]

startx = Label(root, text="Start X")
startxComboBox = ttk.Combobox(root, state="readonly", values=cords, width=10)
startx.place(anchor=CENTER, relx=0.04, rely=0.93)
startxComboBox.place(anchor=CENTER, relx=0.11, rely = 0.93)

starty = Label(root, text="Start Y")
startyComboBox = ttk.Combobox(root, state="readonly", values=cords, width=10)
starty.place(anchor=CENTER, relx=0.23, rely=0.93)
startyComboBox.place(anchor=CENTER, relx=0.3, rely=0.93)

endx = Label(root, text="End X")
endxComboBox = ttk.Combobox(root, state="readonly", values=cords, width=10)
endx.place(anchor=CENTER, relx=0.67, rely=0.93)
endxComboBox.place(anchor=CENTER, relx=0.74, rely=0.93)

endy = Label(root, text="End Y")
endyComboBox = ttk.Combobox(root, state="readonly", values=cords, width=10)
endy.place(anchor=CENTER, relx=0.86, rely=0.93)
endyComboBox.place(anchor=CENTER, relx=0.93, rely=0.93)

root.mainloop()
