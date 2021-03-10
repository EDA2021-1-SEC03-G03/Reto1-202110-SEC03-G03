﻿import config as cf
# import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.DataStructures import arraylistiterator as it
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

    return catalog


def newCategory():
    category = {'id': None,
                'category': None}

    return category


def newCategoryList():
    categoryList = lt.newList("ARRAY_LIST")
    return categoryList


def newCatalogList():

    catalogList = lt.newList("ARRAY_LIST")

    return catalogList


# Funciones para agregar informacion al catalogo


def addVideoInfo(catalog, video):

    cg = catalog.copy()

    cg['trending_date'] = video['trending_date']
    cg['title'] = video['title']
    cg['channel_title'] = video['channel_title']
    cg['category_id'] = video['category_id']
    cg['publish_time'] = video['publish_time']
    cg['tags'] = video['tags']
    cg['views'] = float(video['views'])
    cg['likes'] = int(video['likes'])
    cg['dislikes'] = int(video['dislikes'])
    cg['country'] = video['country']

    return cg


def addVideo(catalogList, cg):
    lt.addLast(catalogList, cg)


def addCategory(catalog, cl):
    lt.addLast(catalog, cl)


def addCategoryInfo(catalog, category):
    cl = catalog.copy()

    cl['id'] = category['id']
    cl['category'] = category['name']

    return cl


def traduceCategoryToId(categoryList, category_name):
    iterator = 0
    while iterator < (lt.size(categoryList)):
        if str(categoryList[iterator['category']]) == category_name:
            return categoryList[iterator['id']]

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


# Funciones de ordenamiento
def sortVideos(categoryList, catalogList, category_name, country, size):
    '''
    if catalog['country'] == country:
        # obtener la pos
        lt.deleteElement(catalog['title'], pos)

    sub_list = lt.subList(catalog['title'], 0, size)
    '''
    print(traduceCategoryToId(categoryList, category_name))
    new_title = shs.sort(catalogList, cmpVideosByViews)

    return new_title
