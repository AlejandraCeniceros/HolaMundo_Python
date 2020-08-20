print("hola mundo")
print("adios mundo")
print(4+5)
print(4*5)
print(4/5)
print(4-5)
print(4+5*3+2)
print(4+5*(3+2))


#tipos de datos

print(type(2))
print(type(3.22))
print(type("texto"))
print(type('texto'))
print(type("5"))

#Variables de memoria
mensaje = "esto es un mensaje"
print(mensaje)
mensaje = "esto es un mensaje modificado"
print(mensaje)
print(mensaje)
print(type(mensaje))
mensaje=1010
print(mensaje)
print(type(mensaje))

mis3animales = "perico, gllo, chivo"
print(mis3animales)
animales_3= "perico, gallo, chivo"
print(animales_3)

textoUno = "mi texto"
textoDos = "mi segundo texto"
print(textoUno+textoDos)
edad=20
print("La edad del usuario es:" + str (edad))
print("El tipo de dato de edad es:"+ str( type(edad)))

import math
grados =45
radianes =grados * math.pi /180
seno = math.sin(radianes)
print("seno de 45°: " +str (seno))
#funciones en python:

def saludar (nombre): 
    print("hola " + nombre)
    print("¿como estas?")
    
    print("te saludo de lejos c:")
def despedir():
    print("ya me voy")
    print("luego nos abrazamos")

def concatenar (parte1, parte2):
    return parte1 + parte2

print( "esto no es parte de la funcion")
saludar("Emiliano")
despedir()

frase = concatenar ("Hola ," , "adios")
print = frase