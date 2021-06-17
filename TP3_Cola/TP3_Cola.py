from TDA_ColaDin import Cola, arribo, atencion, cola_vacia, barrido_cola
from TDA_ColaDin import colaint, colastring, colaneg, colacaracteres, primos
from TDA_ColaDin import tamanio_cola, en_frente, mover_final
from TDA_PilaDin import Pila, apilar, desapilar, pila_vacia, pilaint
from TDA_PilaDin import barrido_pila, ordenar_pila
from math import asin, sqrt, sin, cos, radians
from time import sleep
from random import randint, choice

#ColaC = Cola()
#colacaracteres(ColaC, 7)
#print('Cola de caracteres')
#barrido_cola(ColaC)
#print('')

#ColaN = Cola()
#colaneg(ColaN, 5)
#print('Cola de numeros enteros positivos y negativos')
#barrido_cola(ColaN)
#print('')

#ColaE = Cola()
#colaint(ColaE, 5)
#print('Cola de numeros enteros')
#barrido_cola(ColaE)
#print('')

ColaS = Cola()
colastring(ColaS, 4)
print('Cola de letras')
barrido_cola(ColaS)
print('')

#PilaN = Pila()
#pilaint(PilaN, 5)
#print('Pila de numeros enteros')
#barrido_pila(PilaN)
#print('')

#1
def vocales(C):
    Caux = Cola()
    Csl= Cola()
    while not cola_vacia(C):
        aux = atencion(C)
        if (aux == 'a') or (aux == 'e') or (aux == 'i') or (aux == 'o') or (aux == 'u') or (aux == 'A') or (aux == 'E') or (aux == 'I') or (aux == 'O') or (aux == 'U'):
            arribo(Caux, aux)
        else:
            arribo(Csl,aux)
    print('La Cola sin vocales es')
    barrido_cola(Csl)

#vocales(ColaS)

#2
def invertir(C):
    P = Pila()
    while not cola_vacia(C):
        apilar(P, atencion(C))
    while not pila_vacia(P):
        arribo(C, desapilar(P))
    print ('pila invertida')
    barrido_cola(C)

#invertir(ColaS)
    
#3
def palindromo(C):
    P = Pila()
    Caux = Cola()
    while not cola_vacia(C):
        apilar(P, atencion(C))
    while not pila_vacia(P):
        arribo(Caux, desapilar(P))
    barrido_cola(Caux)
    if (Caux == C):
        print ('son palindromo')
    else:
        print('NO es palindromo')

#palindromo(ColaS)

#4
def primoss(C):
    Caux = Cola()
    while not cola_vacia(C):
        x = atencion(C)
        if primos(x):
            arribo(Caux, x)
    C = Caux 
    barrido_cola(C)

#primoss(ColaE)  
  
#5
def invertir_pilaa(P):
    C = Cola()
    while not pila_vacia(P):
        arribo(C, desapilar(P))
    while not cola_vacia(C):
        apilar(P, atencion(C))
    barrido_pila(P)

#invertir_pilaa(PilaN)

#6
def ocurrencias(C):
    #print('ingrese la ocurrencia que desear comparar')
    aux = 2 #queria poner un input pero cuando lo ponia , el programa no me funcionaba
    cont = 0
    while not cola_vacia(C):
        xx = atencion(C)
        if (xx == aux):
            cont += 1
    if (cont > 0):
        print('La cantidad de ocurrencias de esta cola es : ', cont)
    else:
        print('NO hay ocurrencias en esta cola')

#ocurrencias(ColaE)
'''
#8
def ordenada(C):
    Caux = Cola()
        for i in range (tamanio_cola(C)):

ordenada()        
'''
#10
def StarWars():
    C = Cola()
    Caux = Cola()
    Caux2 = Cola()
    personaje = ['Breha Organa', 'Bail Organa', 'Killik',
                 'Chirpa el Ewok', 'Asha Fahn el Ewok', 'Kneesaa el Ewok',
                 'Saqueador Tusken', 'Dathcha el Jawa', 'Jabba el Hutt',
                 'Luke Skywalker', 'Han Solo', 'Yoda',
                 'Jar Jar Binks', 'Darth Maul']
    origen = ['Alderaan', 'Alderaan', 'Alderaan', 'Endor', 'Endor', 'Endor',
              'Tatooine', 'Tatooine', 'Tatooine', 'Polis Massa', 'Corellia',
              'Desconocido', 'Naboo', 'Dathomir']
    for i in range(0, len(personaje)):
        arribo(C, [personaje[i], origen[i]])
    print('Personaje  |   Planeta de origen')
    barrido_cola(C)
    while not cola_vacia(C):
        aux = atencion(C)
        if (aux[1] == 'Alderaan') or (aux[1 == 'Endor']) or (aux[1] == 'Tatooine'):
            print('El personaje ', aux[0], ' pertenece al planeta ', aux[1])
        if (aux[0] == 'Luke Skywalker'):
            print('El planeta natal de Luke Skywalker es ', aux[1])
        if (aux[0] == 'Han Solo'):
            print('El planeta natal de Han Solo es ', aux[1])
        if (aux[0] != 'Yoda'):
           arribo(Caux, aux)
        else:
            arribo(Caux, ['Personaje', 'Nuevo'])
            arribo(Caux, aux) 
        if (aux[0] != 'Jar Jar Binks'):
            arribo(Caux2, aux)
        else:
            arribo(Caux2, aux)
            arribo(Caux2, ['Personaje2', 'Nuevo2'])
    print('La Cola con el personaje nuevo antes de Yoda es:')
    barrido_cola(Caux)
    print('La Cola con el personaje nuevo despues de Jar Jar Binks es:')
    barrido_cola(Caux2)

#StarWars()

#Ej 11
def numeros_ordenados():
    C = Cola()
    Caux = Cola()
    numeros1 = [0, 5, 9, 11]
    numeros2 = [2, 6, 10, 14]
    for i in range(0, len(numeros1)):
        arribo(C, numeros1[i])
        arribo(Caux, numeros2[i])
    for i in range(0, tamanio_cola(C)):
        if (en_frente(C) < en_frente(Caux)):
            mover_final(C)
        else:
            while (en_frente(C) > en_frente(Caux)):
                arribo(C, atencion(Caux))
            mover_final(C)
    while not cola_vacia(Caux):
        arribo(C, atencion(Caux))
    print('Termino')
    barrido_cola(C)

#numeros_ordenados()

#Ej 12
def caracter(C):
    Caux = Cola()
    Caux2 = Cola()
    auxD = False
    auxL = False
    cont_L = 0
    existe1 = False
    existe2 = False
    while not cola_vacia(C):
        aux = atencion(C)
        auxD = aux.isdigit()
        if (auxD == True):
            arribo(Caux, aux)
        else:
            arribo(Caux2, aux)
        if (aux == '#'):
            existe1 = True
        if (aux == '?'):
            existe2 = True
    print('La cola con solo digitos es:')
    barrido_cola(Caux)
    print('La cola con el resto de caracteres es :')
    barrido_cola(Caux2)
    while not cola_vacia(Caux2):
        aux2 = atencion(Caux2)
        auxL = aux2.isalpha()
        if (auxL == True):
            cont_L += 1
    print('La cantidad de letras de la segunda Cola es: ', cont_L)
    if (existe1 == True):
        print('Existe el caracter #')
    if (existe2 == True):
        print('Existe el caracter ?')

#caracter(ColaC)

#Ej 16
def procesador():
    C = Cola()
    ID = [4242, 1244, 6446, 8655]
    tiempo = [8, 12, 2, 15]
    for i in range(len(ID)):
        arribo(C, [ID[i], tiempo[i]])
    print('ID | Tiempo')
    barrido_cola(C)
    while not cola_vacia(C):
        aux = atencion(C)
        if (aux[1] < 4.5):
            sleep(aux[1])
            print(aux, ' ejecutado con exito')
        else:
            print('El dato ', aux ,' excedio el tiempo de procesamiento de 4,5 segundos')
            print('El dato ha sido devuelto a la cola con el tiempo restante de ejecucion')
            aux[1] = aux[1] - 4.5
            arribo(C, aux)

#procesador()

#Ej 19
def peaje():
    Cola1 = Cola()
    Cola2 = Cola()
    Cola3 = Cola()
    automoviles = ['automovil', 'camioneta', 'camion', 'colectivo']
    for i in range (5):
        arribo(Cola1, choice(automoviles))
        arribo(Cola2, choice(automoviles))
        arribo(Cola3, choice(automoviles))
    auto = 0
    camionet = 0
    cami = 0
    cole = 0
    cabina1 = 0
    while not cola_vacia(Cola1):
        aux = atencion(Cola1)
        if (aux == 'automovil'):
            cabina1 += 47
            auto += 1
        if (aux == 'camioneta'):
            cabina1 += 59
            camionet += 1
        if (aux == 'camion'):
            cabina1 += 71
            cami += 1
        if (aux == 'colectivo'):
            cabina1 += 64
            cole += 1
    print('Esta cola recaudo $', cabina1)
    print('En la cabina 1 se contaron los siguientes vehiculos:')
    print('automoviles: ', auto)
    print('camionetas: ', camionet)
    print('camiones: ', cami)
    print('colectivos: ', cole)
    auto2 = 0
    camionet2 = 0
    cami2 = 0
    cole2 = 0
    cabina2 = 0
    while not cola_vacia(Cola2):
        aux = atencion(Cola2)
        if (aux == 'automovil'):
            cabina2 += 47
            auto2 += 1
        if (aux == 'camioneta'):
            cabina2 += 59
            camionet2 += 1
        if (aux == 'camion'):
            cabina2 += 71
            cami2 += 1
        if (aux == 'colectivo'):
            cabina2 += 64
            cole2 += 1
    print('Esta cola recaudo $', cabina2)
    print('En la cabina 2 se contaron los siguientes vehiculos:')
    print('automoviles: ', auto2)
    print('camionetas: ', camionet2)
    print('camiones: ', cami2)
    print('colectivos: ', cole2)
    auto3 = 0
    camionet3 = 0
    cami3 = 0
    cole3 = 0
    cabina3 = 0
    while not cola_vacia(Cola3):
        aux = atencion(Cola3)
        if (aux == 'automovil'):
            cabina3 += 47
            auto3 += 1
        if (aux == 'camioneta'):
            cabina3 += 59
            camionet3 += 1
        if (aux == 'camion'):
            cabina3 += 71
            cami3 += 1
        if (aux == 'colectivo'):
            cabina3 += 64
            cole3 += 1
    print('Esta cola recaudo $', cabina3)
    print('En la cabina 3 se contaron los siguientes vehiculos:')
    print('automoviles: ', auto3)
    print('camionetas: ', camionet3)
    print('camiones: ', cami3)
    print('colectivos: ', cole3)   
    max = 0
    if (cabina1 > max):
        max = cabina1
        num = 1
    if (cabina2 > max):
        max = cabina2
        num = 2
    if (cabina3 > max):
        max = cabina3
        num =3
    print('La cabina ', num, ' fue la que mas recaudo con un monto de $', max)

#peaje()

#Ej 20
def aeropuerto():
    C = Cola()
    nom_empresa = ['Singapore Airlines', 'Qatar Airways', 'Emirates', 'Delta']
    hora_salida = [21.00, 10.00, 17.15, 7.30]
    hora_llegada = [4.00, 19.30, 1.00, 00.45]
    aerop_origen = ['Aeropuerto de Changi', 'Aeropuerto Internacional de Incheon', 'Aeropuerto Internacional de Haneda', 'Aeropuerto Internacional de Hong Kong']
    aerop_destino = ['Aeropuerto Internacional Hamad', 'Aeropuerto de Munich', 'Aeropuerto Internacional Chubu Centrair', 'Aeropuerto de Heathrow']
    tipo = ['Negocio', 'Pasajero', 'Negocio', 'Carga']
    print('     Empresa      | Hora salida | Hora llegada |  Aeropuerto de Origen    |    Aeropuerto de Destino    | Tipo de vuelo')
    for i in range(0, len(nom_empresa)):
        arribo(C, [nom_empresa[i], hora_salida[i], hora_llegada[i], aerop_origen[i], aerop_destino[i], tipo[i]])
    barrido_cola(C)


#aeropuerto()

# EJ 21
def marvel():
    '''Cola con personajes de Marvel Cinematic Universe'''
    C = Cola()
    personaje = ['Carol Danvers', 'Natasha Romanoff', 'Gamora Zen Whoberi',
                 'Tony Stark', 'Scott Lang', 'Steve Rogers', 'Stephen Strange',
                 'Peter Benjamin Parker']
    superheroe = ['Capitana Marvel', 'Black Widow', 'Gamora', 'Iron Man',
                  'Ant-Man', 'Capitan America', 'Doctor Strange', 'Spider Man']
    genero = ['F', 'F', 'F', 'M', 'M', 'M', 'M', 'M']
    for i in range(len(personaje)):
        arribo(C, [personaje[i], superheroe[i], genero[i]])
    print('Nombre del personaje | Nombre del superheroe | Genero')
    barrido_cola(C)
    print('')
    while not cola_vacia(C):
        dato = atencion(C)
        if dato[1] == 'Capitana Marvel':
            print('El personaje de la Capitana Marvel es: ' + dato[0])
        if dato[2] == 'F':
            print(dato[1] + ', personaje femenino')
        if dato[2] == 'M':
            print(dato[1] + ', personaje masculino')
        if dato[0] == 'Scott Lang':
            print('El nombre del superheroe de Scott Lang es: ' + dato[1])
        cad = dato[0]
        if cad[0] == 'S' or cad[0] == 'S':
            print('El personaje ' + dato[0] + ' empieza con S')
            print('El superheroe ' + dato[1] + ' empieza con S')
        if dato[0] == 'Carol Danvers':
            print('El superheroe de Carol Danvers es: ' + dato[1])

#marvel()
