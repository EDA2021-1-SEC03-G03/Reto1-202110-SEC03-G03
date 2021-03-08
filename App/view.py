import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Conocer los videos tendencia en un país y caterogía específica")
    print("0- Salir")


def initCatalog(tad):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tad)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def printResults(ord_books, sample):
    size = lt.size(ord_books)
    if size == sample:
        print("Los primeros ", str(sample), " libros ordenados son: ")
        i = 1
        while i <= sample:
            book = lt.getElement(ord_books, i)
            print('Titulo: ' + book['title'] + ' views: ' + book['views'])
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
        print('Videos cargados: ' + str(lt.size(catalog['title'])))

    elif int(inputs) == 2:
        size = int(input("Indique el tamaño de la muestra: "))
        result = controller.sortVideos(catalog, size)
        printResults(result[1], size)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
              str(result[0]))

    else:
        sys.exit(0)
sys.exit(0)
