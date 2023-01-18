import pandas as pd
import numpy as np



#Rango etarioooo!!
today = '2023-01-11 05:00:00'

# dd/mm/YY




df = pd.read_csv('E:/maxib/back up/Codigo/Test Power BI/Test_PowerBi (1)/Data_Usuarios.csv', delimiter=',')
df1 = df.drop(['id_usuario','ciudad','nivel_educativo', 'Sueldo'], axis=1)


df1['fechas_de_nacimiento'] = np.where((df1['fechas_de_nacimiento'] >'1923-01-11 05:00:00') , df1['fechas_de_nacimiento'],0 )

#print(df1.sort_values('fechas_de_nacimiento'))

indexAge = df1[ (df1['fechas_de_nacimiento'] == 0)].index
df1.drop(indexAge , inplace=True)

df1['fechas_de_nacimiento'] = np.where((df1['fechas_de_nacimiento'] <'2008-01-11 05:00:00') , df1['fechas_de_nacimiento'], 0)


indexAge = df1[ (df1['fechas_de_nacimiento'] == 0)].index
df1.drop(indexAge , inplace=True)


df1 =df1.append(pd.DataFrame({'fechas_de_nacimiento': pd.date_range(start=df1.fechas_de_nacimiento.iloc[-1], periods=6, freq='M', closed='right')}))


print(df1.tail(50))

