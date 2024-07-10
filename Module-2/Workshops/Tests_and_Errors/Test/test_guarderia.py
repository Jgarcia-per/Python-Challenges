import pytest
from Class.guarderia import Guarderia

def test_alimentar_boa_exito():
    guarderia = Guarderia()
    boa = guarderia.boas[0]
    result = guarderia.alimentar_boa(boa)
    assert result == "Éxito"
    assert boa.get_ratones_comidos() == 1

def test_alimentar_boa_llena():
    guarderia = Guarderia()
    boa = guarderia.boas[0]
    for _ in range(10):
        guarderia.alimentar_boa(boa)
    result = guarderia.alimentar_boa(boa)
    assert result == "La boa está llena"
    assert boa.get_ratones_comidos() == 10

def test_alimentar_boa_no_existe():
    guarderia = Guarderia()
    result = guarderia.alimentar_boa(None)
    assert result == "Esta Boa no existe!"
