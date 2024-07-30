

class Cuenta:
    def __init__(self, titular, saldo, numero_cuenta):
        self.titular = titular
        self.saldo = saldo
        self._numero_cuenta = numero_cuenta  # El guion bajo indica que es un atributo privado

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print(f"Número de cuenta: {self._numero_cuenta}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print("Depósito realizado con éxito.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro realizado con éxito.")
        else:
            print("Fondos insuficientes o cantidad a retirar inválida.")

# Ejemplo de uso:
cuenta1 = Cuenta("Juan Pérez", 1000, "123456789")
cuenta1.mostrar_informacion()
cuenta1.depositar(500)
cuenta1.mostrar_informacion()
cuenta1.retirar(200)
cuenta1.mostrar_informacion()