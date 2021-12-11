def cleandata(file):
    import numpy as np
    import pandas as pd

    with open('JI_GitHub_SIATA/estacion_data_calidadaire_48_20190101_20201231.txt') as f:
        station48 = f.read().splitlines() #lista con el nombre de los archivos csv
    
    print(station48)