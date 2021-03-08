import config as cf
import model
import csv

# Inicialización del Catálogo de libros


def initCatalog(tad):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(tad)
    return catalog

# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los archivos y los datos en la estructura de datos
    """
    loadVideos(catalog)


def loadVideos(catalog):
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

# Funciones de ordenamiento


def sortVideos(catalog, size, iterable_ord):
    return model.sortVideos(catalog, size, iterable_ord)

# Funciones de consulta sobre el catálogo
