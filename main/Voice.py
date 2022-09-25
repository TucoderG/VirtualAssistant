import speech_recognition as sr
import pyttsx3
import requests
import urllib
import time
from textblob import TextBlob



##########################################################################################

#####################"""""""""""""VOICE"""""""""""#################################
voice = 2
volume = 1
rate = 130


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[voice].id)
engine.setProperty('rate', rate)
engine.setProperty('volume', volume)



def talk(text):

    engine.say(text)
    engine.runAndWait()


name = 'rogelio'


def recognize(voz):
    listener = sr.Recognizer()
    
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        talk(voz)
        audio = listener.listen(source)
    try:
        record = listener.recognize_google(audio, language = "es")
        record = record.lower()
        if name in record:
            record = record.replace(name, '')

    except sr.UnknownValueError:
        print("no entendi, prueba de nuevo.")

    except sr.RequestError as e:
        print(f"Could not request results from google speech recognition service; {0}".format(e))

    return record
    
    
################################################################################
##############""""""""""""""MAPA"""""""""""""""""""""###########################


def maps():
    api_url = 'http://www.mapquestapi.com/directions/v2/route?'
    key = 'kAkZg2QZIQrApayzAyPdtp1FA7qstGZV'
    origin = ''
    destination = ''
    url = ''
    
    origin = input("Ingresa el origen: ") 
    destination = input("Ingresa el destino: ")


    url = api_url + urllib.parse.urlencode({'key':key, 'from': origin, 'to': destination})#creo URL
    json_data = requests.get(url).json() #obtengo lectura de la URL
    status_code = json_data['info']['statuscode'] # [estructura][dato] 

    if status_code == 0:
        duracion = json_data['route']['formattedTime']
        distance = json_data['route']['distance'] * 1.61 #millas a KM
        print("-----------------------")
        print("Informacion del viaje: ")
        print("Origen: " + origin + "\nDestino :" + destination)
        print("Duracion: " + duracion)
        print("Distancia entre el origen y el destino: " + str("{:.2f}".format(distance)) + " KM") #reduce decimales a solo 2

    for each in json_data['route']['legs'][0]['maneuvers']:
        distance_to_point = each['distance'] * 1.61 
        distance_remaining = distance - distance_to_point
        
        print("Faltan " + str("{:.2f}".format(distance_remaining)) + " KM por recorrer..")

        #if distance_to_point <= 0.14: #0.1388KM es lo que recorre en 5seg si va a 100km/hs
        texto = translate(each['narrative'])
        print(texto)
        talk(texto)
        distance = distance_remaining

        time.sleep(1)


######################################################################################
##################""""""""""""""""""TRADUCTOR""""""""""""""""#########################


def translate(text):

    
    print("TRADUCIENDO...")
    
    translation = TextBlob(text)
    try:
        es_blob = translation.translate(from_lang = 'en', to='es')
    except:
        print("No se pudo traducir...")
    text = str(es_blob)
    

    print("TERMINO TRADUCCION..")
    return text