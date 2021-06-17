from TDA_pila import pila_llena, pila_vacia, desapilar, apilar, tamanio, cima, Pila
import random
'''
HAY ALGUNOS EJERCICIOS QUE ME TRABE Y NO SE SI FUNCIONAN, Y ALGUNOS 
TIENEN COMANDOS QUE NO LOS DIMOS PERO LOS BUSQUE POR INTERNET, 
PERDON POR LA DEMORA
'''
p = Pila()

def carga_automatica(pila):
    while not pila_llena(pila):
        dato = random.randint(0, 5)
        apilar(pila, dato)

carga_automatica(p)

def mostrar(pila):
    paux = Pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))
    print('pila cargada')

mostrar(p)

# EJERCICIO 1
def ocurrencias(p, elem):
    cont = 0
    aux = 0
    pila_aux = Pila()
    while not pila_vacia(p):
        aux = desapilar(p)
        if elem == aux:
            cont += 1
        apilar(pila_aux, aux)
    while not pila_vacia(pila_aux):
        apilar(p, desapilar(pila_aux))
    if cont == 0:
        print("El elemento no existe")
    else:
        print("La cantidad de ocurrencias son: ", cont)

ocurrencias(p, 5)

# EJERCICIO 2
def pares(p):
    pila_aux = Pila()
    aux = 0
    while not pila_vacia(p):
        aux = desapilar(p)
        if (aux % 2) == 0:
            apilar(pila_aux, aux)
    while not pila_vacia(pila_aux):
        apilar(p, desapilar(pila_aux))
    print('Los pares de esta pila son: ')
    mostrar(p)

pares(p)

# EJERCICIO 3
def ocurrencias(p, elemento):
    cont = 0
    aux = 0
    pila_aux = Pila()
    while not pila_vacia(p):
        aux = desapilar(p)
        if elemento == aux:
            cont += 1
            aux = int(input("Ingrese un numero para reemplazar por la ocurrencia"))
        apilar(pila_aux, aux)
    while not pila_vacia(pila_aux):
        apilar(p, desapilar(pila_aux))
    if cont == 0:
        print("El elemento no existe en la pila")

ocurrencias(p, 3)

# EJERCICIO 4
def invertir(p):
    pila_aux = Pila()
    print('lla Pila original es: ')
    mostrar(p)
    while not pila_vacia(p):
        apilar(pila_aux, desapilar(p))
    print('la Pila invertida es: ')
    mostrar(pila_aux)

invertir(p)

# EJERCICIO 5('Funciona pero la pila con la que trabaje es de numeros enteros')
def palindromo(palabra):
    p = Pila()
    aux = len(palabra)
    palabra_aux = ''
    for i in range(0, aux):
        car = palabra[i]
        apilar(p, car)
    while not pila_vacia(p):
        palabra_aux = palabra_aux + desapilar(p)
    if palabra == palabra_aux:
        print("La palabra es palindromo")

#palindromo(p)

# EJERCICIO 6//Mismo problema que en el ejercicio anterior
def palabra_inverza(palabra):
    p = Pila()
    aux = len(palabra)
    palabra_aux = ''
    for i in range(0, aux):
        car = palabra[i]
        apilar(p, car)
    while not pila_vacia(p):
        palabra_aux = palabra_aux + desapilar(p)
    print(palabra_aux)

#palabra_inverza(software)

# EJERCICIO 7
def eliminar(p, pos):
    pila_aux = Pila()
    for i in range(0, pos):
        apilar(pila_aux, desapilar(p))
    desapilar(p)
    while not pila_vacia(pila_aux):
        apilar(p, desapilar(pila_aux))

eliminar(p, 3)

# EJERCICIO 8
def ordenar_pila(p):
    aux = Pila()
    while not pila_vacia(p):
        cont = 0
        dato = desapilar(p)
        while not pila_vacia(aux) and (cima(aux) >= dato):
            apilar(p, desapilar(aux))
            cont += 1
        apilar(aux, dato)
        for i in range(0, cont):
            apilar(aux, desapilar(p))
    return aux

ordenar_pila(p)    

def cartas():
    p = Pila()
    po = Pila()
    pb = Pila()
    pe = Pila()
    pc = Pila()
    palos = ['Oro', 'Basto', 'Copa', 'Espada']
    while not pila_llena(p):
        num = random.randint(1, 13)
        palo = random.choice(palos)
        apilar(p, [num, palo])
    while not pila_vacia(p):
        aux = desapilar(p)
        if aux[1] == "Basto":
            apilar(pb, aux)
        if aux[1] == "Copa":
            apilar(pc, aux)
        if aux[1] == "Oro":
            apilar(po, aux)
        if aux[1] == "Espada":
            apilar(pe, aux)
    print("Mazo de basto")
    mostrar(pb)
    print("Mazo de copa")
    mostrar(pc)
    print("Mazo de oro")
    mostrar(po)
    print("Mazo de espada")
    mostrar(pe)
    pe = ordenar_pila(pe)
    print("Mazo de espada ordenados")
    mostrar(pe)

cartas()

# EJERCICIO 9
def factorial(n):
    p = Pila()
    aux = 1
    for i in range(1, n+1):
        apilar(p, i)
    while not pila_vacia(p):
        aux = aux*desapilar(p)
    print('El factorial de ', n, 'es', aux)

factorial(4)

# EJERCICIO 11
def vocales(p):
    cont = 0
    while not pila_vacia(p):
        aux = desapilar(p)
        aux.lower()
        if (aux == 'a') or (aux == 'e') or (aux == 'i') or (aux == 'o') or (aux == 'u'):
            cont += 1
    print("La cantidad de vocales son: ", cont)

vocales(p)

# EJERCICIO 13
def ordenados():
    p = Pila()
    p_aux = Pila()
    aux = 0
    elemento = input("Ingrese el elemento: ")
    int(elemento)
    while (elemento != -100):
        if pila_llena(p):
            print("No hay mas espacio")
        else:
            if pila_vacia(p):
                apilar(p, elemento)
            else:
                aux = desapilar(p)
                while elemento < aux and not pila_vacia(p):
                    apilar(p_aux, aux)
                    aux = desapilar(p)
                else:
                    if elemento < aux:
                        apilar(p, elemento)
                        apilar(p, aux)
                    else:
                        apilar(p, aux)
                        apilar(p, elemento)
                if not pila_vacia(p_aux):
                    while not pila_vacia(p_aux):
                        apilar(p, desapilar(p_aux))
            elemento = input("Ingrese el elemento: ")
            int(elemento)
    mostrar(p)

ordenados()

# EJERCICIO 14
def quicksort(v, pri, ult):
    p = Pila()
    apilar(p, [pri, ult])
    datos = []
    while not pila_vacia(p):
        datos = desapilar(p)
        i = datos[0]
        j = datos[1] - 1
        pivot = datos[1]
        while (i < j):
            while (v[i] <= v[pivot]) and (i < j):
                i += 1
            while (v[j] > v[pivot]) and (i < j):
                j -= 1
            if i <= j:
                v[i], v[j] = v[j], v[i]
        if v[pivot] < v[i]:
            v[pivot], v[i] = v[i], v[pivot]
        if datos[0] < j:
            apilar(p, [datos[0], j])
        if datos[1] > i:
            apilar(p, [i+1, datos[1]])

# EJERCICIO 16
def parrafo(palabra):
    pv = Pila()
    pc = Pila()
    po = Pila()
    pila_aux = Pila()
    cc = 0
    cv = 0
    co = 0
    ce = 0
    cn = 0
    palabra = palabra.lower()
    hay_z = 0
    i = 0
    while palabra[i] != '.':
        if (palabra[i] == 'a') or (palabra[i] == 'e') or (palabra[i] == 'i') or (palabra[i] == 'o') or (palabra[i] == 'u'):
            apilar(pv, palabra[i])
        else:
            aux = ord(palabra[i])
            if aux in range(97, 123):
                if aux == 122:
                    hay_z += 1
                apilar(pc, palabra[i])
            else:
                apilar(po, palabra[i])
        i += 1
    while not pila_vacia(pc):
        apilar(pila_aux, desapilar(pc))
        cc += 1
    while not pila_vacia(pila_aux):
        apilar(pc, desapilar(pila_aux))
    while not pila_vacia(pv):
        apilar(pila_aux, desapilar(pv))
        cv += 1
    while not pila_vacia(pila_aux):
        apilar(pv, desapilar(pila_aux))
    while not pila_vacia(po):
        aux = desapilar(po)
        aux = ord(aux)
        if aux == 32:
            ce += 1
        if aux in range(48, 58):
            cn += 1
        co += 1
        aux = chr(aux)
        apilar(pila_aux, aux)
    while not pila_vacia(pila_aux):
        apilar(po, desapilar(pila_aux))
    print("Cantidad de vocales: ", cv)
    print("Cantidad de consonantes: ", cc)
    print("Cantidad de caracteres especiales: ", co)
    print("Cantidad de numeros: ", cn)
    print("Cantidad de espacios: ", ce)
    porcentaje = (cv*100)/cc
    print("Porcentaje de vocales con respecto a consonantes: ", porcentaje)
    if hay_z > 0:
        print("Hay almenos una z")
    if co == cv:
        print("la cantidad de otros caracteres y las vocales son iguales")
    else:
        print("la cantidad de otros caracteres y las vocales no son iguales")


# EJERCICIO 17
def oficina():
    objetos = ["escritorio", "silla", "teclado", "mouse", "monitor", "gabinete"]
    peso = [10.5, 5, 0.800, 0.400, 2.5, 5]
    pila_oficina = Pila()
    for i in range(0, len(objetos)):
        apilar(pila_oficina, [peso[i], objetos[i]])
    pila_ordenada = ordenar_pila(pila_oficina)
    print('Pila ordenada')
    mostrar(pila_ordenada)


# EJERCICIO 19
def movimientos():
    pila_robot = Pila()
    p_aux = Pila()
    direcciones = ["norte", "sur", "este", "oeste", "noreste", "noroeste", "sureste", "suroeste"]
    num_al = random.randint(5, 50)
    for i in range(1, num_al):
        apilar(pila_robot, random.choice(direcciones))
    print("Ida")
    mostrar(pila_robot)
    while not pila_vacia(pila_robot):
        aux = desapilar(pila_robot)
        if aux == "norte":
            apilar(p_aux, "sur")
        if aux == "sur":
            apilar(p_aux, "norte")
        if aux == "este":
            apilar(p_aux, "oeste")
        if aux == "oeste":
            apilar(p_aux, "este")
        if aux == "norte":
            apilar(p_aux, "sur")
        if aux == "noreste":
            apilar(p_aux, "suroeste")
        if aux == "noroeste":
            apilar(p_aux, "sureste")
        if aux == "sureste":
            apilar(p_aux, "noroeste")
        if aux == "suroeste":
            apilar(p_aux, "noreste")
    while not pila_vacia(p_aux):
        apilar(pila_robot, desapilar(p_aux))
    print("")
    print("vuelta")
    mostrar(pila_robot)

movimientos()    

# EJERCICIO 20
def fibonacci(val):
    p = Pila()
    p_aux = Pila()
    apilar(p, 0)
    apilar(p, 1)
    for i in range(1, val):
        f1 = desapilar(p)
        f0 = desapilar(p)
        aux = f1 + f0
        apilar(p, f0)
        apilar(p, f1)
        apilar(p, aux)
    print("Fibonacci de: ", val)
    mostrar(p)

fibonacci(3)

# EJERCICIO 21
def temperatura():
    p = Pila()
    p_aux = Pila()
    sum = 0
    c_encima = 0
    c_debajo = 0
    for i in range(0, 30):
        apilar(p, random.randint(15, 27))
    max = desapilar(p)
    min = max
    apilar(p, max)
    while not pila_vacia(p):
        aux = desapilar(p)
        sum = sum + aux
        if aux < min:
            min = aux
        if aux > max:
            max = aux
        apilar(p_aux, aux)
    media = sum/30
    while not pila_vacia(p_aux):
        aux = desapilar(p_aux)
        if aux > media:
            c_encima += 1
        elif aux < media:
            c_debajo += 1
        apilar(p, aux)
    print("Valor maximo de temperatura: ", max)
    print("Valor minimo de temperatura: ", min)
    print("Promedio del total de los valores: ", media)
    print("Valores por encima de la media: ", c_encima)
    print("Valores por debajo de la media: ", c_debajo)
    print("Lista de los valores: ")
    mostrar(p)
