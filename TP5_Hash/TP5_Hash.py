from TDA_Hash import crear_tabla, agregar_ta, agregar_tc, quitar_ta, quitar_tc, buscar_tc, buscar_ta, cantidad_ta, cantidad_tc, hash_division, hash_diccionario, bernstein, barrido_ta, barrido_tc
from TDA_Hash import hash_division_guiatel, hash_division_catedra, bernstein_contactos, bernstein_star_wars
from TDA_lista import barrido_lista
from random import randint, choice


class Catedras():
    def __init__(self, codigo, nombre, modalidad, horas, docentes):
        self.codigo = codigo
        self.nombre = nombre
        self.modalidad = modalidad
        self.horas = horas
        self.docentes = docentes
    def __str__(self):
        return self.codigo + '/ ' + self.nombre + '/ ' + self.modalidad + '/ ' + self.horas + '/' + self.docentes
tabla = crear_tabla(20)

#Ej 1
class Palabra():
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado
    def __str__(self):
        return self.palabra + ', ' + self.significado
tabla = crear_tabla(28)

def diccionario(tabla):
    palabra = Palabra('Hola', 'Es un saludo')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    palabra = Palabra('Hielo', 'Agua congelada')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    palabra = Palabra('Arbol', 'Parte de la naturaleza')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    barrido_ta(tabla)

diccionario(tabla)
'''
pos = buscar_ta(tabla, 'hola', 'palabra')
if(pos is not None):
    print('Palabra', pos.info.palabra, 'significado', pos.info.significado)

print('Elemento eliminado:', quitar_ta(tabla, hash_diccionario, Palabra('Hielo', ''), 'palabra'))
barrido_ta(tabla)
'''
#Ej 2
class Guia_Tel():
    def __init__(self, numero, apellido, nombre, direccion):
        self.numero = numero
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion
    def __str__(self):
        return str(self.numero) + ', ' + self.apellido + ', ' + self.nombre + ', ' + self.direccion
def guia_telefono():
    tabla = crear_tabla(20)
    guiatel = Guia_Tel(randint(400000, 499999), 'Lionel', 'Messi', 'espala 1823')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    guiatel = Guia_Tel(randint(400000, 499999), 'Sergio', 'Aguero', 'manchestaeer 232')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    guiatel = Guia_Tel(randint(400000, 499999), 'Paulo', 'Dybala', 'italia 322')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    print('NUMERO DE TELEFONO | NOMBRE | APELLIDO | DIRECCION')
    barrido_ta(tabla)

guia_telefono()

#Ej 3
class Catedras():
    def __init__(self, codigo, nom, modalidad, horas, docente):
        self.codigo = codigo
        self.nom = nom
        self.modalidad = modalidad
        self.horas = horas
        self.docente = docente
    def __str__(self):
        return str(self.codigo) + ' | ' + self.nom + ' | ' + self.modalidad + ' | ' + str(self.horas) + ' | ' + self.docente

def catedrass():
    tabla = crear_tabla(20)
    modalidad = ['Anual', 'Cuatrimestral']
    profe = ['Pepito', 'Juan', 'Carolina', 'Esteban']
    catedra = Catedras(randint(1, 1000), 'Algorimtos y Estr. de Datos', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
    catedra = Catedras(randint(1, 1000), 'Base de Datos', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
    catedra = Catedras(randint(1, 1000), 'Prog. Orientada a Objetos', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
    catedra = Catedras(randint(1, 1000), 'Diseño UX/UI', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
    catedra = Catedras(randint(1, 1000), 'Analisis Matemático', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
    print('CODIGO | CATEDRA | MODALIDAD | CANT. HORAS | DOCENTE')
    barrido_tc(tabla)

catedrass()

# EJ 4
class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


def personajes_starwars():
    tabla = crear_tabla(25)
    personajes = ['Darth Vader', 'Luke Skywalker', 'Chewbacca', 'Yoda', 'R2D2', 'Jabba el Hutt',
                  'Obi-Wan Keobi', 'Han Solo', 'C3PO', 'Leia Organa', 'Rey', 'Poe Dameron',
                  'Finn', 'Lando Calrissian', 'Jabba el Hutt', 'Boba Fett', 'Jawa', 'Darth Maul',
                  'Anakin Skywalker', 'Bobba Fett', 'Jar Jar Binks', 'Darth Sidious', 'Kylo Ren',
                  'Obi-Wan Kenobi', 'Greddo', 'Wilhuff Tarkin', 'Owen Lars', 'Breha Organa']
    pos = 0
    for i in range(0, len(personajes)):
        nom = personajes[pos]
        dato_sw = Personaje(nom)
        agregar_tc(tabla, bernstein_star_wars, dato_sw)
        pos += 1
    print('Tabla de personajes de Star Wars con', len(tabla), 'posiciones')
    barrido_tc(tabla)

    # porcentaje de personajes cargados
    porc_tabla = (cantidad_tc(tabla)*100)/len(tabla)
    print('Porcentaje usado de la tabla', porc_tabla)
    print()

    if porc_tabla > 75:
        print('El factor de carga de la tabla supero el 75%. Haciendo rehashing...')
        nueva_tabla = crear_tabla(len(tabla)*2)
        for dato in tabla:
            if dato is not None:
                agregar_tc(nueva_tabla, bernstein_star_wars, dato)
        print('Nueva tabla con', len(nueva_tabla), 'posiciones')
        barrido_tc(nueva_tabla)
        porc_nueva_tabla = (cantidad_tc(nueva_tabla)*100)/len(nueva_tabla)
        print('Porcentaje usado de la nueva tabla', porc_nueva_tabla)
    else:
        print('El porcentaje de la tabla es menor a 75%')

personajes_starwars()

# EJ 5
class Contacto():
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        return self.nombre + ' | ' + self.apellido + ' | ' + self.correo


def contactos_personas():
    tabla = crear_tabla(20)
    datos = Contacto('Gordon', 'Freeman', 'elgordofr@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    datos = Contacto('Barney', 'Calhoun', 'barney1972@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    datos = Contacto('Alyx', 'Vance', 'alyxuwu@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    datos = Contacto('Eli', 'Vance', 'eli_vance@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    datos = Contacto('Isaac', 'Kleiner', 'drisaackleiner@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    print('NOMBRE | APELLIDO | CORREO ELECTRÓNICO')
    barrido_tc(tabla)
