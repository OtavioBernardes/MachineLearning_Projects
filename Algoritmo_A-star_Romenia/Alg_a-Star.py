CidadeObjetivo = 'Bucharest'  # Objetivo a ser atingido
filaPrioridadeCidade = [] # Fila de Prioridade de cidades, em ordem por menor custo.
# Declaração do dicionario, que representa o grafo de cidades. No exemplo da cidade de SIBIU logo a baixo estão as seguintes informações: [NomeCidade, Distancia de Sibiu ate Arad, Distancia de Sibiu ate Objetivo]
grafocidades = {'Arad':[['Zerind', 75, 374], ['Timisoara', 118, 329], ['Sibiu', 140, 253]],
                'Bucharest':[['Fagaras', 211,178], ['Pitesti', 101, 101], ['Giurgiu', 90, 77], ['Urziceni', 85, 80]],
                'Craiova': [['Dobreta', 120,242], ['RimnicuVilcea' ,146, 193], ['Pitesti', 138, 101]],
                'Dobreta': [['Craiova', 120,160], ['Mehadia', 75,241]],
                'Eforie': [['Hirsova', 86, 151]],
                'Fagaras': [['Sibiu', 99,253], ['Bucharest', 211,0]],
                'Giurgiu': [['Bucharest', 90,0]],
                'Hirsova': [['Eforie', 86,161], ['Urziceni', 98, 80]],
                'Iasi': [['Neamt', 87,234], ['Vaslui', 92]],
                'Lugoj': [['Timisoara', 111, 329], ['Mehadia', 70,241]],
                'Mehadia': [['Lugoj', 70,244], ['Dobreta', 75,242]],
                'Neamt': [['Iasi', 87, 226]],
                'Oradea': [['Zerind', 71,374],['Sibiu', 151,253]],
                'Pitesti': [['RimnicuVilcea', 97,193], ['Craiova', 138,160], ['Bucharest', 101,0]],
                'RimnicuVilcea': [['Pitesti', 97, 101], ['Sibiu', 80,253], ['Craiova', 146,160]],
                'Sibiu': [['RimnicuVilcea', 80,193], ['Oradea', 151,380], ['Arad', 140,366],['Fagaras', 99,178]],
                'Timisoara': [['Arad', 118,366], ['Lugoj', 111,244]],
                'Urziceni': [['Bucharest', 85,0], ['Vaslui', 144, 199], ['Hirsova', 98, 151]],
                'Vaslui': [['Urziceni', 142, 80], ['Iasi', 92,226]],
                'Zerind': [['Arad', 75,366], ['Oradea', 71,380]]}
                
def OrdenarFILA(): # Ordenada a lista de prioridade com base nos valores de heuristica (Algoritmo de ordenação Selection Sort)  
    for i in range(len(filaPrioridadeCidade)):
        auxPos = -1
        aux = filaPrioridadeCidade[i][1]
        for j in range(i, len(filaPrioridadeCidade)): # Irá encontrar o menor elemento de um intervalo da lista
            if (filaPrioridadeCidade[j][1] < aux): 
               aux = filaPrioridadeCidade[j][1]
               auxPos = j
        if(filaPrioridadeCidade[auxPos][1] < filaPrioridadeCidade[i][1]): # Trocando elementos de posicação
            aux = filaPrioridadeCidade[i]
            filaPrioridadeCidade[i] = filaPrioridadeCidade[auxPos]
            filaPrioridadeCidade[auxPos] = aux

def AdicionaElementosListaPrioridade(cidade, distanciaPercorrida, cidadespercorridas): # Adiciona as cidades na lista de prioridade e retorna o 1° elemento da lista ordenada
    for i in range(len(grafocidades[cidade])): #Dados gravados na lista: [NomeCidade, Heuristica, DistanciaPercorridaAteEsseNó, CidadesPercorridasAteEsseNó]
        filaPrioridadeCidade.append([grafocidades[cidade][i][0],grafocidades[cidade][i][1]+grafocidades[cidade][i][2]+distanciaPercorrida, grafocidades[cidade][i][1]+distanciaPercorrida, cidadespercorridas+'\n'+cidade])    
    OrdenarFILA()
    return filaPrioridadeCidade[0][0], filaPrioridadeCidade[0][2], filaPrioridadeCidade[0][3] # Retorna as informações do 1° elemento da fila

def expandeCidade(cidade, distanciaPercorrida, cidadesPercorridasAteNóAtual):
    if(cidade == CidadeObjetivo): # Verifica se chegou ao objetivo
        print('\nVocê chegou em bucharest!\nCaminho Percorrido ate o objetivo:', cidadesPercorridasAteNóAtual,'\nBucharest')
    else: 
        ProximaCidade, distanciaPercorrida, cidadesPercorridasAteNóAtual = AdicionaElementosListaPrioridade(cidade, distanciaPercorrida, cidadesPercorridasAteNóAtual)
        del(filaPrioridadeCidade[0]) # Exclui o 1° elemto da fila
        expandeCidade(ProximaCidade, distanciaPercorrida, cidadesPercorridasAteNóAtual) # Expande proxima cidade

#_____________main____________
expandeCidade('Arad',0, '') #Cidade Origem, Distancia percorrida inicial, Cidades já percorridas.
