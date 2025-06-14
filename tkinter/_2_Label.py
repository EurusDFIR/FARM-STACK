import tkinter as tk
from PIL import Image,ImageTk


window = tk.Tk()
img = Image.open(r"R:/Eurus_Workspace/FARM_STACK/tkinter/shiina5.jpg")
photo = ImageTk.PhotoImage(img)


label = tk.Label(window,
              text="Shiina Mahiru",
              image=photo)

window.geometry("1096x1654")
# label.image = photo
label.pack()

window.mainloop()