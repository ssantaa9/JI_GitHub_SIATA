def cleandata(file):
    import numpy as np
    import pandas as pd

    with open("JI_GitHub_SIATA/"+file) as f:
        station = f.read().splitlines() #lista con el nombre de los archivos csv
    
    frames = []
    for i in range(len(station)):
        frames.append(pd.read_csv('JI_GitHub_SIATA/'+station[i]))

    d = pd.concat(frames) #Para algunos datos la fecha y hora estan en 'Unamed 0:' y para otros en 'Fecha_Hora'
    # d['id'] = d['Unnamed: 0'].fillna(d['Fecha_Hora']) #Se unifica la fecha y hora en una columna 'id'
    # d.index = pd.to_datetime(d['id']) #Definir como id la fecha y hora
    # del(d['Unnamed: 0'], d['Fecha_Hora'], d['id'])

    return d