import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import math #para comprobar valores vacios

def rank_tutores(codigo,nro_tutorados,ses_individuales,ses_grupales,referidos,atendidos,criterio): #ranking adicionado proximamente
    
  print("\n\nhello world\n\n")
  #ingresamos los datos dentro de un dataframe de pandas
  data = pd.DataFrame({"codigo":codigo, "nro_tutorados":nro_tutorados, "ses_individuales":ses_individuales,
                     "ses_grupales":ses_grupales, "referidos":referidos, "atendidos":atendidos,
                     "criterio":criterio})
  
  #reservamos el codigo de los tutores que no es neceario para la clasificacion, pero si para la identificacion de los rankings al final
  cod=data['codigo']

  #Quitamos la columna codigo del dataframe
  data = data.drop(['codigo'], axis = 1)

  #Normalizamos los datos para evitar sesgos
  data_norm = (data-data.min())/(data.max()-data.min())
  data=data_norm

  #Limpiamos contenido Nan del dataframe posiblemente provocado por la normalizacion
  for i in range(len(data.referidos)):
    if math.isnan(data.nro_tutorados[i]):
        data.nro_tutorados[i]=0
    if math.isnan(data.ses_individuales[i]):
        data.ses_individuales[i]=0
    if math.isnan(data.ses_grupales[i]):
        data.ses_grupales[i]=0
    if math.isnan(data.referidos[i]):
        data.referidos[i]=0
    if math.isnan(data.atendidos[i]):
        data.atendidos[i]=0
    if math.isnan(data.criterio[i]):
        data.criterio[i]=0

  """ aplicable posteriormente
  #Busqueda de clusters (elbow method)
  wcss = []

  for i in range(1,len(data.codigo)): #no exceder la cantidad de datos que tienes ya que no puedes hacer mas grupos de la cantidad de datos o personas que se tengan
      kmeans = KMeans(n_clusters = i, max_iter = 300)
      kmeans.fit(data)
      wcss.append(kmeans.inertia_)"""

  # aplicamos kmeans con el numero de clusters por defecto para esta version el cual es 5
  clustering = KMeans(n_clusters = 5, max_iter = 300)
  clustering.fit(data)

  #reservamos los clusters obtenidos en tutores_Clusters
  clusters={'tutores_Clusters':clustering.labels_}

  #el siguiente proceso nos permite redimensionar los parametros de los tutores en este caso a 2, su funcionalidad no afecta directamente al proceso de clasificacion por el momento
  from sklearn.decomposition import PCA #analisis de componentes principales , representacion de las variables en menor cantidad 2d
  dataf=data
  pca = PCA(n_components=2)
  pca_dataf = pca.fit_transform(dataf)
  pca_dataf_df = pd.DataFrame(data = pca_dataf, columns=['Componente_1','Componente_2'])
  pca_nombres_dataf = pd.concat([pca_dataf_df,pd.DataFrame(cod),pd.DataFrame(clusters)], axis=1)
   
  #Quitamos los componentes generados el el proceso anterior ya que no son relevantes por el momento
  rank_data = pca_nombres_dataf.drop(['Componente_1','Componente_2'], axis = 1)

  #el siguiente proceso nos almacenara los codigos de los tutores con sus respectivos rankings en pares "[codigo,ranking]"
  lista_return=[]
  for i in range(len(rank_data.codigo)):
    lista_return.append([rank_data.codigo[i],rank_data.tutores_Clusters[i]])
    
  print("\n\n todo listo funcione correctamente")

  return lista_return




def rank_tutorados(id,ciclo,tipo_beca): #ranking adicionado proximamente quitamos el parametro modalidad por el momento
  tipo_beca2=[]
  for c in tipo_beca:
    if(c=="beca permanencia"):
      tipo_beca2.append(1)
    if(c==""):
      tipo_beca2.append(0)
  
  """
  modalidad2=[]
  for c in modalidad:
      if(c=="primer ciclo"):
        modalidad2.append(1)
      if(c=="becario"):
        modalidad2.append(2)
      if(c=="observado"):
        modalidad2.append(3)
      if(c=="riesgo"):
        modalidad2.append(4)"""
 
  #ingresamos los datos dentro de un dataframe de pandas
  data = pd.DataFrame({"id":id, "ciclo":ciclo, "tipo_beca":tipo_beca2}) #eliminamos "modalidad":modalidad2
  
  #reservamos el codigo de los tutores que no es neceario para la clasificación, pero si para la identificación de los rankings al final
  cod=data['id']

  #Quitamos la columna codigo del dataframe
  data = data.drop(['id'], axis = 1)

  #Normalizamos los datos para evitar sesgos
  data_norm = (data-data.min())/(data.max()-data.min())
  data=data_norm

  #Limpiamos contenido Nan del dataframe posiblemente provocado por la normalizacion
  for i in range(len(data.ciclo)):
    if math.isnan(data.ciclo[i]):
        data.ciclo[i]=0
    if math.isnan(data.tipo_beca[i]):
        data.tipo_beca[i]=0
    """
    if math.isnan(data.modalidad[i]):
        data.modalidad[i]=0"""
   

  """ aplicable posteriormente
  #Busqueda de clusters (elbow method)
  wcss = []

  for i in range(1,len(data.codigo)): #no exceder la cantidad de datos que tienes ya que no puedes hacer mas grupos de la cantidad de datos o personas que se tengan
      kmeans = KMeans(n_clusters = i, max_iter = 300)
      kmeans.fit(data)
      wcss.append(kmeans.inertia_)"""

  # aplicamos kmeans con el numero de clusters por defecto para esta versión el cual es 5
  clustering = KMeans(n_clusters = 5, max_iter = 300)
  clustering.fit(data)

  #reservamos los clusters obtenidos en tutores_Clusters
  clusters={'tutorados_Clusters':clustering.labels_}

  #el siguiente proceso nos permite redimensionar los parámetros de los tutores en este caso a 2, su funcionalidad no afecta directamente al proceso de clasificacion por el momento
  from sklearn.decomposition import PCA #análisis de componentes principales , representación de las variables en menor cantidad 2d
  dataf=data
  pca = PCA(n_components=2)
  pca_dataf = pca.fit_transform(dataf)
  pca_dataf_df = pd.DataFrame(data = pca_dataf, columns=['Componente_1','Componente_2'])
  pca_nombres_dataf = pd.concat([pca_dataf_df,pd.DataFrame(cod),pd.DataFrame(clusters)], axis=1)

  #Quitamos los componentes generados el el proceso anterior ya que no son relevantes por el momento
  rank_data = pca_nombres_dataf.drop(['Componente_1','Componente_2'], axis = 1)

  #el siguiente proceso nos almacenara los codigos de los tutores con sus respectivos rankings en pares "[codigo,ranking]"
  lista_return=[]
  for i in range(len(rank_data.id)):
    lista_return.append([rank_data.id[i],rank_data.tutorados_Clusters[i]])

  return lista_return