listaPrioridadeCidades = [] # Lista de prioridade de cidades com os respectivos dados: NomeCidade, heurÃ­stica, Distancia Percorrida do ponto inicial ate a cidade
CidadeObjetivo = 'Bucharest'  # Objetivo a ser atingido
# Declaração do dicionario, que representa o grafo com as cidades. No exemplo de Sibiu logo a baixo: [NomeCidade, Distancia de Sibiu ate Arad, Distancia de Sibiu ate Objetivo]
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

def OrdenaListaPrioridade(): # Ordenada a lista de prioridade com base nos valores de heurÃ­stica de cada elemento
    for i in range(len(listaPrioridadeCidades)):
        aux = listaPrioridadeCidades[i][1]
        for j in range(len(listaPrioridadeCidades)):
            if(listaPrioridadeCidades[j][1] > aux):
                auxCidade = listaPrioridadeCidades[j]
                listaPrioridadeCidades[j] = listaPrioridadeCidades[i]
                listaPrioridadeCidades[i] = auxCidade

def AdicionaElementosListaPrioridade(cidade, distanciaPercorrida): # Adiciona as cidades na lista de prioridade e retorna o 1° elemento da lista ordenada
    for i in range(len(grafocidades[cidade])):
        listaPrioridadeCidades.append([grafocidades[cidade][i][0],grafocidades[cidade][i][1]+grafocidades[cidade][i][2]+distanciaPercorrida, grafocidades[cidade][i][1]+distanciaPercorrida])    
    OrdenaListaPrioridade()
    return listaPrioridadeCidades[0][0], listaPrioridadeCidades[0][2] # Retorna o 1° elemento da lista ordenada

def expandeCidade(cidade, distanciaPercorrida):
    print('Cidade Percorrida atual:', cidade,'\nDistancia Percorrida ate cidade atual:',distanciaPercorrida,'\n')
    if(cidade == CidadeObjetivo): # Verifica se o objetivo foi atingido
        print('Você chegou a bucharest!!!!')
    else: 
        ProximaCidade, distanciaPercorrida = AdicionaElementosListaPrioridade(cidade, distanciaPercorrida)
        del(listaPrioridadeCidades[0]) # Retira da lista a Cidade a ser expandida
        expandeCidade(ProximaCidade, distanciaPercorrida) # Expande proxima cidade
#_____________main____________
expandeCidade('Oradea',0)
