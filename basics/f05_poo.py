# Programacion Orientada a Objetos

# Clase: Template para crear objetos - Kia motors Fabrica -> Generar coches
# Objetos: Color, Puertas, Llantas, parabrisa, motor


# Comportamientos -> funciones -> Arrancar motor, Reversa, Apagarse
# Estados -> Variable(Variables de instancia) -> Modelo, Color, Cantidad llantas

class Kia:
    def __init__(self, modelo, color):
        self.modelo = modelo # Estados
        self.color = color

    def arrancar_motor(self): # Comportamientos
        print(f'Motor arrancando del coche {self.modelo}')
    
    def apagar_motor(self):
        print('Motor apagado')

coche1 = Kia(2025, "Rojo")
coche1.arrancar_motor()

coche2 = Kia(2020, "Azul")
coche2.arrancar_motor()
coche2.apagar_motor()

# Constructores -> Objetos: se encargan de generar los elementos de la instancia

# Conceptos de la POO

# HERENCIA -> Se define como la capacidad de una funcion compartir estados o comportamientos

# POLIMORFISMO -> Capacidad de una funcion para adaptarse a las necesiadades del programa
class Animal:
    def hablar(self):
        print("Este animal hace un sonido")
    
class Perro(Animal):
    def hablar(self):
        print("Guau 🐶")

class Gato(Animal):
    def hablar(self):
        print("Miau 😸")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")

animales = [Perro(), Gato(), Vaca()] # Polimorfismo

for animal in animales:
    animal.hablar()


# ABSTRACCION -> Dejar al programar interpretar el codigo en base a una clase abstracta

from abc import ABC, abstractmethod
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio**2
    
    def perimetro(self):
        return 2 * (3.1416 * self.radio)
    
figuras = [Rectangulo(4,6), Rectangulo(4,4), Circulo(10)]

circulo = Circulo(6)
print(circulo.area())

for f in figuras:
    print(f'Area: {f.area()} Perimetro: {f.perimetro()}')

# ENCAPSULACION -> Proteger datos publicos en funciones con acceso desde MAIN

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # Encapsulado

    def depositar(self, monto):
        self.__saldo += monto # Encapsulado
    
    def consultar_saldo(self):
        return self.__saldo
    
    def consultar_saldo_fecha(self, fecha:str):
        return f'el saldo del dia {fecha} es ${self.__saldo}'

cuenta_miguel = CuentaBancaria(1000)
cuenta_miguel.depositar(1000)
cuenta_miguel.depositar(100000)

print(cuenta_miguel.consultar_saldo_fecha("28 Aug"))

# Generen un metodo que sea para Retirar dinero
# Modifiquen el mentodo de consultar saldo para que imprima el saldo y la fecha

