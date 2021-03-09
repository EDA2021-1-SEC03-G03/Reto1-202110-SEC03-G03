import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shs

assert cf

# Construccion de modelos


def newCatalog():
    catalog = {'trending_date': None,
               'title': None,
               'channel_title': None,
               'publish_time': None,
               'views': None,
               'likes': None,
               'dislikes': None}

    catalog['title'] = lt.newList("ARRAY_LIST")
    catalog['views'] = lt.newList("ARRAY_LIST",
                                  cmpfunction=cmpVideosByViews)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, title):
    lt.addLast(catalog['title'], title)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


# Funciones de ordenamiento
def sortVideos(catalog, category_name, country, size):

    sub_list = lt.subList(catalog['title'], 0, size)
    new_title = shs.sort(sub_list, cmpVideosByViews)

    return new_title
