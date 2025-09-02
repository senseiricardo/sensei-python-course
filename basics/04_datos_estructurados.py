print("-"*80)
print("LISTAS")

# Listas

# coleccion ordenada y mutable de elementos
# puede contener cualquier tipo de dato -> str, int, float, bool
# guardar varios valores en una sola variable
# se define como: [] 

# Lista del super
#           0           1              2        3       4           5
super = ["tomate", "desodorante", "pollo", "ketchup", "mayonesa", "pan blanco"]

# Imprimir toda la lista
print(super)

# Acceder a un elemnto -> desodorante
print(super[5])

# Agregar un articulo
super.append("platano")

# Ordenar la lista
super.sort() # Sort: ordenar alfabaticamente o numericamente
print(super)

print("-"*80)
print("TUPLES")

# TUPLES o TUPLA (Spanish)

# Coleccion ordenada pero INMUTABLE (no se puede modificar)
# Almacenar datos que no deben cambiar(e.g coordenadas, dias de la semana, nombre de paises)
# Se define como: ()

coordenadas = (10123243434, 12332322232) # Tupla

# Imprimir el primer valor
#print(coordenadas[0]) -> ERROR porque una tupla no puede modificarse

# Tupla nombre de meses
meses = ("Enero", "Febrero", "Marzo")

# Tuple de colores
colores = ("rojo", "azul", "verde")

color_favorito = colores[1]
print("Tupla de colores: ", colores)
print(f"Mi color favorito es: {color_favorito}")


# Diccionarios (Dict)

print("-"*80)
print("DICTIONARIES")

# Estructura que nos ayuda a guardar valores utilizando clave : valor -> key : value
# Buscar datos por su clave de manera rapida
# Se define como: {}

alumno = {"nombre": "Miguel",
          "edad": "30",
          "curso": "Selenium - Python"}

print(alumno["nombre"]) # Miguel
print(alumno["curso"])

# Agregar clave (Key)
alumno["calificacion"]= 95

# Update
alumno.update({"edad": "31",
               "curso": "Automation con Rest Assured"})

print(alumno)

# Eliminar
alumno.pop("edad")

print(alumno)

# SET (conjunto)
print("-"*80)
print("SET")

# Una coleccion DESORDENADA de elementos unicos (que no se repiten)
# Sirve para eliminar datos duplicados y hacer operaciones de conjuntos
# Union o interseccion
# como se define: {} o con el keyword set()

# Declarar un set - opcion 1
numeros_set = {2,3,5,1,6,5,3} # SET

# Declarar un set - opcion 2
numeros_set2 = [2,4,6,7,8,8,8,2,1] # LISTA
numeros_set2_conv = set(numeros_set2) # SET

# ELIMINAR LOS DUPLICADOS
print(numeros_set)
print(numeros_set2_conv)

planetas = {"Marte", "Tierra", "Marte"}
print(planetas)

# Set operations - Operaciones de Set
print("Interseccion: ", numeros_set & numeros_set2_conv)
print("Union: ", numeros_set | numeros_set2_conv)
print("Diferencia (Diff): ", numeros_set - numeros_set2_conv)