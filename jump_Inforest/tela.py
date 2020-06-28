#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:41:34 2020

@author: otavio
"""
import pygame
from pygame.locals import *

def __init__():
    largura = 500
    altura = 400
    clock = pygame.time.Clock()
    pygame.display.set_caption('Game + Alg. Genético')
    bg = pygame.image.load("/mnt/backup/Development/Portfolio_GitHub/Machine_Learning/jump_Inforest/arts_game/fundo.jpg")
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 18)
    screen = pygame.display.set_mode((largura, altura))  # Tamanho do meu ambiente
    bala = "/mnt/backup/Development/Portfolio_GitHub/Machine_Learning/jump_Inforest/arts_game/bala.png"
    return font, screen,  bala, bg, largura, altura, clock

def Personagem():
    persongem_parado = "/mnt/backup/Development/Portfolio_GitHub/Machine_Learning/jump_Inforest/arts_game/Woodcutter/Woodcutter.png"
    persongem_passo1 = "/mnt/backup/Development/Portfolio_GitHub/Machine_Learning/jump_Inforest/arts_game/Woodcutter/run1.png"
    persongem_passo2 = "/mnt/backup/Development/Portfolio_GitHub/Machine_Learning/jump_Inforest/arts_game/Woodcutter/run2.png"
    persongem_passo3 = "/mnt/backup/Development/Portfolio_GitHub/Machine_Learning/jump_Inforest/arts_game/Woodcutter/run3.png"
    persongem_passo4 = "/mnt/backup/Development/Portfolio_GitHub/Machine_Learning/jump_Inforest//arts_game/Woodcutter/run4.png"
    persongem_pulo = "/mnt/backup/Development/Portfolio_GitHub/Machine_Learning/jump_Inforest/arts_game/Woodcutter/Woodcutter_jump.png"
    return persongem_parado, persongem_passo1, persongem_passo2, persongem_passo3, persongem_passo4, persongem_pulo
    