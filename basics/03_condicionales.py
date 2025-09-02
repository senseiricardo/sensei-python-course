edad = 35 # años
tiene_id = False

     #Cond1.     Cond2
if edad>=18 or tiene_id:
    # Block code
    print("Puedes entrar a un bar🍻")
else:
    print("No puedes entrar a un bar🍻")


# Pythonismos - Conditionals
var = 12
if 0 < var < 10:
    print("El numero esta en rango")

color = "verde"
if color in ("azul", "amarillo", "verde", "rojo", "cafe"):
    print(f"Color {color} - valido")
else:
    print(f"Color {color} - no valido")


# IF / ELSE / IF ELSE

# Calificaciones
'''
calificacion = int(input("Ingresar calificacion del alumno (0-100): "))

if calificacion >= 90:
    print("Excelente")
elif calificacion >=70:
    print("Aprobado")
elif calificacion>=50:
    print("Reprobado - echale ganas!")
else:
    print("Completamente reprobado")

    '''
# Tarifas

#peso
#precio

# Peso 1 - Si el articulo pesa mas de 5 kg -> $100
# Peso 2 - si el articulo pesa mas de 10 kg -> $500
# Peso 3 - si el articulo pesa menos de 5 kg -> $50
# Peso 4 - si el articulo pesa mas de 50 kg -> 35 por cada kilo

# Pistas:

'''

Estructura de control
Operadores aritmeticos y comparacion

'''

'''

MATCH - Estructura condicional apartir de python 3.10

'''

# TODO: Mejorar la implementacion del metodo "metodo_2"

dia = "Jueves"

match dia:
    case "Lunes":
        print("Animo! es Lunes!")
    case "Martes" | "Miercoles":
        print("Dia de Curso Selenium con Python")
    case "Sabado" | "Domingo":
        print("fin de semana")
    case _:
        print("Dia normal")

opcion = 10

match opcion:
    case 1:
        print("Retirar efvo")
    case 2:
        print("consultar saldo")
    case 3:
        print("Depositar")
    case _:
        print("Opcion no valida")

# MATCH con Intervalos de valores (Guards o condiciones de guarda)

temperatura = 32 # Monterrey
temperatura = 22 # CDMX
temperatura = -12 # Groenlandia
temperatura = 43 # Mexicali

match temperatura:
    case t if t < 0:
        print("Hace mucho frio (bajo cero)")
    case t if t <= t <= 15:
        print("Clima frio")
    case t if 16 <= t <= 25:
        print("Clima templado")
    case t if 26 <= t <= 35:
        print("Hace calor")
    case t if t > 35:
        print("Calor extremo")
    case _:
        print("Valor desconocido")
