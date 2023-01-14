import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#codigo,nro tutorados, ses individuales, ses grupales, referidos, atendidos, criterio
tutores=[[970478, 70398213, 41268129, 299128, 2130463, 2130447, 2121009, 2008918],
         [6,         5,          5,     6,      5,        6,        5,         6],
         [12,        13,        11,     5,      15 ,      4 ,       9,         0],
         [0,          0,        0,      0,       1,        1,       0,         1],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [4,         3,         4,      2,       4,       3 ,       0,         0]]

data = pd.DataFrame({"codigo":tutores[0], "nro_tutorados":tutores[1], "ses_individuales":tutores[2],
                     "ses_grupales":tutores[3], "referidos":tutores[4], "atendidos":tutores[5],
                     "criterio":tutores[6]})

data = data.drop(['codigo'], axis = 1)

data.describe()

#normalizacion primero probar sin esto
data_norm = (data-data.min())/(data.max()-data.min())

data=data_norm
data.describe()

type(data.referidos[1])

len(data.referidos)

for i in range(len(data.referidos)):
    if(data.referidos[i] is not int):
        data.referidos[i]=0
    if(data.atendidos[i] is not int):
        data.atendidos[i]=0
        
#Busqueda de clusters
wcss = []

for i in range(1,8): #no exceder la cantidad de datos que tienes ya que no puedes hacer mas grupos de la cantidad de datos o personas que se tengan
    kmeans = KMeans(n_clusters = i, max_iter = 300)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

#el número optimo de clasificaciones segun la grafica es de 2
plt.plot(range(1,8), wcss)
plt.title("codo de jambu")
plt.xlabel('número e clusters')
plt.ylabel('WCSS')
plt.show()

# aplicamos kmeans con el numero de clusters realizado
clustering = KMeans(n_clusters = 4, max_iter = 300)
clustering.fit(data)

data['tutores_Clusters'] = clustering.labels_
data.head()

from sklearn.decomposition import PCA #análisis de componentes principales , representación de las variables en menor cantidad 2d
dataf=data
pca = PCA(n_components=2)
pca_dataf = pca.fit_transform(dataf)
pca_dataf_df = pd.DataFrame(data = pca_dataf, columns=['Componente_1','Componente_2'])
pca_nombres_dataf = pd.concat([pca_dataf_df, dataf[['tutores_Clusters']]], axis=1)

pca_nombres_dataf

fig = plt.figure(figsize = (6,6))

ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Componente_1', fontsize = 15)
ax.set_ylabel('Componente_2', fontsize = 15)
ax.set_title('componentes principales', fontsize = 20)

color_theme = np.array(["blue", "green", "orange", "black", "yellow"])
ax.scatter(x= pca_nombres_dataf.Componente_1, y=pca_nombres_dataf.Componente_2, c=color_theme[pca_nombres_dataf.tutores_Clusters], s = 50)