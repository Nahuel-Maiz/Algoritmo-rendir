from TDA_lista import lista_vacia, insertar, insertar_vec, eliminar, eliminar_vec, criterio, lista_vacia, busqueda_lista, busqueda_lista_vec, tamanio_lista, barrido_sublista, barrido_lista, listaint, listaneg, listastring, listacaracteres, Lista
from random import randint, choice
#lista = Lista()

#Ej 1
def contar(lista):
    aux = lista.inicio
    cont = 0
    while (aux is not None):
        cont += 1
        aux = aux.sig
    print ('Esta lista contiene ', cont, ' nodos')

#contar(lista)

#Ej 2
def vocales(lista):
    aux = lista.inicio
    while (aux is not None):
        if (aux.info == 'a') or (aux.info == 'A') or (aux.info == 'e') or (aux.info == 'E') or (aux.info == 'i') or (aux.info == 'I') or (aux.info == 'o') or (aux.info == 'O') or (aux.info == 'u') or (aux.info == 'U'):
            eliminar(lista, aux.info)
        aux = aux.sig
    print('La lista sin vocales seria :')
    barrido_lista(lista)

#vocales(lista)

#Ej 3
def par_impar(lista):
    lista_par = Lista()
    lista_impar = Lista()
    aux = lista.inicio
    while (aux is not None):
        if (aux.info % 2 == 0):
            insertar(lista_par, aux.info)
        else:
            insertar(lista_impar, aux.info)
        aux= aux.sig
    print('La lista de elementos pares es:')
    barrido_lista(lista_par)
    print('La lista de elementos impares es:')
    barrido_lista(lista_impar)

#par_impar(lista)

#Ej 5
def primos(lista):
    aux = lista.inicio
    while (aux is not None):
        cont = 0
        for i in range (1, aux.info):
            if (aux.info % i == 0):
                cont += 1
        if (cont < 2):
            eliminar(lista, aux.info)
        aux = aux.sig
    print('La pila sin los primos es:')
    barrido_lista(lista)

#primos(lista)

#LO QUE ESTA ACA PARA ABAJO PERTENECE AL EJERCICIO 6
SuperHeroes= Lista()
nombres_superHeroes = ['Linterna Verde', 'Wolverine', 'Dr. Strange', 'Capitana Marvel', 'Mujer Maravilla', 'Flash', 'Star-Lord', 'Joker']
casa = ['DC', 'Marvel', 'DC', 'Marvel', 'DC', 'DC', 'Marvel', 'DC']
anio_aparicion = [1940, 1974, 1963, 1968, 1941, 1940, 1976, 1940]
bio = ['traje : color verde, arma : anillo de poder', 'poderosa capacidad de regeneracion, tres garras retractiles en cada mano', 'hechicero supremo', 'guerrera extraterrestre de la civilizacion Kree', 'princesa guerrera de las Amazonas', 'capacidad de correr, moverse y pensar extremadamente rapido', 'policia interplanetario', 'criminal mas notable de Gotham City']
for i in range (len(nombres_superHeroes)):
    dato = [nombres_superHeroes[i], casa[i], anio_aparicion[i], bio[i]]
    insertar(SuperHeroes, dato)
barrido_lista(SuperHeroes)

#Ej 6
def Super_Heroes(SuperHeroes):
    aux = SuperHeroes.inicio
    c_dc = 0
    c_M = 0
    while (aux is not None):
        dato = aux.info
        if (dato[0] == 'Linterna Verde'):
            eliminar(SuperHeroes, aux.info)
            print('La nueva lista sin Linterna Verde es :')
            barrido_lista(SuperHeroes)
        if (dato[0] == 'Wolverine'):
            print('El anio de aparacion de Wolverine es :', dato[2])
        if (dato[0] == 'Dr. Strange'):
            dato[1] == 'Marvel'  
        if (dato[3].find("traje") >= 0) or (dato[3].find("armadura") >= 0):
            print('Los nombres de los Super Heroes con armadura o traje son:')
            print(dato[0]) 
        if (dato[2] < 1963):
            print(dato[0], ' aparecio antes de 1963 y su casa es: ', dato[1])
        if (dato[0] == 'Capitana Marvel') or (dato[0] == 'Mujer Maravilla'):
            print('La casa de ', dato[0], ' es ', dato[1])
        if (dato[0] == 'Flash') or (dato[0] == 'Star-Lord'):
            print('Informacion')
            print(aux.info)
        cadena = dato[0]
        if (cadena[0] == 'B') or (cadena[0] == 'M') or (cadena[0] == 'S'):
            print(dato)
        if (dato[1] == 'DC'):
            c_dc +=1
        else:
            c_M += 1
        aux = aux.sig
    print ('De la casa DC hay ', c_dc, ' Superheroes')
    print ('De la casa DC hay ', c_M, ' Superheroes')

Super_Heroes(SuperHeroes) #ARREGLAR

#Ej 10
#ESTO PERTENECE AL EJERCICIO 10

lista_canciones = Lista()
cancion = ['Crying Lightning', 'Parque Acuatico', 'Esperando el impacto', 'Where Is The Love?', 'La Rueda Magica', 'Clavado En Un Bar', 'Fluorescent Adolescent']
artista = ['Artics Monkeys', 'El Kuelgue', 'Bersuit Vergarabat', 'The Black Eyed Peas', 'Fito Paez', 'Mana', 'Artics Monkeys']
duracion = [3.43, 2.53, 3.34, 4.12, 3.54, 6.11, 3.15]
reproducciones = [19883309, 4147845, 7633770, 463109437, 762594, 142933249, 121735091]

for l in range(0, len(cancion)):
    dato = [cancion[l], artista[l], duracion[l], reproducciones[l]]
    insertar(lista_canciones, dato)
#barrido_lista(lista_canciones)
#Ej 10
def Spotify (lista_canciones):
    aux = lista_canciones.inicio
    larga = 0
    lista_artic = Lista()
    lista_solo_palabra = Lista()
    solo_palabra = False
    artic = False
    while (aux is not None):
        dato = aux.info
        if(dato[2] > larga):
            larga = dato[2]
            info = dato
        if (dato[1] == 'Artics Monkeys'):
            artic = True
            insertar(lista_artic, dato[0])
        if (' ' in dato[1]):
            print()
        else:
            solo_palabra = True
            insertar(lista_solo_palabra, dato[1])
        aux = aux.sig
    print('La informacion de la cancion mas larga es: ')
    print(info)
    if (artic == True):
        print('Las canciones de Artics Monkeys son:')
        barrido_lista(lista_artic)
    if (solo_palabra == True):
        print('Los nombres de las bandas con nombre de una sola palabra son:')
        barrido_lista(lista_solo_palabra)

Spotify(lista_canciones)

#Ej 9
lista_curso = Lista()
nombre = ['Milagros', 'Nahuel', 'Fernanda']
apellido = ['Gimenez', 'Maiz', 'Miniom']
legajo = [2323, 4344, 6767]
materia = ['Calculo', 'Programacion', 'Algebra']
nota = [8, 10, 4]
fecha = ['30/07/00', '18/08/99', '05/10/00']

for l in range(0, len(nombre)):
    dato = [nombre[l], apellido[l], legajo[l]]
    insertar(lista_curso, dato)
barrido_lista(lista_curso)

#11
saga_starwars = Lista()
nombre = ['Luke Skywalker', 'Han Solo', 'Yoda', 'Leia Organa', 'Jar Jar Binks', 'Darth Vader', 'C3PO', 'Chewbacca']
altura = [1.75, 1.85, 0.66, 1.55, 1.96, 2.03, 1.75, 2.30]
edad = [20, 18, 900, 14, 30, 37, 54, 140]
genero = ['Masculino', 'Masculino',  'Masculino', 'Femenino', 'Masculino', 'Masculino', 'Masculino', 'Masculino']
especie = ['Humano', 'Humano', 'List of Star Wars species', 'Humano', '	Gungan', 'Humano', 'Droide', 'Wookiee']
planeta_natal = ['Polis Massa', 'Corellia', 'Desconocido', 'Alderaan', 'Naboo', 'Polis Massa', 'Tatooine', 'Kashyyyk']
episodios = ['3 4 5 6 7 8 9', '1 2 3 4 5 6 7 8', '1 2 3 4 5 6 7 8 9', '4 5 6 7 8 9', '1 2 3', '3 4 5 6', '1 2 3 4 5 6 7 8 9', '1 2 3 4 5 6 7 8 9']

for l in range(0, len(nombre)):
    dato = [nombre[l], altura[l], edad[l], genero[l], especie[l], planeta_natal[l], episodios[l]]
    insertar(saga_starwars, dato)
#barrido_lista(saga_starwars)

def StarWars_2():
    aux = saga_starwars.inicio
    lista_femenina = Lista()
    lista_droide = Lista()
    lista_850 = Lista()
    lista_humano = Lista()
    lista_70 = Lista()
    lista_epiosodio_7 = Lista()
    chewbacca = ' '
    chewbacca2 = Lista()
    while (aux is not None):
        dato = aux.info
        if (dato[3] == 'Femenino'):
            insertar(lista_femenina, dato)
        if (dato[4] == 'Droide'):
            insertar(lista_droide, dato)
        if (dato[0] == 'Darth Vader'):
            print('Informacion de Darth Vader:')
            print(dato)
        if (dato[0] == 'Han Solo'):
            print('Informacion de Han Solo:')
            print(dato) 
        if (dato[2] > 850):
            insertar(lista_850, dato)
        if (dato[4] == 'Humano') and (dato[5] == 'Alderaan'):
            insertar(lista_humano, dato)
        if (dato[1] < 0.70):
            insertar(lista_70, dato)
        if ('4' in dato[6]) and ('5' in dato[6]) and ('6' in dato[6]) and ('7' in dato[6]):
            insertar(lista_epiosodio_7, dato)
        if ('4' in dato[6]) and ('5' in dato[6]) and ('6' in dato[6]):
            eliminar(saga_starwars, dato)
        if (dato[0] == 'Chewbacca'):
            chewbacca = dato[6]
            insertar(chewbacca2, dato)
        aux = aux.sig
    print('Lista de personajes de genero Femenino:')
    barrido_lista(lista_femenina)
    print('Lista de personajes de especie droide :')
    barrido_lista(lista_droide)
    print('Personajes con edad mayor a 850 años:')
    barrido_lista(lista_850)
    print('Los personajes de especie humana de origen Alderaan son:')
    barrido_lista(lista_humano)
    print('La informacion de los personajes menor a 70 centimetros es:')
    barrido_lista(lista_70)
    print('Los personajes que aparecieron en el episodio 7 y los 3 anteriores son:')
    barrido_lista(lista_epiosodio_7)
    print('La lista sin los personajes que aparecen en los episodios 4, 5 y 6 es:')
    barrido_lista(saga_starwars)
    print('Los episodios en los que sale Chewbacca son:')
    print(chewbacca)
    print('La informacion de Chewbacca es:')
    barrido_lista(chewbacca2)
StarWars_2()

#Ej 12
elimino_anteultimo = Lista()
lista_eliminar = [2, 34, 465, 21, 56]

for l in range(0, len(lista_eliminar)):
    dato = [lista_eliminar[l]]
    insertar(elimino_anteultimo, dato)
barrido_lista(elimino_anteultimo)

def elimino():
    aux = elimino_anteultimo.inicio
    atr = tamanio_lista(elimino_anteultimo)
    atr2 = atr-2
    for i in range (atr):
        dato = aux.info
        if ( i == atr2):
            eliminar(elimino_anteultimo, dato)
        aux = aux.sig
    print('La lista sin su alteuntimo nodo es:')
    barrido_lista(elimino_anteultimo)

elimino()

#Ej 14
lista_dados = Lista()
nombres = ['Juan', 'Moe', 'Pepito']
numeros = [randint (0, 100), randint (0, 100), randint (0, 100)]

for l in range(0, len(nombres)):
    dato = [nombres[l], numeros[l]]
    insertar(lista_dados, dato)
barrido_lista(lista_dados)

def juego_dados():
    aux = lista_dados.inicio
    dado5 = False
    while (dado5 != True): 
            dato = aux.info
            dados = 0
            print('Turno de :', dato[0])
            dados = randint(1, 6)
            print('A ', dato[0], ' le ha tocado un: ', dados)
            if (dados == 5):
                dado5 = True
                print('El juego termino y los datos del ganador es:')
                print(dato)
            else:
                print('Avanzamos al siguiente jugador')
            if (aux.sig == None):
                aux = lista_dados.inicio
            else:
                aux = aux.sig

juego_dados()
'''     
#Ej 15
lista_entrenadores = Lista()
nombres = ['Juan', 'Mario', 'Xavier']
cant_torneos = [12, 5, 11]
batalla_perdidas = [4, 2, 7]
batalla_ganadas = [5, 3, 1]

for l in range(0, len(nombres)):
    dato = [nombres[l], cant_torneos[l], batalla_perdidas[l], batalla_ganadas[l]]
    insertar(lista_entrenadores, dato)
barrido_lista(lista_entrenadores)

pokemons = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Spearow', 'Dugtrio', 'Primeape', 'Terrakion', 'Tyrantrum', 'Wingull']
tipo = ['Fuego', 'Agua', 'Electrico', 'Normal', 'Veneno']
subtipo = ['Tierra', 'Fuego', 'Planta', 'Agua', 'Aire', 'Volador']

for i in range(2):
        poke = Pokemon(choice(pokemons), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista_entrenadores, 'Juan')
        insertar(pos.sublista, poke)

    print('NOMBRE | TORNEOS GAN. | VICTORIAS | DERROTAS')
    barrido_lista(lista_entrenadores)
    print()
    aux = lista_entrenadores.inicio
    # barrido sublista
    while aux is not None:
        print('Entrenador:', aux.info.entrenador)
        print('NOMBRE | NIVEL | TIPO | SUBTIPO')
        barrido_sublista(aux.sublista)
        print()
        aux = aux.sig
        
'''
#Ej 16
lista_software = Lista()
costo = [randint(0, 50000)]
tiempo_ejecucion = [randint(0, 30)]
fecha_inicio = ['10/05/05']
fin_estimada = ['12/01/06']
fin_efectiva = ['13/12/09']
persona_cargo = ['Messi']

for l in range(0, len(costo)):
    dato = [costo[l], tiempo_ejecucion[l], fecha_inicio[l], fin_estimada[l], fin_efectiva[l], persona_cargo[l]]
    insertar(lista_software, dato)
barrido_lista(lista_software)

def Software():
    aux = lista_software.inicio
    while (aux is not None):
        dato = aux.info
        if (dato[4] == dato[3]):
            print('Informacion de la tarea')
            print(dato[0])
        aux = aux.sig
    print('El tiempo promedio de las tareas es')
    print('Tiempo: ', dato[1])
    print('El costo total del proyecto es:')
    print('$', dato[0])
    print('La persona llamda ', dato[5], ' realiza la actividad (NO DICE NADA EN EL EJERCICIO)')

Software()

#Ej 17
lista_aeropuerto = Lista()
empresa = ['Qatar Airways', 'Singapore Airlines', 'Fly Emirates', 'Iberia', 'Turkish Airlines']
num_vuelo = [randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999)]
cant_asientos = [randint(100, 200), randint(100, 200), randint(100, 200), randint(100, 200), randint(100, 200)]
fecha_salida = ['10/12/09', '14/11/19', '03/08/20', '16/06/04', '14/11/19']
destino = ['Atenas', 'Miconos', 'Rodas', 'Tailandia', 'Nicosia', 'Ulan Bator', 'Yakarta', 'El Brillante']
km = [randint(100, 1000), randint(100, 1000), randint(100, 1000), randint(100, 1000), randint(100, 1000)]
clase_turista_ocupado = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
clase_primera_ocupado = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]

for l in range(0, len(empresa)):
    dato = [empresa[l], num_vuelo[l], cant_asientos[l], fecha_salida[l], destino[l], km[l], clase_turista_ocupado[l], clase_primera_ocupado[l]]
    insertar(lista_aeropuerto, dato)
barrido_lista(lista_aeropuerto)

def aeropuerto():
    aux = lista_aeropuerto.inicio
    lista_a = Lista()
    lista_vuelos_programados = Lista()
    fecha = input('Ingrese fecha a comparar')
    while (aux is not None):
        total_recaudado = 0
        clase_turis_dispo = 0
        dato = aux.info
        if (dato[4] == 'Atenas') or (dato[4] == 'Miconos') or (dato[4] == 'Rodas'):
            insertar(lista_a, dato)
        clase_turis_dispo = dato[2] - dato[6] 
        if (clase_turis_dispo > 0):
            print('En el vuelo numero ', dato[1], ' hay ', clase_turis_dispo, ' asientos disponibles')
        if ( dato[6] > 0):
            total_recaudado += (dato[5] * 75 * dato[6]) 
        if ( dato[7] > 0):
            total_recaudado += (dato[5] * 203 * dato[7])
        print('El total recaudado del vuelo numero ', dato[1], ' es $', total_recaudado)
        if (dato[3] == fecha):
            insertar(lista_vuelos_programados, dato)
        if (dato[4] == 'Tailandia'):
            print('Empresa del vuelo a Tailandia: ', dato[0])
            print('Kilometros del vuelo a Tailandia: ', dato[5])
        aux= aux.sig
    print('Los vuelos con destino a Atenas, Miconos y Rodas son:')
    barrido_lista(lista_a)
    print('Los vuelos programados para una determinada fecha son')
    barrido_lista(lista_vuelos_programados)
aeropuerto()

#Ej 21
lista_pelicula = Lista()
nombre = ['La Gran Estafa', 'Tarzan', 'Batman']
valoracion = [randint(0, 10), randint(0, 10), randint(0, 10)]
anio_estreno = [randint(1970, 2020), randint(1970, 2020), randint(1970, 2020)]
recaudacion = [randint(0, 1000000), randint(0, 1000000), randint(0, 1000000)]

for l in range(0, len(nombre)):
    dato = [nombre[l], valoracion[l], anio_estreno[l], recaudacion[l]]
    insertar(lista_pelicula, dato)
barrido_lista(lista_pelicula)

def peliculas():
    aux = lista_pelicula.inicio
    lista_anio = Lista() 
    peli_max = ''
    max = 0
    valoracion_publico = 0
    lista_valoracion = Lista()
    anio = input('Ingrese el año para comparar')
    while (aux is not None):
        dato = aux.info
        if (dato[2] == anio):
            insertar(lista_anio, dato)
        if (dato[3] > max):
            max = dato[3]
            peli_max = dato[0]
        if (dato[1] > valoracion_publico):
            valoracion_publico = dato[1]
            lista_valoracion = Lista()
            insertar(lista_valoracion, dato)
        else:
            if (valoracion_publico == dato[1]):
                insertar(lista_valoracion, dato)
        aux = aux.sig
    print('La peliculas de un determinado año son:')
    barrido_lista(lista_anio)
    print('La pelicula que mas recaudo fue ', peli_max, ' y recaudo un monto de $', max )
    print('Las o la pelocula de mayor valoracion es/son:')
    barrido_lista(lista_valoracion)
peliculas()
