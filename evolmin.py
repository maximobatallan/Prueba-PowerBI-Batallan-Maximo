import pandas as pd
import numpy as np



evolucion = pd.read_csv('E:/maxib/back up/Codigo/Test Power BI/Test_PowerBi (1)/Cursos_Usuarios.csv', delimiter=',')

evolucion = evolucion.dropna()

evolucion['fecha_de_finalizacion'] = pd.to_datetime(evolucion['fecha_de_finalizacion'])
evolucion = evolucion.set_index('fecha_de_finalizacion')




#evolucion['fecha_de_finalizacion'] = pd.to_datetime(evolucion['fecha_de_finalizacion'])
evolucion= evolucion.groupby(pd.Grouper(freq="M"))

evolucion =evolucion.sum()

evolucion['fecha_de_finalizacion'] = evolucion.index
evolucion['cursos_finalizados'] = evolucion['cursos_finalizados'].astype(int)

print(evolucion)