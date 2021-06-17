#Ejercicio 1
def  fibonacci ( numero ):
    if ( numero == 0  or  numero == 1 ):
        return  numero
    else :
        return  fibonacci ( numero - 1 ) +  fibonacci ( numero - 2 )
        
#print(fibonacci(3))

#Ejercicio 2
def  suma ( numero1 ):
    if ( numero1 == 0 ):
        return  numero1    
    else :
        return  numero1 + suma ( numero1 - 1 ) 

#print(suma(4))

#Ejercicio 3
def producto (num1, num2):
    if (num2==1):
        return num1
    else:
        return num1 + producto (num1, num2-1) 

print(producto(3,3))

#Ejercicio 4
def potencia(base, expo):
    if (expo==1):
        return base
    else:
        return base * potencia(base, expo-1)

#Ejercicio 5
def secuencia(palabra):
    if (len(secuencia) == 1):
        return secuencia
    else:        
        return palabra[-1] + secuencia(palabra[:-1])

#Ejercicio 6
def serie(n):
    if (n == 1):
        return serie
    else:
        return n + serie(n-1) 

#Ejercicio 7
def binario(num):
    if (num <= 1):
        return  str ( num )
    else:
        return  binario ( num // 2 ) +  str ( num  %  2 )

#Ejercicio 8
def logaritmo(base, numero):
    if ( base  ==  numero ):
        return  1
    else :
        return  1  +  logaritmo ( base , numero / base )  

#Ejercicio 9
def digitos(num):
    if (num == 0):
        return 0
    else:
        return 1 + digitos(num//10) 
'''
#Ejercicio 10
def invertir_numero(n, posicion=-1):
    posicion += 1
    tamanio = cuenta_digitos(n)

    if (tamanio == 1):
        return n * potencia(10, posicion)

    actual = n // potencia(10, tamanio-1)
    restante = n - actual * potencia(10, tamanio-1) 
    return actual * potencia(10, posicion) + invertir_numero(restante, posicion)
'''
#Ejercicio 11
def  mcd ( n1 , n2 ):
    if  (n2 == 0):
        return  n1
    else :
        return  mcd ( n2, n1  %  n2 )

#Ejercicio 12
def  mcm ( n , m ):
    if ( n  %  m  ==  0 ):
        return  n
    else :
        return  mcm ( n , m  *  n )  

#Ejercicio 13
def  suma_digitos ( n ):
    if  (n < 10) :
        return  n
    else:
        return ( n % 10 ) +  suma_digitos ( n // 10 )   

# Ejercicio 14
def  raíz ( n , x ):
    if (x*x == n):
        return x
    elif (x*x > n):
        return x-1
    else:
        return raíz(n,x+1)

#Ejercicio 15
def sucesion(num):
    if(num == 1):
        return 2
    else:
        return -3 * sucesion(num-1)

#Ejercicio 16
def barrido(vec):
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])
        barrido(vec[0:-1])

#Ejercicio 17
def barrido_matriz(m, i, j):
    if (i<len(m) and j<len(m[i])):
        print(m[i][j])
        if(j==len(m[i][j])):
            j+=1
            j=-1
        barrido_matriz(m,i,j+1)

#Ejercicio 18
def suc(n):
    if (n==1):
        return 2
    else:
        return n+1/suc(n-1)

#Ejercicio 19
i=0
def busq_secuencial(buscado, v):
    global i
    if buscado==v[i]:
        return "El elemento se encuentra en la posicion ",i," de la lista"
    else:
        i+=1
        return busq_secuencial(buscado,v)

#Ejercicio 20
def bbin(buscado,v,pri,ult):
    if pri>ult:
        return "El elemento no se encuentra"
    med=(pri+ult)//2
    if buscado==v[med]:
        return med
    elif buscado>v[med]:
        return bbin(buscado,v,med+1,ult)
    else:
        return bbin(buscado,v,pri,med-1)


#Ejercicio 21
def contar_naves(vec):
    if(len(vec)==0):
        return 0
    else:
        if(vec[-1][2]):
            return 1 + contar_naves(vec[0:-1])
        else:
            return 0 + contar_naves(vec[0:-1])

#Ejercicio 25
def sucesion2(n):
    if (n==1):
        return 3
    elif (n>=2):
         return sucesion2( n - 1 ) + 2 * n 
