# SE INTENTA EJECUTAR LA VENTANA EN HD
try:
   from ctypes import windll
   windll.shcore.setProcessDpiAwarness(1)
except:
   pass

import pywhatkit
import Voice
import wikipedia
import subprocess as sub
import threading as tr
import keyboard
import datetime
from pygame import mixer
from tkinter import *
from Windows.WindowP import WindowPassive
from diccionarios import charge_data, save_data, apps, sites, contacts
from Windows.MainWindow import MainWindow
import whts
import Face_files.face_recognizer as fr

mainw = MainWindow()

#------------------------------------------------------ FUNCIONES ---------------------------------#

#--------------escribir texto-----------#

def write_text(text_wiki):
   mainw.text_info.delete("1.0", "end")
   mainw.text_info.insert(INSERT, text_wiki)

# ---------funcion alarma---------#
def clock(rec):
   num = rec.replace('alarma', '').strip()
   Voice.talk(f'Alarma establecida a las {num} horas')
   if num[0] != '0' and len(num) < 5:
      num = '0' + num
   print(num)

   while True:
      if datetime.datetime.now().strftime('%H:%M') == num:
         print("DESPIERTA!!!")
         mixer.init()
         mixer.music.load("tema.mp3")
         mixer.music.play()
      else:
         continue

      if keyboard.read.key() == 's':
         mixer.music.stop()
         break

#----------------funcion para parar de escuchar---------#

def detente():
   Voice.talk("Si señor")

#---------funcion para musica en youtube------------------#
def musica(entr):
   music = entr.replace('musica', '')
   Voice.talk('Reproduciendo '+ music)
   write_text(f"Reproduciendo {music}")
   pywhatkit.playonyt(music)

#------------------funcion para ejecutar aplicaciones---------#
def ejecutar(entr):
   entr = entr.replace('ejecutar ', '')
   charge_data(apps, "app.txt")
   try:
      if entr in apps:  
         print(apps[entr])
         sub.call((f'start {apps[entr]}'), shell = True, )
         Voice.talk(f'Ejecutando {entr}')
         write_text(f'Ejecutando {entr}')
   except:
      pass

#------------------funcion para enviar mensaje a whatsapp---------#
def enviar_mensaje(entr):
   print("hola")
   charge_data(contacts, "contactos.txt")

   for c in contacts:
      print(c)
   try:
      entr = Voice.recognize('A quien quieres enviar un mensaje?')
   except UnboundLocalError:
      print("nada")
   entr = entr.strip()

   try:
      if entr in contacts:
         for cont in contacts:
            if cont in entr:
               entr = contacts[cont]
               try:
                  message = Voice.recognize('Que mensaje quieres enviar?')
               except UnboundLocalError:
                  print("nada")
               Voice.talk('Enviando mensaje..')
               whts.send_message(entr, message)
   except:
      print('chingao')

#------------------funcion para buscar en wikipedia---------#
def busca(entr):
   search = entr.replace('busca', '')
   wikipedia.set_lang("es")
   wiki = wikipedia.summary(search, 1) #busca resumidamente y guarda en search 1 oracion
   write_text(search + ": " + wiki)
   t = tr.Thread(target = Voice.talk, args = (wiki,))
   t.start()

#------------------funcion para abrir el mapa------------------#
def mapa():
   Voice.talk('Abriendo Maps')
   write_text("Abriendo mapa...")
   Voice.maps()

#------------------funcion para abrir paginas web en opera------------------#
def abrir(entr):
   entr = entr.replace('abrir ', '')
   print(entr)
   charge_data(sites, "pw.txt")
   try:
      if entr in sites:
         print(sites[entr])
         sub.call(f'start opera.exe {sites[entr]}', shell = True) #call va a ejecutar la app de opera en el sitio especificado
         Voice.talk(f'Abriendo {entr}') #la f y las {} es lo mismo que el '...' + '...'
         write_text(f'Abriendo {entr}')
   except:
      pass

#------------------funcion para establecer la alarma en un hilo---------#
def alarma(entr):
   t = tr.Thread(target = clock, args = (entr,)) #la coma es importante, rec1 es el parametro que se le pasa a clock
   t.start()

#------------------funcion para cerrar aplicaciones y/o el programa---------#
def cierra(entr):
   if 'cierrate' or 'ciérrate' in entr:
      Voice.talk('Nos re vimos men')
      sub.call('taskkill /IM python.exe /F', shell= True) #cierra el programa ejecutandose en python

   for task in apps:
      kill_task = apps[task].split('\\') # convierte el path en una lista, quitando los \\
      print(kill_task)
      kill_task = kill_task[-1] #agarra el ultimo elemento de la lista
      print(kill_task)
      if task in entr:
         sub.call(f'taskkill /IM {kill_task} /F', shell= True)
         write_text(f'cerrando {kill_task}')
         Voice.talk(f'cerrando {kill_task}')
      if 'todo' in entr:
         sub.call(f'taskkill /IM {kill_task} /F', shell= True)
         write_text(f'cerrando {kill_task}')
         Voice.talk(f'cerrando {kill_task}')

#------------------funcion para el reconocimento facial------------------#
def reconocimiento(entr):
   entr = entr.replace('reconocimiento', '')
   if 'activar' in entr:
      write_text('Activando reconocimiento facial')
      Voice.talk('Activando reconocimiento facial')
      tfr = tr.Thread(target = fr.face_rec, args = (0,))# con 0 se activa, con 1 se desactiva
      tfr.start()
   elif 'lisa' in entr:
      write_text('Desactivando reconocimiento facial')
      Voice.talk('Desactivando reconocimiento facial')
      fr.face_rec(1)
   print("xd")

#------------------funcion para el cambio de ventana------------------#
def passive_mode(entr):
   pasive = WindowPassive()
   if 'activar' in entr:
      Voice.talk('Activando modo pasivo')
      
      pasive.pasive_window(read_voice)
      mainw.destroy()
      
   elif 'desactivar' in entr:
      Voice.talk('Desactivando modo pasivo')
      
      pasive.destroy()
      

   


#------------------comandos (key:value)------------------#

key_words = {

   'musica' : musica,
   'detente' : detente,
   'ejecutar' : ejecutar,
   'enviar' : enviar_mensaje,
   'busca' : busca,
   'mapa' : mapa,
   'abrir' : abrir,
   'alarma' : alarma,
   'cierra' : cierra,
   'ciérrate' : cierra,
   'reconocimiento' : reconocimiento,
   'pasivo' : passive_mode

}

#------------------ejecutar funciones en el diccionario------------------#

def peticiones(entr):
   
   if entr:
      
      if 'detente' in entr:
         key_words['detente']

      elif 'mapa' in entr:
         key_words['mapa']

      else:
         for word in key_words:
            if word in entr:
               key_words[word](entr)
   else:
      print('nada')



#-----------------------funciones para recibir instrucciones--------------------#

#-------------------texto-------------#
def read_text():

   text = mainw.text_input.get()
   peticiones(text)
   mainw.text_input.delete(0, "end")


#-------------------voz-------------#
def read_voice():    
   try:
      rec1 = (str)(Voice.recognize('lo escucho señor'))
      
   except UnboundLocalError:
      print("nada")
   
   print(rec1)
   Voice.talk(rec1)
   peticiones(rec1)

#-----------------------------------------------------VENTANAS AGREGAR ITEMS----------------------------------------------------#

#-----------------------ventana app--------------------#

def agg_app():
   window_apps = Toplevel()
   window_apps.title("Agregar Apps")
   window_apps.configure(bg = "#434343")
   window_apps.geometry("300x170")
   window_apps.resizable(0,0)
   mainw.eval(f'tk::PlaceWindow {str(window_apps)} center')


   title_label = Label(window_apps, text = "Agrega una aplicacion", fg = "white", bg = "#434343", font = ("Arial", 15, "bold"))
   title_label.pack(pady = 3)

   name_label = Label(window_apps, text = "Nombre de la App", fg = "white", bg = "#434343", font = ("Arial", 10, "bold"))
   name_label.pack(pady = 2)

   name_entry = Entry(window_apps)
   name_entry.pack(pady = 1)

   direc_label = Label(window_apps, text = "Ruta de la App", fg = "white", bg = "#434343", font = ("Arial", 10, "bold"))
   direc_label.pack(pady = 2)

   direc_entry = Entry(window_apps, width = 35)
   direc_entry.pack(pady = 1)


   def del_text():
      n_app = name_entry.get().strip()
      d_app = direc_entry.get()
      save_data(n_app, d_app, "app.txt", "a")
      write_text("App agregada!!")
      name_entry.delete(0,"end")
      direc_entry.delete(0,"end")

   button_agregar = Button(window_apps,  text = "Agregar", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = del_text)
   button_agregar.pack(pady = 2)

#-----------------------termina ventana app--------------------#


#-----------------------ventana pw--------------------#
def agg_pw():
   window_pw = Toplevel()
   window_pw.title("Agregar Paginas Web")
   window_pw.configure(bg = "#434343")
   window_pw.geometry("300x170")
   window_pw.resizable(0,0)
   mainw.eval(f'tk::PlaceWindow {str(window_pw)} center')


   title_label = Label(window_pw, text = "Agrega una pagina web", fg = "white", bg = "#434343", font = ("Arial", 15, "bold"))
   title_label.pack(pady = 3)

   name_label = Label(window_pw, text = "Nombre de la PW", fg = "white", bg = "#434343", font = ("Arial", 10, "bold"))
   name_label.pack(pady = 2)

   name_entry = Entry(window_pw)
   name_entry.pack(pady = 1)

   direc_label = Label(window_pw, text = "Ruta de la PW", fg = "white", bg = "#434343", font = ("Arial", 10, "bold"))
   direc_label.pack(pady = 2)

   direc_entry = Entry(window_pw, width = 35)
   direc_entry.pack(pady = 1)


   def del_text_pw():
      n_pw = name_entry.get().strip()
      d_pw = direc_entry.get()
      save_data(n_pw, d_pw, "pw.txt", "p")
      write_text("Pagina Web agregada!!")
      name_entry.delete(0,"end")
      direc_entry.delete(0,"end")

   button_agregar = Button(window_pw,  text = "Agregar", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = del_text_pw)
   button_agregar.pack(pady = 2)

#-----------------------termina ventana pw--------------------#

#-----------------------ventana contacto--------------------#
def agg_contact():
   window_contac = Toplevel()
   window_contac.title("Agregar Contacto")
   window_contac.configure(bg = "#434343")
   window_contac.geometry("300x170")
   window_contac.resizable(0,0)
   mainw.eval(f'tk::PlaceWindow {str(window_contac)} center')


   title_label = Label(window_contac, text = "Agrega un contacto", fg = "white", bg = "#434343", font = ("Arial", 15, "bold"))
   title_label.pack(pady = 3)

   name_label = Label(window_contac, text = "Nombre del contact", fg = "white", bg = "#434343", font = ("Arial", 10, "bold"))
   name_label.pack(pady = 2)

   name_entry = Entry(window_contac)
   name_entry.pack(pady = 1)

   direc_label = Label(window_contac, text = "Numero del contacto", fg = "white", bg = "#434343", font = ("Arial", 10, "bold"))
   direc_label.pack(pady = 2)

   direc_entry = Entry(window_contac, width = 35)
   direc_entry.pack(pady = 1)


   def del_text_contact():
      nombre_contact = name_entry.get().strip()
      phone_contact = direc_entry.get()
      save_data(nombre_contact, phone_contact, "contactos.txt", "c")
      write_text("Contacto guardado!!")
      name_entry.delete(0,"end")
      direc_entry.delete(0,"end")

   button_agregar = Button(window_contac,  text = "Agregar", fg = "#FFFFFF", bg = "#1C0549", font = ("Arial", 10, "bold"), command = del_text_contact)
   button_agregar.pack(pady = 2)

#-----------------------ventana contacto--------------------#


mainw.charge_window(read_voice, read_text, agg_app, agg_pw, agg_contact)