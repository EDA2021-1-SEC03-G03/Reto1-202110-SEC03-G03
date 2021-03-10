﻿import config as cf
import model
import csv

# Inicialización de los Catálogos


def initCatalogVideos():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


def initCatalogCategories():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    category = model.newCategory()
    return category

# Funciones para la carga de datos


def loadDataVideos(catalog):
    """
    Carga los archivos y los datos en la estructura de datos
    """
    loadVideos(catalog)


def loadDataCategories(categories):
    """
    Carga los archivos y los datos en la estructura de datos
    """
    loadCategory(categories)


def loadVideos(catalog):
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideoInfo(catalog, video)


def loadCategory(catalog):
    categoriesfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)
# Funciones de ordenamiento


def sortVideos(catalog, category_name, country, size):
    return model.sortVideos(catalog, category_name, country, size)

# Funciones de consulta sobre el catálogo
