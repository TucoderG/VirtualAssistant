from tkinter import *
from PIL import Image, ImageTk
from diccionarios import talk_dic_app, talk_dic_pw, talk_dic_c

class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("ROGELIO")
        self.geometry("1024x512")
        self.resizable(0,0)
        self.configure(bg = "#fdeff9")
        self.imagen_fondo = ImageTk.PhotoImage(Image.open("Imagenes/BF.jpg"))
        self.image_text = ImageTk.PhotoImage(Image.open("Imagenes/enviar.png"))
        self.comandos = """
            COMANDOS:

            -detente... Termina la ejecucion
            -musica... busca una cancion en yt
            -mapa... abre el maps
            -busca... busca en wikipedia
            -mensaje.. manda un mensaje a wpp
            -abrir... abre opera con una pag
            -ejecutar... aplicaciones
            -alarma... temporizador
        """

    

    def charge_window(self,read_voice, read_text, comand_app, comand_pw, comand_contact):

        self.label_fondo = Label(self, image = self.imagen_fondo, height = 512, width = 1024)
        self.label_fondo.place(x=0, y=0)

        self.text_info = Text(self, bg= "#271341", fg="#FFFFFF", borderwidth=2)
        self.text_info.place(x = 2 , y = 230, height = 40, width = 380)

        self.text_input = Entry(self, borderwidth=2)
        self.text_input.place(x = 2, y = 271,height = 30,width = 337)

        self.canvas = Canvas(bg = "#2F1341")
        self.canvas.place(x = 0, y = 0, height = 230)
        self.canvas.create_text(130, 120, text = self.comandos, fill = "#986FB3", font = ('Arial', 12, 'bold'))
        
        self.button_principal = Button(self, text = "Peticion", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = read_voice)
        self.button_principal.place(x = 730, y=220, height = 30,width = 125)

        
        self.button_enter = Button(self,image = self.image_text,command = read_text, borderwidth=2)
        self.button_enter.place(x = 340, y = 271, height = 30, width = 42)

        self.button_agg_app = Button(self, text = "Agregar App", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = comand_app)
        self.button_agg_app.place(x = 730, y=282, height = 30,width = 125)
        self.button_ver_apps = Button(self, text = "Apps agregadas", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = talk_dic_app)
        self.button_ver_apps.place(x = 865, y=282, height = 30,width = 135)

        self.button_agg_pw = Button(self, text = "Agregar Pw", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = comand_pw)
        self.button_agg_pw.place(x = 730, y=347, height = 30,width = 125)
        self.button_ver_pw = Button(self, text = "Pw agregadas", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = talk_dic_pw)
        self.button_ver_pw.place(x = 865, y=347, height = 30,width = 135)

        self.button_agg_contact = Button(self, text = "Agregar contacto", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = comand_contact)
        self.button_agg_contact.place(x = 730, y=417, height = 30,width = 125)
        self.button_ver_contact = Button(self, text = "Contactos agregados", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = talk_dic_c)
        self.button_ver_contact.place(x = 865, y=417, height = 30,width = 135)

        self.mainloop()
    
    

    