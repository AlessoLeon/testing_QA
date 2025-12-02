class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

# instancia exportada para mantener compatibilidad con los tests
calculadora = Calculadora()

# funciones a nivel de modulo (opcional)
def sumar(a, b):
    return calculadora.sumar(a, b)

def restar(a, b):
    return calculadora.restar(a, b)

def dividir(a, b):
    return calculadora.dividir(a, b)
