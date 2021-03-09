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


def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def printResults(ord_videos):
    print("La información del primer video cargado es: ")
    video = lt.getElement(ord_videos, 1)
    print('\tTitle: [' + video['title'] +
          ']\n\tChannel title: [' + video['channel_title'] +
          ']\n\tTrending date: [' + video['trending_date'] +
          ']\n\tCountry: [' + video['country'] +
          ']\n\tViews: [' + video['views'] +
          ']\n\tLikes: [' + video['likes'] +
          ']\n\tDislikes: [' + video['dislikes'])


def printResultsReq1(ord_videos, size):
    tam = lt.size(ord_videos)
    if tam == size:
        print("Los primeros ", str(size), " libros ordenados son: ")
        i = 1
        while i <= size:
            video = lt.getElement(ord_videos, i)
            print('\t[Trending date: ' + video['trending_date'] +
                  ']\t[Title: ' + video['title'] +
                  ']\t[Channel title: ' + video['channel_title'] +
                  ']\t[Publish time: ' + video['publish_time'] +
                  ']\t[Views: ' + video['views'] +
                  ']\n\tLikes: [' + video['likes'] +
                  ']\t[Dislikes: ' + video['dislikes'])
            i += 1


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        catalog = initCatalog()
        loadData(catalog)
        print("Cargando información de los archivos ....")
        print('Videos cargados: ' + str(lt.size(catalog['title'])))
        printResults(catalog['title'])

    elif int(inputs) == 2:
        category_name = input("Indique el nombre de la categoria: ")
        country = input("Indique el país a consultar: ")
        size = int(input("Indique el tamaño de la lista de videos: "))
        result = controller.sortVideos(catalog, category_name, country, size)
        printResultsReq1(result, size)

    else:
        sys.exit(0)
sys.exit(0)
