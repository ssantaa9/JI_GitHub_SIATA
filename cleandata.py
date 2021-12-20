def cleandata(file,porcentaje,datos):
    import numpy as np
    import pandas as pd

    with open("JI_GitHub_SIATA/"+file) as f:
        station = f.read().splitlines() #lista con el nombre de los archivos csv
    
    frames = []
    for i in range(len(station)):
        frames.append(pd.read_csv('JI_GitHub_SIATA/'+station[i]))
    
            
    if (datos == 1): 
        d = pd.concat(frames) #Para algunos datos la fecha y hora estan en 'Unamed 0:' y para otros en 'Fecha_Hora'
        d['id'] = d['Unnamed: 0'].fillna(d['Fecha_Hora']) #Se unifica la fecha y hora en una columna 'id'
        d.index = pd.to_datetime(d['id']) #Definir como id la fecha y hora
        del(d['Unnamed: 0'], d['Fecha_Hora'], d['id'])
        k = abs(((d[d==-9999.0]).sum())/9999.0)# Missing values in columns

        to_delete = (k>= (len(d)*(porcentaje/100))).tolist() # Eliminar las columnas que tengan el 10% o mas de datos faltantes
        columns = d.columns.tolist()
        index_to_delete = []
        for i in range(len(to_delete)):
        if(to_delete[i]):
        index_to_delete.append(i)
        index_to_delete.append(i+1)
        for i in index_to_delete:
        del(d[columns[i]])

        final_columns = d.columns.tolist()
        for i in final_columns:
        d = d.drop(d[(d[i]==-9999.0)].index.to_list(), axis=0) #Elimnar las filas que tengan datos malos

        #Matriz con solo las columnas de calidad
        calidad = d[d.columns[[d.columns.to_list().index(s) for s in d.columns.to_list() if s.__contains__("calidad")]].to_list()]

        calidad_columns = calidad.columns.tolist()
        for i in calidad_columns:
        d = d.drop(d[(d[i]>=2.6)].index.to_list(), axis=0) #Elimnar las filas que tengan datos de calidad malos
        calidad = calidad.drop(calidad[(calidad[i]>=2.6)].index.to_list(), axis=0)



    if (datos == 2):
        d.index = pd.to_datetime(d['fecha_hora']) #Definir como id la fecha y hora
        del(d['fecha_hora'])
        k = abs(((d[d==-999.0]).sum())/999.0)# Missing values in columns

        to_delete = (k>= (len(d)*(porcentaje/100))).tolist() # Eliminar las columnas que tengan el 10% o mas de datos faltantes
        columns = d.columns.tolist()
        index_to_delete = []
        for i in range(len(to_delete)):
            if(to_delete[i]):
                index_to_delete.append(i)
                index_to_delete.append(i+1)
        for i in index_to_delete:
            del(d[columns[i]])

        final_columns = d.columns.tolist()
        for i in final_columns:
            d = d.drop(d[(d[i]==-999.0)].index.to_list(), axis=0) #Elimnar las filas que tengan datos malos

        #Matriz con solo las columnas de calidad
        calidad = d[d.columns[[d.columns.to_list().index(s) for s in d.columns.to_list() if s.__contains__("calidad")]].to_list()]

        calidad_columns = calidad.columns.tolist()
        for i in calidad_columns:
            d = d.drop(d[(d[i]!=1.0)].index.to_list(), axis=0) #Elimnar las filas que tengan datos de calidad malos
            calidad = calidad.drop(calidad[(calidad[i]!=1.0)].index.to_list(), axis=0)
      
    return d
