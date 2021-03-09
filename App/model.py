import config as cf
# import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shs

assert cf

# Construccion de modelos


def newCatalog():
    '''
    video_id
    trending_date
    title
    channel_title
    category_id
    publish_time
    tags
    views
    likes
    dislikes
    comment_count
    thumbnail_link
    comments_disabled
    ratings_disabled
    video_error_or_removed
    description
    country
    '''
    catalog = {'trending_date': None,
               'title': None,
               'channel_title': None,
               'category_id': None,
               'publish_time': None,
               'tags': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'country': None}

    catalog['title'] = lt.newList("ARRAY_LIST")
    catalog['views'] = lt.newList("ARRAY_LIST",
                                  cmpfunction=cmpVideosByViews)
    catalog['country'] = lt.newList("ARRAY_LIST")
    catalog['category_id'] = lt.newList("ARRAY_LIST")

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, title):
    lt.addLast(catalog['title'], title)


def addCategory(catalog, category):
    lt.addLast(catalog['category_id'], category)
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


# Funciones de ordenamiento
def sortVideos(catalog, category_name, country, size):

    sub_list = lt.subList(catalog['title'], 0, size)

    # if catalog[''] == category_name:

    new_title = shs.sort(sub_list, cmpVideosByViews)

    return new_title
