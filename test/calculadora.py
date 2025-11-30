def suma( a , b ) :
    return a + b

def resta ( a, b ) :
    return a - b 

def multiplicar ( a, b ) :
    return a * b

def dividir ( a, b ):
    if b == 0 :
        raise ValueError("Error al dividir por cero")
    return a / b 

def calculadora_simple ( operacion, a, b ):
    try:
        a = int(a)
        b = int(b)

        if operacion == "suma":
            return suma(a, b)
        elif operacion == "resta":
            return resta(a, b)
        elif operacion == "multiplicar":
            return multiplicar(a, b)
        elif operacion == "dividir":
            return dividir(a, b)
        else:
            raise ValueError("Operación no válida")
        
    except ZeroDivisionError:
        return 'Error : No se puede dividir por cero.'
    except ValueError:
        raise 'Error : Los valores deben ser numericos.'