import pandas as pd
import numpy as np
#Creacion de BASde de Datos
data={
'Estudiante':['Maria','Pedro','Juan','Luis',np.nan],
'Edad': [21,22,23,24,25],
'Calificacion': [95.80,85,80, 90]

}
df=pd.DataFrame(data)

#Gestion de valores nulos
df['Edad']=df['Edad'].fillna(df['Edad'].mean())#Imputacion de la media
df=df.dropna(subset=['Estudiante'])#Eliminacion de filas con valores nulos

#Eliminacion de Duplicados
df=df.drop_duplicates()
print("Dataser procesado con exito: ")
print(df)