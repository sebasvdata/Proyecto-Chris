import pandas as pd

#Cargar archivo con los datos de criminalidad de 2022

df = pd.read_csv("C:/Users/Usuario/Desktop/Proyectos Chris/Datos criminalidad.csv", sep=";")
df_2022 = df[df["Año"] == 2022].copy()

print(df_2022.head())
print(df_2022.info())

#Cambiar formato de los números para quitar el ".", ejemplo: 1.000 pasarlo a 1000

columnas = ["Año", "Total",'Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
for col in columnas:
    df_2022[col] = df_2022[col].astype(str).str.replace('.', '', regex=False).astype(int)
print(df_2022.head())

top5 = df_2022.groupby("Zona")["Total"].sum().sort_values(ascending=False)
print(top5)

#Cargar archivo de datos de nacionalidad

df_nacionalidad = pd.read_csv("C:/Users/Usuario/Desktop/Proyectos Chris/criminalidad 2022.csv",sep=";", encoding="UTF 8")
df_nacionalidad = df_nacionalidad.loc[:,["Nacionalidad", "Total"]]
print(df_nacionalidad)

#Guardar archivos

df_2022.to_csv("C:/Users/Usuario/Desktop/Proyectos Chris/(Terminado) Datos criminalidad Madrid 2022.csv")
top5.to_csv("C:/Users/Usuario/Desktop/Proyectos Chris/(Terminado) Top 5 criminalidad Madrid 2022.csv")
df_nacionalidad.to_csv("C:/Users/Usuario/Desktop/Proyectos Chris/(Terminado) Nacionalidad criminalidad Madrid 2022.csv")