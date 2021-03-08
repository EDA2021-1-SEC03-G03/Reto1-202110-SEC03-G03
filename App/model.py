import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shs

assert cf

# Construccion de modelos


def newCatalog():
    catalog = {'title': None,
               'channel_title': None}

    catalog['title'] = lt.newList("ARRAY_LIST")
    catalog['channel_title'] = lt.newList("ARRAY_LIST",
                                          cmpfunction=compareChannelTitle)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, title):
    lt.addLast(catalog['title'], title)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def compareChannelTitle(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


# Funciones de ordenamiento
def sortVideos(catalog, size):
    start_time = time.process_time()
    sub_list = lt.subList(catalog['title'], 0, size)
    new_title = shs.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, new_title
