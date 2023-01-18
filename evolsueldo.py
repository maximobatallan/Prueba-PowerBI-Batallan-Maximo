import pandas as pd
import numpy as np



#Rango etarioooo!!
today = '2023-01-11 05:00:00'

# dd/mm/YY




evolucionsueldo = pd.read_csv('E:/maxib/back up/Codigo/Test Power BI/Test_PowerBi (1)/Data_Usuarios.csv', delimiter=',')

evolucionsueldo['hoy'] = (today)


evolucionsueldo['fechas_de_nacimiento'] = pd.to_datetime(evolucionsueldo['fechas_de_nacimiento'], errors='coerce')
evolucionsueldo = evolucionsueldo.dropna(subset=['fechas_de_nacimiento'])





evolucionsueldo[['hoy','fechas_de_nacimiento']] = evolucionsueldo[['hoy','fechas_de_nacimiento']].apply(pd.to_datetime)

evolucionsueldo['diff_days'] = (evolucionsueldo['hoy'] - evolucionsueldo['fechas_de_nacimiento']) / np.timedelta64(1, 'Y')

evolucionsueldo['diff_days'] = evolucionsueldo['diff_days'].astype(int)

evolucionsueldo = evolucionsueldo
evolucionsueldo = evolucionsueldo[evolucionsueldo.diff_days > 17]

evolucionsueldo = evolucionsueldo[evolucionsueldo.diff_days < 100]

print(evolucionsueldo.describe())
evolucionsueldo = evolucionsueldo[['id_usuario', 'fechas_de_nacimiento', 'ciudad', 'nivel_educativo','Sueldo']]
evolucionsueldo.to_csv('evol.csv')


print(evolucionsueldo)