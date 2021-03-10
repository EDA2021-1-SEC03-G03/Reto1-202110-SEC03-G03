import config as cf
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
               'country': None,
               'days': 0}

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

        category = categoryList['elements'][iterator]['category']

        if category_name in category:
            return categoryList['elements'][iterator]['id']
        iterator += 1


def addDays(catalogList, days):

    i = 0
    while i < lt.size(catalogList):

        if catalogList['elements'][i]['title'] in days:
            catalogList['elements'][i]['days'] += 1
        i += 1


# Funciones para creacion de datos

# Funciones de consulta


def loadDays(catalogList):

    catalogDays = lt.newList("ARRAY_LIST")

    i = 0
    while i < lt.size(catalogList):

        lt.addLast(catalogDays, catalogList['elements'][i]['title'])
        i += 1

    return catalogDays

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


def cmpVideosByDays(video1, video2):
    return (float(video1['days']) > float(video2['days']))


# Funciones de ordenamiento
def sortVideos(categoryList, catalogList, category_name, country, size):

    req1 = lt.newList("ARRAY_LIST")

    iD = traduceCategoryToId(categoryList, category_name)

    iterator = 0
    while iterator < (lt.size(catalogList)):
        catalogCountry = catalogList['elements'][iterator]['country']
        catalogId = catalogList['elements'][iterator]['category_id']

        if country in catalogCountry and iD in catalogId:
            lt.addLast(req1, catalogList['elements'][iterator])
        iterator += 1
    viewsList = shs.sort(req1, cmpVideosByViews)

    return viewsList


def sortVideosCountry(catalogList, country):

    req2 = lt.newList("ARRAY_LIST")

    iterator = 0
    while iterator < (lt.size(catalogList)):
        catalogCountry = catalogList['elements'][iterator]['country']

        if country in catalogCountry:
            lt.addLast(req2, catalogList['elements'][iterator])
        iterator += 1

    daysList = shs.sort(req2, cmpVideosByDays)

    return daysList
