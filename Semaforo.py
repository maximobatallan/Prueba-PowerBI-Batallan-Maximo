import pandas as pd
import numpy as np



df = pd.read_csv('E:/maxib/back up/Codigo/Test Power BI/Test_PowerBi (1)/Data_Usuarios.csv', delimiter=',')




#df.to_csv('rangoetario.csv')

semaforo = df
semaforo['fecha_de_finalizacion'] = semaforo['fecha_de_finalizacion'].fillna(0)
semaforo['cursos_finalizados'] = semaforo['cursos_finalizados'].fillna(0)

semaforo['cursos_finalizados'] = semaforo['cursos_finalizados'].astype(int)

semaforo['cursos_finalizados'] = semaforo['cursos_finalizados'].astype(int)

semaforo = semaforo.groupby(by=["id_usuario"]).sum()

semaforo['Porcentaje Finalizado'] = semaforo['cursos_finalizados']/semaforo['cursos_iniciados']*100

Total = semaforo['Porcentaje Finalizado'].sum()
Total = semaforo['Porcentaje Finalizado'].median()

semaforo['Porcentaje Finalizado'] = semaforo['Porcentaje Finalizado'].astype(int)
semaforo['id_usuario'] = semaforo.index
Total= int(Total)
semaforo['verde'] = semaforo['cursos_iniciados']*Total/100

print(semaforo)