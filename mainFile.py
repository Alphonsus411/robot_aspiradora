"""
Le proponemos realizar un proyecto que consiste en la escritura de un script Python que
permite a un robot aspirador calcular la superficie de una habitación y estimar el tiempo
necesario para limpiarla.

Imaginemos que la habitación que hay que limpiar contiene un mueble debajo del cual
no puede meterse el robot y que tiene las siguientes características:

- Es un mueble situado en medio de una habitación de 31.5 mts cuadrados
- Está situado a 220 cts de orientación Sur, 309 cts de orientación Este,
150 cts de orientación Norte y 101 cts de orientación Oeste.

SOLUCIÓN: una de formas posibles de calcular la superficie que debe limpiar el robot
consiste en fragmentar la superficie total en zonas utilizables:

ZONA    |    LARGO(cts)|    ANCHO (cts)

Zona 1   |   500            |       150
Zona 2   |  480             |       101
Zona 3   |   309            |       480
Zona 4   |   90              |        220

Una vez fragmentada, es fácil calcular la superficie total que hay que limpiar, añadiendo
las superficies de cada zona. Estas superficies se calculan multiplicando el largo por el ancho
en cada una de ellas.


"""

# ------------------------------
# APLICACIÓN
# ------------------------------

# Empleo de una tupla para la configuración de la aplicación
# Nombre del robot, tiempo en minutos para limpiar un metro cuadrado
parametros = ("robot aspirador", 2)

# Empleo de diccionarios para crear las zonas
zona1 = {"largo": 500, "ancho": 150}
zona2 = {"largo": 101, "ancho": 480}
zona3 = {"largo": 309, "ancho": 480}
zona4 = {"largo": 90, "ancho": 220}

"""
Una vez definidas las zonas, vamos a guardarlas en una lista para poder acceder a ellas con más
facilidad desde un punto único representado por la lista. 
"""

# Empleo de una lista que permite guardar las zonas
zonas = []
zonas.append(zona1)
zonas.append(zona2)
zonas.append(zona3)
zonas.append(zona4)

"""
Función para calcular la superficie que se ha de limpiar: el propósito de esta función, 
es calcular la superficie total que se ha de cubrir con la limpieza. Ésta, se calculará a partir
de las características de las zonas que le indicaremos mediante los parámetros. 

Al describir la función mediante la creación de un algoritmo, obtenemos lo siguiente:

1.- Creación de la variable superficieATotalLimpiar y inicialización = 0
2.- Para cada zona a limpiar incluida en la lista de las zonas indicada mediante los parámetros:
    - recuperar el largo de la zona y almacenarlo en una variable
    - recuperar el ancho de la zona y almacenarlo en una variable
    - calcular la superficie de la zona multiplicando el largo por el ancho
    - añadir, a la superficie total a limpiar, la superficie de la zona que acabamos de definir. 
3.- Reenviar la superficieTotalALimpiar
"""


def calculoDeLaSuperficieALimpiar(listaDeZonas):
    superficieALimpiar = 0
    for zona in listaDeZonas:
        largo = zona.get("largo") / 100
        ancho = zona.get("ancho") / 100
        calculo = largo * ancho
        print(str(largo) + " x " + str(ancho) + " =" + str(calculo))
        superficieALimpiar = superficieALimpiar + calculo

    return (superficieALimpiar)


"""
La instrucción def permite definir una función que lleva un nombre (calculoDeLaSuperficieALimpiar) 
y posiblemente uno o varios parámetros(listaDeZonas en nuestro caso). El uso de los dos puntos permite
definir el inicio de la función. El cuerpo se escribe respetando los sangrados presentes en Python. 

Si analizamos el código de nuestra función, podemos constatar la creación de una primera variable llamada
superficieALimpiar, que está inicializada a 0. A continuación viene el recorrido por las zonas guardadas en 
la lista de zonas enviada mediante parámetros mediante la instrucción for. Como cada zona es un diccionario, 
se puede acceder a los datos con las claves largo y ancho para calcular la superficie a limpiar. Al final, la instrucción 
return devuelve la superficie calculada. 

Nuestra función ya está programada, sólo hay que usarla en el programa:
"""
superficieALimpiar = calculoDeLaSuperficieALimpiar(zonas)
print("La superficie total a limpiar es de: " + str(superficieALimpiar))

"""
Ahora vamos a crear una segunda función que permite calcular el tiempo de limpieza en función 
de la superficie y del tiempo de limpieza para un metro cuadrado, enviados mediante parámetros. 

Aquí podemos ver el código de la función que se puede añadir debajo de la función de cálculo de la superficie.
"""


def tiempoDeLimpiezaEnMinutos(superficieALimpiar, tiempoParaUnMetroCuadrado):
    return round(superficieALimpiar * tiempoParaUnMetroCuadrado)

"""
El tiempo calculado reenviado por la función es el resultado del redondeo (round) de la multiplicación de
la superficie que hay que limpiar por el tiempo de limpieza para un metro cuadrado. 

Veamos este script en conjunto:
"""

# llamada de la función que permite calcular la superficie de limpieza:
superficieALimpiar = calculoDeLaSuperficieALimpiar(zonas)
print("La superficie total a limpiar es de: " + str(superficieALimpiar) + "m2")

# Llamada de la función que permite determinar el tiempo de limpieza:
tiempoEstimado = tiempoDeLimpiezaEnMinutos(superficieALimpiar, parametros[1])
print("El tiempo estimado es:" + str(tiempoEstimado) + "minutos")

# Añade una condición que se activa en función del tiempo de limpieza:
if tiempoEstimado > 55:
    print(parametros[0] + " dice: Me parece que esto va a tardar un poco! ")
