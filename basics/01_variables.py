#Tipado Dinamico en Python

nombre = "Ricardo" # String - > str
edad = 30 # Integer -> int
pi = 3.14 # Float -> float 
activated = True # Boolean -> bool

print("Hola soy Ricardo")

print(type(nombre)) # <class 'str'>
print(type(edad)) # <class 'int'>
print(type(pi)) # <class 'float'>
print(type(activated)) # <class 'bool'>

# Concatenacion
print("Mi nombre es" + nombre + str(edad)) #Python 2
print(f"Mi nombre es {nombre} y tengo {edad}") # Python 3
print(f"El numero pi es: {pi}") # Python 3

var1 = 3
var2 = 4
var3 = var1 + var2
print(var3) # 7

# INPUT
nombre_usuario = input("Ingrese su nombre: ")

# Fases de una variable

#Inicializacion

#Asignacion

#Uso - Utilizacion
print(nombre_usuario)
