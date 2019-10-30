# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:42:14 2019

@author: OtaviO
"""
## Função para ajuste de pesos -> peson(n+1) = peso(n) + (taxaAprendizagem * entrada * erro)
import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
pesos = np.array([0.0,0.0])
saidas = np.array([0,0,0,1])
taxaAprendizagem = 0.01

##
def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0 

##  Função que nos retorna a saida, a multiplicação dos pesos pelas entradas.
def CalculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

## Minhas funçar para treinar a machine
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