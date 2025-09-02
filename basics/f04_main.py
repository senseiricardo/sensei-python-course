import f04_funciones

nombre = f04_funciones.saludar_basico("Ruben")
print(nombre)

nombre_defecto = f04_funciones.saludar_defecto("Pavel")
print(nombre_defecto)

f04_funciones.suma_simple(18, 8)

presentar = f04_funciones.presentar("Pepito", 15)
print(presentar)

presentar2 = f04_funciones.presentar("Panchito", 20)
print(presentar2)

suma_total = f04_funciones.suma_compuesta(1,3.3,4.5,5,8,19,100, 80, 1.2)
print(f'La suma compuesta total es: {suma_total}')

area_cuadrado = f04_funciones.cuadrado(4)
print(f'El area de mi cuadrado es: {area_cuadrado}')

resultado = f04_funciones.operacion("multiplicar", 1,2,3,4,5)
print(f'La suma de estos numeros es: {resultado}')