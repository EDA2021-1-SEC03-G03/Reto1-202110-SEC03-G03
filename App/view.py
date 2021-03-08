import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ordenar los libros por views")
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


def pregunta1():
    print("Seleccione la estructura de datos")
    print("1- ARRAY_LIST")
    print("2- LINKED_LIST")


def pregunta2():
    print("Seleccione el metodo de ordenamiento")
    print("1- Quick Sort")
    print("2- Merge Sort")
    print("3- Selection Sort")
    print("4- Insertion Sort")
    print("5- Shell Sort")


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        pregunta1()
        tad = int(input())
        print("Cargando información de los archivos ....")
        new_type = 0
        if tad == 1:
            new_type = "ARRAY_LIST"
            catalog = initCatalog(new_type)
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['title'])))
        elif tad == 2:
            new_type == "LINKED_LIST"
            catalog = initCatalog(new_type)
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['title'])))
        else:
            print("No hizo una selección válida, por favor intente nuevamente a continuacion:\n")

    elif int(inputs) == 2:
        size = int(input("Indique el tamaño de la muestra: "))
        pregunta2()
        iterable_ord = int(input())
        new_order = 0
        if iterable_ord == 1:
            new_order = "quicksort"
            result = controller.sortVideos(catalog, size, new_order)
            printResults(result[1], size)
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                  str(result[0]))
        elif iterable_ord == 2:
            new_order = "mergesort"
            result = controller.sortVideos(catalog, size, new_order)
            printResults(result[1], size)
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                  str(result[0]))
        elif iterable_ord == 3:
            new_order = "selectionsort"
            result = controller.sortVideos(catalog, size, new_order)
            printResults(result[1], size)
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                  str(result[0]))
        elif iterable_ord == 4:
            new_order = "insertionsort"
            result = controller.sortVideos(catalog, size, new_order)
            printResults(result[1], size)
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                  str(result[0]))
        elif iterable_ord == 5:
            new_order = "shellsort"
            result = controller.sortVideos(catalog, size, new_order)
            printResults(result[1], size)
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                  str(result[0]))
        else:
            print("No hizo una selección válida, por favor intente nuevamente a continuacion:\n")

    else:
        sys.exit(0)
sys.exit(0)
