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
               'likes': 0,
               'dislikes': 0,
               'country': None}

    catalog['trending_date'] = lt.newList("ARRAY_LIST")
    catalog['title'] = lt.newList("ARRAY_LIST")
    catalog['channel_title'] = lt.newList("ARRAY_LIST")
    catalog['category_id'] = lt.newList("ARRAY_LIST")
    catalog['publish_time'] = lt.newList("ARRAY_LIST")
    catalog['tags'] = lt.newList("ARRAY_LIST")
    catalog['views'] = lt.newList("ARRAY_LIST",
                                  cmpfunction=cmpVideosByViews)
    catalog['likes'] = lt.newList("ARRAY_LIST")
    catalog['dislikes'] = lt.newList("ARRAY_LIST")
    catalog['country'] = lt.newList("ARRAY_LIST")

    return catalog


def newCategory():
    category = {'id': None,
                'category': None}

    category['id'] = lt.newList("ARRAY_LIST")
    category['category'] = lt.newList("ARRAY_LIST")

    return category


# Funciones para agregar informacion al catalogo


def addVideoInfo(catalog, video):
    lt.addLast(catalog['trending_date'], video['trending_date'])
    lt.addLast(catalog['title'], video['title'])
    lt.addLast(catalog['channel_title'], video['channel_title'])
    lt.addLast(catalog['category_id'], video['category_id'])
    lt.addLast(catalog['publish_time'], video['publish_time'])
    lt.addLast(catalog['tags'], video['tags'])
    lt.addLast(catalog['views'], float(video['views']))
    lt.addLast(catalog['likes'], int(video['likes']))
    lt.addLast(catalog['dislikes'], int(video['dislikes']))
    lt.addLast(catalog['country'], video['country'])


def addCategory(catalog, category):
    lt.addLast(catalog['id'], category)
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (float(video1) > float(video2))


# Funciones de ordenamiento
def sortVideos(catalog, category_name, country, size):   
    '''
    if catalog['country'] == country:
        # obtener la pos
        lt.deleteElement(catalog['title'], pos)

    sub_list = lt.subList(catalog['title'], 0, size)
    '''
    # if catalog[''] == category_name:

    new_title = shs.sort(catalog['views'], cmpVideosByViews)

    return new_title
