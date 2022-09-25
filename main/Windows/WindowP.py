from tkinter import *
from PIL import Image, ImageTk



class WindowPassive(Tk):

    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("160x60")
        self.resizable(0,0)
        self.configure(bg="#000000")
        self.image_button = ImageTk.PhotoImage(Image.open("Imagenes\\button_verde.png"))
        self.wm_attributes('-alpha', 0.4)

        

    def pasive_window(self, read_voice):

        self.button = Button(self, image = self.image_button, height=100, width = 100, command = read_voice)
        self.button.place(x = 0, y = 0, height = 50, width = 60)

        self.mainloop()
