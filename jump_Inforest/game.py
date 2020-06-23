import pygame # Biblioteca para construir o game
import numpy as np 
from tela import __init__, Personagem # Modulo que importa os sprits do game 
from pygame.locals import *
from neural import PulaPersonagem, criaRede # Modulo que importa a rede neural
# --------------------------------- Variaveis do Game ---------------------------------
objeto = 0 # Obstaculo
objeto_skin = 0 # skin do obstaculo
FPS = 15 # FPS do Game
Velocidade = 0.95 # Velocidade do obstaculo
font, screen,  bala, bg, largura, altura, clock = __init__() # Iniciando componetes da tela
# ------------------------------ Variaveis do Alg. Genético --------------------------------
CHANCE_MUT = .50     # Chance de mutação de um peso qualquer
CHANCE_CO = .50     # Chance de crossing over de um peso qualquer
NUM_INDIVIDUOS = 2  # Tamanho da população
NUM_MELHORES = 0     # Número de indivíduos que são mantidos de uma geração para a próxima
NUM_GERACOES = 100
# ------------------------------ Funções do Alg. Genético --------------------------------
         
def CriaPopulacao():
    lista = []
    for i in range(NUM_INDIVIDUOS):
        lista.append([_Personagem(), False, 0])
    return lista

def OrdenaLista(lista):
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i][2] < lista[j][2]:
                lista[i][2], lista[j][2] = lista[j][2], lista[i][2]   
    return lista

def Roleta(lista):
    individuos_cros = []
    scoretotal = 0
    for i in range(NUM_MELHORES,len(lista)):
        scoretotal += lista[i][2]
        
    for i in range(NUM_MELHORES,len(lista)): # normalização
        lista[i][2] = lista[i][2]/scoretotal
    for i in range(0, int(NUM_INDIVIDUOS*CHANCE_CO)):
        valor = np.random.rand()
        acumulado = 0.00
        
        for j in range(NUM_MELHORES,len(lista)): # acumulado
            acumulado += lista[j][2]
            if (valor < acumulado):
                individuos_cros.append(j)      
    return individuos_cros

def mutacao(lista):
    for c in range(NUM_MELHORES+int(NUM_INDIVIDUOS*CHANCE_CO),NUM_INDIVIDUOS):
        indipesos1, indipesos2, indipesos3 = lista[c][0].RetornaParametros()
        newpesos1 = []
        newpesos2 = []
        newpesos3 = []
        for i in range(len(indipesos1)):
            for j in range(len(indipesos1[i])):
                newpesos1.append(str(indipesos1[i][j])[0:3] +'0' + str(indipesos1[i][j])[4:6])

        newpesos1 = np.asarray(newpesos1,dtype=float)
        newpesos1 = np.reshape(newpesos1, (len(indipesos1),len(indipesos1[0])))

        for i in range(len(indipesos2)):
            for j in range(len(indipesos2[i])):
                newpesos2.append(str(indipesos2[i][j])[0:3] +'0' + str(indipesos2[i][j])[4:6])
        newpesos2 = np.asarray(newpesos2,dtype=float)
        newpesos2 = np.reshape(newpesos2, (len(indipesos2),len(indipesos2[0])))
        
        for i in range(len(indipesos3)):
            for j in range(len(indipesos3[i])):
                newpesos3.append(str(indipesos3[i][j])[0:3] +'0' + str(indipesos3[i][j])[4:6])
        newpesos3 = np.asarray(newpesos3,dtype=float)
        newpesos3 = np.reshape(newpesos3, (len(indipesos3),len(indipesos3[0])))
        
        lista[c][0].RedefiniRede(newpesos1, newpesos2, newpesos3)
        lista[c][1] = False
        lista[c][2] = 0

def crossover(lista, individuos_cros):
    lista_individuos_cruzados = []
    for c in range(int(NUM_INDIVIDUOS*CHANCE_CO)):
        individuo1 = int(np.random.choice(individuos_cros))
        individuo2 = int(np.random.choice(individuos_cros))
        if(individuo1 == individuo2):
            individuo2 = np.random.choice(individuos_cros)
        indi1pesos1, indi1pesos2, indi1pesos3 = lista[individuo1][0].RetornaParametros()
        indi2pesos1, indi2pesos2, indi2pesos3 = lista[individuo2][0].RetornaParametros()
        newpesos1 = []
        newpesos2 = []
        newpesos3 = []
        for i in range(len(indi1pesos1)):
            for j in range(len(indi1pesos1[i])):
                newpesos1.append(str(indi1pesos1[i][j])[0:3] + str(indi2pesos1[i][j])[3:7])
        newpesos1 = np.asarray(newpesos1,dtype=float)
        newpesos1 = np.reshape(newpesos1, (len(indi1pesos1),len(indi1pesos1[0])))
        
        for i in range(len(indi1pesos2)):
            for j in range(len(indi1pesos2[i])):
                newpesos2.append(str(indi1pesos2[i][j])[0:3] + str(indi2pesos2[i][j])[3:7])
        newpesos2 = np.asarray(newpesos2,dtype=float)
        newpesos2 = np.reshape(newpesos2, (len(indi1pesos2),len(indi1pesos2[0])))
        
        for i in range(len(indi1pesos3)):
            for j in range(len(indi1pesos3[i])):
                newpesos3.append(str(indi1pesos3[i][j])[0:3] + str(indi2pesos3[i][j])[3:7])
        newpesos3 = np.asarray(newpesos3,dtype=float)
        newpesos3 = np.reshape(newpesos3, (len(indi1pesos3),len(indi1pesos3[0])))
        
        lista_individuos_cruzados.append([_Personagem(), False, 0])
        lista_individuos_cruzados[c][0].RedefiniRede(newpesos1, newpesos2, newpesos3)
    return lista_individuos_cruzados

def proximageracao(lista):
    for i in range(NUM_MELHORES):
        lista[i][0].LimpaParametros()
        lista[i][1] = False
        lista[i][2] = 0
        
    individuos_cros = Roleta(lista)
    lista_individuos_cruzados = crossover(lista, individuos_cros)
    for i in range(NUM_MELHORES,NUM_MELHORES+int(NUM_INDIVIDUOS*CHANCE_CO)):
        lista[i] = lista_individuos_cruzados[i-NUM_MELHORES]
    mutacao(lista)
    return lista
# ------------------------------ Funções do Game --------------------------------

def criaobjeto():
    objeto = [np.random.randint(largura-200,largura), 205]  # Posicão inicial do objeto
    objeto_skin = pygame.Surface((10, 10))  # Tamanho do objeto
    objeto_skin = pygame.image.load(bala)
    return objeto, objeto_skin, 1

class _Personagem():
    def __init__(self):
        self.PULA = 0 
        self.andar = 0
        self.game_over = False
        self.score = 0
        self.pesosCamada0, self.pesosCamada1, self.pesosCamada2 = criaRede()
        
    def RedefiniRede(self, new0, new1, new2):
         self.pesosCamada0, self.pesosCamada1, self.pesosCamada2 = new0, new1, new2
         self.LimpaParametros()
    def LimpaParametros(self):
        self.PULA = 0 
        self.andar = 0
        self.game_over = False
        self.score = 0
        
    def RetornaParametros(self):
        return self.pesosCamada0, self.pesosCamada1, self.pesosCamada2

    def JogaPersonagem(self, _):
        persongem_parado, persongem_passo1, persongem_passo2, persongem_passo3, persongem_passo4, persongem_pulo = Personagem()
        self.x = np.random.randint(185,215)
        self.monkey = [self.x, 200]
        self.monkey_skin = pygame.Surface((10, 35))
        self.monkey_skin = pygame.image.load(persongem_parado)
        

        if(self.monkey[0] == 200 and self.monkey[1] == self.x):  # Se o macaco estiver no chão
            self.PULA = 0  # Defini PULA como 0
            self.monkey_skin = pygame.image.load(persongem_passo1)
        
        if(self.PULA == 1):  # Se o macaco estiver em um salto
            self.monkey_skin = pygame.image.load(persongem_pulo)
            self.monkey = (self.monkey[0], self.monkey[1]+10)  # A cada ciclo ele desce 15 pixels
        
        if(self.andar == 0 and self.PULA == 0):
            self.monkey_skin = pygame.image.load(persongem_passo1)
            self.andar = 1
        elif(self.andar == 1 and self.PULA == 0):
            self.monkey_skin = pygame.image.load(persongem_passo2)
            self.andar = 2
        elif(self.andar == 2 and self.PULA == 0):
            self.monkey_skin = pygame.image.load(persongem_passo3)
            self.andar = 3
        elif(self.andar == 3 and self.PULA == 0):
           self.monkey_skin = pygame.image.load(persongem_passo4)
           self.andar = 0
           
           # BUG 
        if(self.monkey[1] == self.x and objeto[0] >= 197.5 and objeto[0] <= 202.5):
            self.game_over = True
        elif(self.monkey[1] == self.x and objeto[0]+10*Velocidade > 202.5 and objeto[0] < 197.5):
            self.game_over = True
            
        if PulaPersonagem((objeto[0] - self.monkey[0],Velocidade), self.pesosCamada0, self.pesosCamada1, self.pesosCamada2) and self.PULA == 0:  # Se o usuario apertar spaco e o macaco estiver no chão
            for i in range(10):    
                self.monkey = (self.monkey[0], self.monkey[1]-10)  # Macaco salta
            self.PULA = 1
       
        if(objeto[0] < self.monkey[0] and self.game_over != True and _ == 1):
            _ = 0
            self.score = self.score + 1
            
        screen.blit(self.monkey_skin, self.monkey)
        screen.blit(objeto_skin, objeto)
        pygame.display.update()
        return self.game_over, self.score, _

# ---------------------------- Rota do Game + Alg. Genético ------------------------------

populacao = CriaPopulacao()
MelhorScore = [0,0]
for e in range(NUM_GERACOES):
    while(True):
        gameover = True
        screen.blit(bg, (-100, 0))
        populacao_font = font.render('População N°: %s' % (e), True, (255, 255, 255))
        populacao_rect = populacao_font.get_rect()
        populacao_rect.topleft = (450, 10)
        screen.blit(populacao_font, populacao_rect)
        score_font = font.render('Melhor Score: %s' % (MelhorScore[0]), True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topright = (140, 30)
        screen.blit(score_font, score_rect)
        Populacaoscore_font = font.render('Populacao com melhor Score: %s' % (MelhorScore[1]), True, (255, 255, 255))
        Populacaoscore_rect = Populacaoscore_font.get_rect()
        Populacaoscore_rect.topright = (280, 10)
        screen.blit(Populacaoscore_font, Populacaoscore_rect)
        clock.tick(FPS)  # FPS por segundo
        for event in pygame.event.get():
            if event.type == QUIT:  # Se apertar no x, fecha o game
                pygame.quit()
        if(objeto == 0):
            objeto, objeto_skin, _ = criaobjeto()
        for i in range(NUM_INDIVIDUOS):
            if populacao[i][1] != True:
                gameover = False
                populacao[i][1], populacao[i][2], a = populacao[i][0].JogaPersonagem(_)
        _ = a
        if gameover == True:
            break
        objeto = (objeto[0]-(10*Velocidade), objeto[1])
        if(objeto[0] <= 15):
            if(Velocidade <= 3.5):
                Velocidade *= 1.10
            objeto = 0
    populacao = OrdenaLista(populacao)
    if(populacao[0][2] > MelhorScore):
        MelhorScore = populacao[0][2]
        MelhorScore = e
    populacao = proximageracao(populacao)