import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

T = True
F = False

url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

urls = {'1': url1,
        '2': url2,
        '3': url3,
        '4': url4}

# Diccionario para almacenar los DataFrames
df = {}

# Lectura de los archivos CSV
for name, url in urls.items():
    df[name] = pd.read_csv(url)

# Acceso: dataframes['st1'], dataframes['st2'], etc.

sum_prec = []

for i in range (1,5):
    sum_prec.append((df[f'{i}'].Precio.sum()))
    ganancias = pd.DataFrame({'Ganancia': sum_prec})

ganancias.rename(index={0: "Tienda 1",
                        1: "Tienda 2",
                        2: "Tienda 3",
                        3: "Tienda 4"}, inplace=T )

ganancias.rename_axis("Tienda", inplace = T) 

sns.set_style("whitegrid") # Set style for chart
fig, ax = plt.subplots()
ax.ticklabel_format(style='plain')
ax.bar( ganancias.index, 
       ganancias.Ganancia,
       color = sns.color_palette("Set2"))
for i in range(len(ganancias.Ganancia)):
        plt.text(i-0.35, ganancias.Ganancia[i], ganancias.Ganancia[i])  # Placing text slightly above the bar

bx = ganancias.plot(kind="bar", 
               title='Ganacias de Cada Tienda', 
               xlabel='Tienda Individual',
               ylabel='Porcentaje',
               legend=F)
bx.ticklabel_format(style='plain', axis='y')


sns.set_style("whitegrid") # Set style for chart
plt.figure(figsize=(6,6)) # Set figure size
plt.pie(ganancias.Ganancia,
        colors = sns.color_palette("Set2"),
        explode = [0.1, 0 , 0, 0],
        labels = ganancias.index,
        autopct ='%.2f%%')
