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
vent_cat = []
cal_cat = []
env_cat = []

for i in range (1,5):
    sum_prec.append((df[f'{i}'].Precio.sum()))
    vent_cat.append((df[f'{i}']['Categoría del Producto'].value_counts()))
    cal_cat.append((df[f'{i}'].Calificación.mean().round(2)))
    env_cat.append((df[f'{i}']['Costo de envío'].mean().round(2)))



ganancias = pd.DataFrame({'Ganancia': sum_prec})
ganancias.index = [f'Tienda {i}' for i in range(1, 5)]
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

ventas = pd.concat(vent_cat, axis=1)
ventas.columns = [f'Tienda {i}' for i in range(1, 5)]
ventas

vent = ventas.plot(kind='barh', 
                   rot=0, 
                   xlabel = 'Unidades Vendidas',
                   title = 'Ventas por Categorias')
vent.invert_yaxis()

cal_env = pd.DataFrame({"Calificacion Promedio": cal_cat,
                        'Promedio envio':env_cat}, 
                       index= [f'Tienda {i}' for i in range(1, 5)])
cal_env.rename_axis("Tienda", inplace = T) 

cal_env.reset_index().plot(kind='scatter',
                                x='Tienda',
                                y="Calificacion Promedio",
                                marker='^',
                                color='green',
                                s=150)

ventas.transpose().apply(lambda x: x*100/sum(x), axis=1).plot(kind="barh", stacked=True)
plt.title("Porcentaje de productos vendidos")
plt.ylabel("Tienda")
plt.xlabel("Ventas (%)")
plt.legend(
    title="Categoría del Producto",
    bbox_to_anchor=(1, 0.75),   # Posición: ligeramente a la derecha
    loc='upper left')            # Ubicación relativa del ancla)
plt.show()

ex = sns.barplot(cal_env.reset_index(), 
                x = 'Tienda',
                y='Promedio envio',
                palette="hls",
                errorbar=None)
for container in ex.containers:
        ex.bar_label(container, fmt='%.2f') # Format labels to two decimal places
