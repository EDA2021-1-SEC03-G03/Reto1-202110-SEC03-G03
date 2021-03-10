import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Conocer los videos con más views que son tendencia en un país")
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
    controller.loadDataCategories(catalog)


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
    for index in categories['id']['elements']:
        print('\tID: [' + str(index['id']) +
              ']\tCategoria: [' + index['name'] + ']')


def printResultsReq1(ord_videos, size):

    print("Los primeros ", str(size), " videos ordenados son: ")
    i = 1
    while i <= size:
        video = lt.getElement(ord_videos, i)
        print('\t[Trending date: ', video['trending_date'],
              ']\t[Title: ', video['title'],
              ']\t[Channel title: ', video['channel_title'],
              ']\t[Publish time: ', video['publish_time'],
              ']\t[Views: ', video['views'],
              ']\n\tLikes: [', video['likes'],
              ']\t[Dislikes: ', video['dislikes'],
              ']')
        i += 1


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
        loadDataCategories(categories)
        printCategories(categories)

    elif int(inputs) == 2:
        category_name = input("Indique el nombre de la categoria: ")
        country = input("Indique el país a consultar: ")
        size = int(input("Indique el tamaño de la lista de videos: "))
        result = controller.sortVideos(catalogList, category_name,
                                       country, size)
        printResultsReq1(result, size)

    else:
        sys.exit(0)
sys.exit(0)
