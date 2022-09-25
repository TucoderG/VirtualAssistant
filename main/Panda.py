from itertools import count
import pandas as pd
import matplotlib.pyplot as plt


data = pd.DataFrame
exel = 'Archivos\Retail2.xlsx'
q = plt
p = plt

try:
    print("Leyendo EXEL...\n")
    data = pd.read_excel(exel, header = 1) #leer archivo exel
    print("Cargando tablas...\n")
    data.columns = ['Invoice', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'Price', 'Customer ID', 'Country'] #nombres de columnas
    print("20 DE Price COUNT: \n")
    print(data['Price'].value_counts().head(20).sort_index(ascending = True)) # sort_index(Ascending = True o False) ordena A->Z
    print("######################")
    
    print("Guardando en variable 20 Prices")
    price = data['Price'].value_counts().head(20).sort_index(ascending = True)
    print("\nPrices guardados: \n")
    print(price)

    print("\nVALORES UNICOS DE price: \n")
    print(price.unique())

    print("\nGrafica de Customer COUNT: ........\n")
    colors = ['Red', 'Green', 'Blue', 'Black', 'Orange']
    price.plot(kind = 'bar', color = colors) #Dibuja un grafico de barras
    p.xlabel('Country')
    p.ylabel('Acciones')
    p.title('Total Acciones Country')
    print(p.show())
    print("TERMINO.........")

    
    print("\nOTRO GRAFICO--------------------\n")
    print("\nGuardando Datos de Quantity...\n")
    dato = data['Quantity'].head(20).sort_index(ascending = True)
    print("\nDatos guardados: \n")
    print(dato)
    print("\nDatos unicos: \n")
    print(dato.unique())
    

    datoCount = dato.value_counts(7).sort_index(ascending = True)
    print("\nDatos Count: \n")
    print(datoCount)
    

    #country = data[['Country', 'Price', 'StockCode'][:3]]
    
    ###########""""TORTA"""""#############
    print("\nCreando grafico torta...\n")
    explode = [0,0,0.3,0,0,0,0]   # espacio entre los pedazos de la grafica de pastel
    size = [0,0,0,0,0,0,0]                                             #tamaño de cada porcion
    i = 0
    for d in dato.unique():
        size[i] = d
        i+=1
    labels = ['1', '2', '3', '4', '5', '6', '7']                #etiquetas
    print("cargando..")
    q.pie(size,  labels =  labels, color = colors, explode = explode, shadow= True, autopct='%.2f%%')  #podes pasarle varias cosas al pie de la grafica

                                                    #autopct muestra 2 decimales
    print("Por mostrar..")
    q.title('Grafica.')
    q.axis('off')                                             #ejes "x" e "y"
    q.legend(loc = 'best')                                    #mejor posicion
    print("MOSTRANDO....")
    print(q.show())                                           # muestra la grafica
    print("TERMINO...")
except:
    pass


# print(data.head()) #muestra 5 elementos primeros
# print(data.sample()) #muestra 5 elementos aleatorios
# print(data.tail())  #muestra 5 elementos ultimos
# print(data['Price'][:3]) #muestra los primeros 3 de la columna Price
# print(data[['Price', 'Description']].tail(3)) #muestra las columnas Price y Description de los ultimos 3

# print(data['Country'].value_counts()) #value_counts cuenta las filas que sean de la misma Country







