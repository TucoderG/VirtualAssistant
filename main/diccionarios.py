from Voice import talk

sites = dict()
apps = dict()
contacts = dict()

def charge_data(name_dict, name_file):
   try:
      with open(name_file) as f:
         for line in f:
            (key, val) = line.split(",")
            val = val.rstrip("\n")
            name_dict[key] = val

   except FileNotFoundError as e:

      print(e)



def save_data(key, value, file_name, dic):
    try:
        print(f"guardando datos en txt: {key}, {value}, {file_name}")
        with open(file_name, 'a') as f:
            f.write(f"{key},{value}\n")
            if(dic == "a"):
                charge_data(apps, file_name)

            elif(dic == "p"):
                charge_data(sites, file_name)
            elif(dic == "c"):
                charge_data(contacts, file_name)

            f.close()

    except:
        pass


def talk_dic_app():
    charge_data(apps,'app.txt')
    if bool(apps) == True:
        talk("Las aplicaciones guardadas son: ")
        for ap in apps:
            talk(ap)
    else:
        talk("No hay aplicaciones..")

def talk_dic_pw():
    charge_data(sites,'pw.txt')
    if bool(sites) == True:
        talk("Las paginas guardadas son: ")
        for s in sites:
            talk(s)
    else:
        talk("No hay paginas web..")

def talk_dic_c():
    charge_data(contacts,'contactos.txt')
    if bool(contacts) == True:
        talk("Los contactos guardados son: ")
        for c in contacts:
            talk(c)
    else:
        talk("No hay contactos..")