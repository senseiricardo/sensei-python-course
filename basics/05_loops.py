'''
LOOPS

- FOR
- WHILE

'''

'''
FOR:

* Secuencia  que puede recorrer un numero especifico de ciclos o 
recorrer lista, string, o rangos
* Repetir acciones de un numero conocido de veces o sobre colecciones
* Como se usa?

'''

# contador del 1 al 10
for i in range(10): # No funciona
    print(i)

print("-"*70)

for i in range(1,11):
    print(i)

# Recorrer una lista con un for
nombres = ["Ricardo", "Ruben", "Pavel", "Miguel", "Pedrito", "Pablito"]
for nombre in nombres:
    print(f'Hola soy {nombre}')

# Recorrer una lista del tipo int - Ejercicio suma
numeros = [1,2,3,4,5,6,7,8]
suma = 0
for n in numeros:
    # BLOCK CODE - Bloque de codigo
    suma = suma + n
    # suma += n - Compound assignment operator o asignacion compuesto
    print(f'Soy el numero {n}')

print(suma)

# Ejercicio de Suma

'''
While

* Repite el numero de instrucciones mientras la condicion sea verdadera (TRUE)
* Cuando NO sabemos cuantas veces se repetira el ciclo
* Como se usa?
'''
print("-"*70)
x = 0
while x<5:
    print(x)
    x = x +1 # Salida logica

# Ejercicio en clase 
# Sumar los numeros hasta que el usuario escriba 0

'''
suma_2 = 0
num = int(input("Escribe un numero (0 para terminar): "))

while num !=0:
    suma_2 += num
    num = int(input("While-Escribe un numero (0 para terminar): "))
print(f'La suma total es: {suma_2}')

'''

# Ejercicio en clase - Alumno

# While que haga cuenta regresiva del 10 al 1

'''
CONTROL DE LOOPS (Break, Continue)

Break : Salir de ciclo - cuando tenemos una condicion dentro de un ciclo
continue: Salta a la siguiente iteracion

'''
print("-"*70)

for i in range(1,11):
    if i == 7:
        break # Rompe el ciclo
    print(i)

print("-"*70)
# Imprimir los numero del 1 al 10 pero omite los pares

for i in range(1,11):
    if i % 2 == 0:
        print(f'El numero {i} es divisible entre 2')
        continue # Salta al siguiente ciclo
    print(i)


'''
Ciclos anidados

* Un ciclo o loop dentro de otro ciclo
* recorrer tablas, combinaciones o matrices

'''

#Tabla de multiplicar
for i in range(1,21):
    for j in range(1,21):
        print(f'{i} x {j} = {i*j}')
    print("*"*20)

# Sugerencia - cuando en un codigo vemos mas de 2 ciclos anidados significa que puede haber una mejor
# implementacion

# 1- Crear un programa que recorra los numeros del 1 al 20
    # 1.1 Si el numero es divisible entre 3, saltalo (usa continue)
    # 1.2 Si llegas a 15, deten el loop (usa break)

# Nota: Muestra en consola solamente los numeros que NO pasen esas condiciones en los IFs

for i in range(1,21): # 1
    if i % 3 == 0: # 1.1
        #print(f'El numero {i} no paso la primer condicion') # Descomentar solo para entender el codigo
        continue # Saltar el ciclo
    if i == 15: # 1.2
        #print(f'El numero {i} no paso la segunda condicion') # Descomentar solo para entender el codigo
        break 
    print(f'Este numero {i} si paso las condiciones') # Nota