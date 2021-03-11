import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylistiterator as it
assert cf


def printMenu():
    print("\nBienvenido")
    print("\t1. Cargar información en el catálogo")
    print("\t2. Conocer los videos con más views que son tendencia en un país")
    print("\t3. Conocer el video que más días ha sido trending en un país")
    print("\t4. Conocer el video que más días ha sido trending en una",
          "categoria")
    print("\t5. Conocer los videos con más likes en un país y con un tag",
          "determinado")
    print("\t0. Salir")


def initCatalogVideos():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalogVideos()


def initCatalogCategories():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalogCategories()


def loadDataVideos(catalog):
    """
    Carga los libros en la estructura de datos
    """
    catalogList = controller.loadDataVideos(catalog)

    return catalogList


def loadDataCategories(catalog):
    """
    Carga los libros en la estructura de datos
    """
    categoryList = controller.loadDataCategories(catalog)

    return categoryList


def printVideos(videos):
    print("\nLa información del primer video cargado es: ")
    video = lt.getElement(videos, 1)
    print('\tTrending date: [', video['trending_date'],
          ']\n\tTitle: [', video['title'],
          ']\n\tChannel title: [', video['channel_title'],
          ']\n\tPublish time: [', video['publish_time'],
          ']\n\tViews: [', video['views'],
          ']\n\tLikes: [', video['likes'],
          ']\n\tDislikes: [', video['dislikes'],
          ']')


def printCategories(categories):
    print('\nLa informacion de las categorias es: ')
    iterator = it.newIterator(categories)
    while it.hasNext(iterator):
        pos = it.next(iterator)
        print('\tID: [', pos['id'],
              ']\tCategoria: [', pos['category'],
              ']')


def printResultsReq1(video, size):

    print("\nLos primeros", str(size), "videos ordenados son: ")
    i = 0
    while i < size:
        print('\nVideo:', i + 1)
        print('\n\tTrending date: [', video[i]['trending_date'],
              ']\n\tTitle: [', video[i]['title'],
              ']\n\tChannel title: [', video[i]['channel_title'],
              ']\n\tPublish time: [', video[i]['publish_time'],
              ']\n\tViews: [', video[i]['views'],
              ']\n\tikes: [', video[i]['likes'],
              ']\n\tDislikes: [', video[i]['dislikes'],
              ']')
        i += 1


def printResultsReq2(video, country):

    print("\nEl video más trending para", country, "fue: ")

    print('\tTitle: [', video[0]['title'],
          ']\n\tChannel title: [', video[0]['channel_title'],
          ']\n\tCountry: [', video[0]['country'],
          ']')


def printResultsReq3(video, category):

    print("\nEl video mas trending para ", str(category), " es: ")

    print('\tTitle: [', video[0]['title'],
          ']\n\tChannel title: [', video[0]['channel_title'],
          ']\n\tcountry: [', video[0]['category_id'],
          ']\n\tNumber of days: [', video[0]['days'],
          ']')


def printResultsReq4(video, size, tag):

    print("Los", str(size), "videos con más likes para el tag", tag, "son: ")
    i = 0
    while i < size:
        print('\nVideo:', i + 1)
        print('\tTitle: [', video[i]['title'],
              ']\n\tChannel title: [', video[i]['channel_title'],
              ']\n\tPublish time: [', video[i]['publish_time'],
              ']\n\tViews: [', video[i]['views'],
              ']\n\tLikes: [', video[i]['likes'],
              ']\n\tDislikes: [', video[i]['dislikes'],
              ']\n\tTags: [', video[i]['tags'], ']')
        i += 1


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('\nSeleccione una opción para continuar:\n')
    if int(inputs) == 1:
        print("\nCargando información de los archivos ....")
        videos = initCatalogVideos()
        catalogList = loadDataVideos(videos)
        print('\tVideos cargados: ' + str(lt.size(catalogList)))
        printVideos(catalogList)

        categories = initCatalogCategories()
        categoryList = loadDataCategories(categories)
        printCategories(categoryList)

    elif int(inputs) == 2:
        category_name = input("Indique el nombre de la categoria: ")
        country = input("Indique el país a consultar: ")
        size = int(input("Indique el tamaño de la lista de videos: "))
        result = controller.sortVideos(categoryList, catalogList,
                                       category_name, country, size)
        printResultsReq1(result['elements'], size)

    elif int(inputs) == 3:
        country = input("Indique el nombre del país: ")

        controller.loadDays(catalogList)
        result = controller.sortVideosCountry(catalogList, country)

        printResultsReq2(result['elements'], country)

    elif int(inputs) == 4:
        category_name = input("Indique el nombre de la categoria: ")

        controller.loadDays(catalogList)
        result = controller.sortVideosCategory(categoryList, catalogList,
                                               category_name)
        printResultsReq3(result['elements'], category_name)

    elif int(inputs) == 5:
        country = input("Indique el nombre del país: ")
        tag_name = input("Indique el nombre del tag: ")
        size = int(input("Indique el tamaño de la lista de videos: "))

        result = controller.sortVideosTags(catalogList, tag_name,
                                           country)
        printResultsReq4(result['elements'], size, tag_name)

    else:
        sys.exit(0)
sys.exit(0)
