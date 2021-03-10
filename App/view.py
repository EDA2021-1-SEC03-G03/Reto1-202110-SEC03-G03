import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylistiterator as it
assert cf


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Conocer los videos con más views que son tendencia en un país")
    print("3- Conocer el video que más días ha sido trending en un país")
    print("4- Conocer el video que más días ha sido trending en una categoria")
    print("0- Salir")


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
    print("La información del primer video cargado es: ")
    video = lt.getElement(videos, 1)
    print('\t[Trending date: ', video['trending_date'],
          ']\t[Title: ', video['title'],
          ']\t[Channel title: ', video['channel_title'],
          ']\t[Publish time: ', video['publish_time'],
          ']\t[Views: ', video['views'],
          ']\n\tLikes: [', video['likes'],
          ']\t[Dislikes: ', video['dislikes'],
          ']')


def printCategories(categories):
    print('\nLa informacion de las categorias es: ')
    iterator = it.newIterator(categories)
    while it.hasNext(iterator):
        pos = it.next(iterator)
        print('\tID: [', pos['id'],
              ']\tCategoria: [', pos['category'], ']')


def printResultsReq1(video, size):

    print("Los primeros ", str(size), " videos ordenados son: ")
    i = 0
    while i < size:
        print('\t[Trending date: ', video[i]['trending_date'],
              ']\t[Title: ', video[i]['title'],
              ']\t[Channel title: ', video[i]['channel_title'],
              ']\t[Publish time: ', video[i]['publish_time'],
              ']\t[Views: ', video[i]['views'],
              ']\n\tLikes: [', video[i]['likes'],
              ']\t[Dislikes: ', video[i]['dislikes'],
              ']')
        i += 1


def printResultsReq2(video, country):

    print("El video más trending para", country, "fue: ")

    print('\t[Title: ', video[0]['title'],
          ']\t[Channel title: ', video[0]['channel_title'],
          ']\t[country: ', video[0]['country'],
          ']\t[Number of days: ', video[0]['days'],
          ']')


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        print("Cargando información de los archivos ....")
        videos = initCatalogVideos()
        catalogList = loadDataVideos(videos)
        print('Videos cargados: ' + str(lt.size(catalogList)))
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

    else:
        sys.exit(0)
sys.exit(0)
