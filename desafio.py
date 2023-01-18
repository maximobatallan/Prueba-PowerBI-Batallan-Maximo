import pandas as pd


df = pd.read_csv('E:/maxib/back up/Codigo/Test Power BI/Test_PowerBi (1)/Cursos_Usuarios.csv')
df1 = df.groupby('id_usuario').sum()
df1 = df1.sort_values(by=['Minutos en pantalla'], ascending=False)
summin = df['Minutos en pantalla'].sum()

df1['Porcentaje en pantalla'] = (df1['Minutos en pantalla']/summin)*100

df1['Porcentaje en pantalla'] = df1['Porcentaje en pantalla'].round(decimals = 2)

df1['id_usuario'] = df1.index.get_level_values('id_usuario') 

df1 = df1.head(10)






