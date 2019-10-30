# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:42:14 2019
@author: OtaviO

Nesse codigo implento algumas definições de machine learning, como ajuste de pesos,
stepFunction, taxa de aprendizagem, dentre outros conceitos básicos.
"""

import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
pesos = np.array([0.0,0.0]) # Iniciamos a nossa implentação com ambos os pesos zerados.
saidas = np.array([0,0,0,1]) # Como é uma porta AND, somente no array [1,1] que a stepFunction podera retornar 1
taxaAprendizagem = 0.01

## Função que nos retorna se o valor da multiplicação da entrada e do peso é ou não >= 1
def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0 

##  Função que nos retorna a saida, a multiplicação dos pesos pelas entradas.
def CalculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

## Função que irá realizar o ajuste dos pesos.
def TreinarMachine():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = CalculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Pesso atualizado: ' + str(pesos[j]))
            print('Total de erros: ' + str(erroTotal))
    
## Main
TreinarMachine()
print("Novos pesos:\nPeso 1: {} \nPeso 2: {}".format(pesos[0], pesos[1]))