import random
import string
class nodoPila():
    """crea una variable nodo pila"""
    def __init__(self):
        self.info, self.sig = None, None


class Pila():
    """Crear una pila vacia"""
    def __init__(self):
        self.tamanio = 0
        self.cima = None


def apilar(pila, dato):
    """apila el dato en la cima"""
    nodo = nodoPila()
    nodo.info = dato 
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1


def desapilar(pila):
    dato = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return dato


def pila_vacia(pila):
    return pila.cima is None


def tamanio(pila):
    return pila.tamanio


def cima(pila):
    return pila.cima.info

def pilaint(pila, cant):
    '''Carga una pila con numeros enteros randomicos'''
    for i in range(0, cant):
        apilar(pila, random.randint(0, 10))

def barrido_pila(pila):
    '''Muestra los elementos de una pila'''
    paux = Pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))

def ordenar_pila(pila):
    '''Ordena una pila de forma creciente'''
    paux = Pila()
    while not pila_vacia(pila):
        c = 0
        dato = desapilar(pila)
        while not pila_vacia(paux) and cima(paux) <= dato:
            apilar(pila, desapilar(paux))
            c += 1
        apilar(paux, dato)
        for i in range(0, c):
            apilar(paux, desapilar(pila))
    return paux
