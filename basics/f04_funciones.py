'''
Que es una funcion?

* El codigo reutilizable de cualquier archivo de python y se puede invocar
* Declaracion: Def
* Nombre unico de la funcion
* Parametros
'''
def saludar_basico(nombre: str) -> str: # Pythonism: Type Hint o anotacion de tipo
    return f'Hola {nombre}' # Regresar el valor y usarlo fuera de la misma funcion

# Funcion con valores por defecto -> Pythonism
def saludar_defecto(nombre: str = "Invitado"):
    return f'Hola {nombre}'

# Suma
def suma_simple(numero1: int, numero2: int):
    suma_total = numero1 + numero2
    print(f'Suma total {suma_total}')

# Funciones multiparametros
def presentar(nombre: str, edad:int) -> str:
    return f'Yo soy {nombre} y tengo {edad} años'

# Funcion - argumentos variables
def suma_compuesta(*numeros:float):
    print("DEBUG: args ", type(numeros))
    return sum(numeros)

# Funcion - Objetos
def cuadrado(x:float):
    return x * x

# Datos y buenas practicas de funciones

# NO EXISTE LA SOBRECARGA DE FUNCIONES
# Nombre claro
# Una funcion nueva = Una responsabilidad
# esta_funcion_hace_esto 

# Actividad en clase

# Crear una funcion que sume o reste valores recibiendo una cantidad indistinta de numero 
# indistinto de valores

# Pistas: boolean

#min

def operacion(tipo_operacion: str, *numeros: float):
    if tipo_operacion == "suma":
        resultado = sum(numeros)
        return resultado
    elif tipo_operacion == "resta":
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado -= n
        return resultado
    else:
        print("Operacion no valida")
'''
JAVA

public static sumatotal(int numero1, int numero2){
    int suma_total = numero1 + numero2
    System.out.println(suma_total)
}

'''
