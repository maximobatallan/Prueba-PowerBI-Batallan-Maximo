import pandas as pd
import numpy as np



#Rango etarioooo!!
today = '2023-01-11 05:00:00'

# dd/mm/YY




df = pd.read_csv('E:/maxib/back up/Codigo/Test Power BI/Test_PowerBi (1)/Data_Usuarios.csv', delimiter=',')

df['hoy'] = (today)


df['fechas_de_nacimiento'] = pd.to_datetime(df['fechas_de_nacimiento'], errors='coerce')
df = df.dropna(subset=['fechas_de_nacimiento'])





df[['hoy','fechas_de_nacimiento']] = df[['hoy','fechas_de_nacimiento']].apply(pd.to_datetime)

df['diff_days'] = (df['hoy'] - df['fechas_de_nacimiento']) / np.timedelta64(1, 'Y')

df['diff_days'] = df['diff_days'].astype(int)

df1 = df

df1 = df1[df1.diff_days > 17]

df1 = df1[df1.diff_days < 100]

df1['Menor a 30'] = df1['diff_days'].between(0, 30)

df1['Entre 31 - 40'] = df1['diff_days'].between(31, 40)

df1['Entre 41 - 50'] = df1['diff_days'].between(41, 50)

df1['Mayor a 51'] = df1['diff_days'].between(51, 106)

rangoetario = df1.drop(['fechas_de_nacimiento','ciudad','nivel_educativo', 'Sueldo','hoy','diff_days'], axis=1)


rangoetario['Menor a 30'] = np.where((rangoetario['Menor a 30'] == True),1,0)
rangoetario['Entre 31 - 40'] = np.where((rangoetario['Entre 31 - 40'] == True),1,0)
rangoetario['Entre 41 - 50'] = np.where((rangoetario['Entre 41 - 50'] == True),1,0)
rangoetario['Mayor a 51'] = np.where((rangoetario['Mayor a 51'] == True),1,0)



print(rangoetario)