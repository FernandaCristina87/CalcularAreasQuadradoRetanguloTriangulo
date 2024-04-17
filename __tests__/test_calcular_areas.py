
# biblioteca
import pytest 

from calcular_areas.calcular_areas import calcular_area_quadrado, calcular_area_retangulo, calcular_area_triangulo
from utils.utils import ler_csv

# Funções
def test_calcular_area_quadrado():
    #configura
    lado=4
    resultado_esperado=16
    #executa
    resultado_obtido=calcular_area_quadrado(lado)
    #valida
    assert resultado_esperado==resultado_obtido

def test_calcular_area_retangulo():
    #configura
    base=8
    altura=5
    resultado_esperado=40
    #executa
    resultado_obtido=calcular_area_retangulo(base, altura)
    #valida
    assert resultado_esperado==resultado_obtido

def test_calcular_area_triangulo():
    #configura
    base=5
    altura=4
    resultado_esperado=10
    #executa
    resultado_obtido=calcular_area_triangulo(base, altura)
    #valida
    assert resultado_esperado==resultado_obtido

@pytest.mark.parametrize('lado, resultado_esperado',
                         [
                            (8,64),
                            (5,25),
                            (3,9)
                         ]
                         )
def test_calcular_area_quadrado_lista(lado, resultado_esperado):
    #configura
   
    #executa
    resultado_obtido=calcular_area_quadrado(lado)
    #valida
    assert resultado_esperado==resultado_obtido

@pytest.mark.parametrize('base, altura, resultado_esperado',
                         [
                            (8,4,32),
                            (5,3,15),
                            (3,1,3)
                         ]
                         )
def test_calcular_area_retangulo_lista(base, altura, resultado_esperado):
    #configura
   
    #executa
    resultado_obtido=calcular_area_retangulo(base, altura)
    #valida
    assert resultado_esperado==resultado_obtido

@pytest.mark.parametrize('base, altura, resultado_esperado',
                         [
                            (5,4,10),
                            (5,10,25),
                            (10,3,15)
                         ]
                         )
def test_calcular_area_triangulo_lista(base, altura, resultado_esperado):
    #configura
   
    #executa
    resultado_obtido=calcular_area_triangulo(base, altura)
    #valida
    assert resultado_esperado==resultado_obtido

@pytest.mark.parametrize('lado, resultado_esperado', 
                            ler_csv('./fixtures/massa.calcular_areas.csv')
                        )

def test_calcular_area_quadrado_csv(lado, resultado_esperado):
    #configura
  
    #executa
    resultado_obtido = calcular_area_quadrado(float(lado))
    #valida
    assert float(resultado_esperado) == resultado_obtido




