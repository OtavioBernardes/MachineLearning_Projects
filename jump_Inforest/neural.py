#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:20:27 2020

@author: otavio
"""


import numpy as np

def criaRede():
    pesosCamada0 = np.random.rand(2,10) # Cria-se um array com 6 elementos, 3 para cada entrada.
    pesosCamada1 = np.random.rand(10,10) # Cria-se um array para a segunda camada 
    pesosCamada2 = np.random.rand(10,1) # Cria-se um array para a terceira camada 
    return pesosCamada0, pesosCamada1, pesosCamada2

def sigmoid(soma): ## Função sigmoid
    return 1 / (1+ np.exp(-soma)) # 1/(1+exp^(-x))


def PulaPersonagem(dist_velo, pesosCamada0, pesosCamada1, pesosCamada2):
    SomaSinapse0 = np.dot(dist_velo, pesosCamada0) ## Multiplicamos as entradas com os pesos respctivios e somamos
    ValoresAtivacaoCamadaOculta0 = sigmoid(SomaSinapse0) ## Utilizando a função sigmoid calculo os valores de ativação dos meu neuronios
    
    SomaSinapse1 = np.dot(ValoresAtivacaoCamadaOculta0, pesosCamada1)
    ValoresAtivacaoCamadaOculta1 = sigmoid(SomaSinapse1)
    
    SomaSinapse2 = np.dot(ValoresAtivacaoCamadaOculta1, pesosCamada2)
    CamadaSaida = sigmoid(SomaSinapse2)
    return CamadaSaida > 0.99

    
