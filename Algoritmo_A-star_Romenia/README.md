# Problema
O problema consiste em encontrar o melhor caminho de uma cidade do mapa ate a cidade de Bucharest.
![](https://raw.githubusercontent.com/OtavioBernardes/MachineLearning_Projects/master/Algoritmo_A-star_Romenia/imagens/mapa_bucareste.png)
O mapa acima contem a distancia entre cada nó, e na barra lateral a distancia em linha reta de cada cidade ate o objetivo.
# Metodo de Solucão
O metodo escolhido para solucionar o problema foi o algoritmo A*, pois garante que encontre uma solução otima. 
### Heuristica
Minha função de custo é definida pela seguinte heuristica.<br/>
*ValorHeuristica =  Distancia Entre NÓs + Distancia em linha reta + Distancia Percorrida Ate Nó Atual*

Assumindo o mapa acima,  o algoritmo  é capaz de definir uma rota que permita,	a partir de qualquer cidade de origem, chegar  a bucharest,  optando pela melhor rota.

### Exemplo	de entrada:
Cidade de Origem: Arad
O algoritmo irá expandir as cidades vizinhas de Arad e ordena-las pela menor heuristica.
Fila de Prioridade = []
> Zerind
>> Valor Heuristica:   75 + 374 + 0 = 449

> Timisoara
>> Valor Heuristica: 118 + 329 + 0 = 447

> Sibiu 
>> Valor Heuristica: 140 + 253 + 0 = 393

*Fila ordenada em ordem crescente*
##### Fila de Prioridade  = [Sibiu, Timisoara, Zerind]
O algoritmo irá expandir e retirar o 1° elemento da fila.

Continuará expandido as cidades ate chegar ao objetivo.
