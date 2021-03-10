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
               'country': None}

    return catalog


def newCategory():
    category = {'id': None,
                'category': None}

    category['id'] = lt.newList("ARRAY_LIST")
    category['category'] = lt.newList("ARRAY_LIST")

    return category


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


def addCategory(catalog, category):
    lt.addLast(catalog["id"], category)


def traduceCategoryToId(category_cat, cataloglist, category):
    print(category_cat)
    category_pos = lt.isPresent(category_cat['category'], category)
    print(category_pos)
    category_id = lt.getElement(category_cat['id'], category_pos)
    return category_id['id']

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


# Funciones de ordenamiento
def sortVideos(categories_cat, catalogList, category_name, country, size):
    '''
    if catalog['country'] == country:
        # obtener la pos
        lt.deleteElement(catalog['title'], pos)

    sub_list = lt.subList(catalog['title'], 0, size)
    '''
    print(traduceCategoryToId(categories_cat, catalogList, category_name))
    new_title = shs.sort(catalogList, cmpVideosByViews)

    return new_title
