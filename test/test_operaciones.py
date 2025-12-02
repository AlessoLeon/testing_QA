import pytest
from calculadora import calculadora

def test_suma():
    assert calculadora.sumar(2,4) == 6

def test_division_por_cero():
    with pytest.raises(ValueError):
        calculadora.dividir(10, 0)

@pytest.mark.parametrize("a,b,esperado", [
    (2,5,7),    # numeros positivos
    (-4,-2,-6), # numeros negativos
    (0,0,0)     # numeros ceros
])
def test_sumer_varios(a,b,esperado):
    assert calculadora.sumar(a,b) == esperado

def test_restar_com_fixture(numeros):
    a, b = numeros
    assert calculadora.restar(a,b) == 0 

def test_sumar_con_fixture(numeros):
    a,b = numeros
    assert calculadora.sumar(a,b) == 10

@pytest.mark.listorty
def test_sumar_listo():
    assert calculadora.sumar(1,3) == 4

def test_estructura_dicc():

    data = {"nombre" : "Luisa", "edad" : 34}

    assert "nombre" in data
    assert "edad" in data

    assert isinstance(data["nombre"], str)
    assert isinstance(data["edad"], int)

def test_estructura_list():
    items = [{"id":1, "id":2}]

    assert all("id" in item for item in items)