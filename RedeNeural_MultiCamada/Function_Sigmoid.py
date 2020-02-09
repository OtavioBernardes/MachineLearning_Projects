import numpy as np

def sigmoid(soma): ## Função sigmoid
    return 1 / (1+ np.exp(-soma)) # 1/(1+exp^(-x))

def sigmoidDerivada(sig): ## Calculando a derivada parcial da função sigmoid
        return sig * (1 - sig) # d= y * (1-y)

entradas = np.array([[0,0], [0,1], [1,0], [1,1]]) # Declarei as entradas da minha porta logica
saidas = np.array([[0], [1], [1], [0]]) # A saida esperada da minha porta XOR 
pesosCamada0 = np.random.rand(2,3) # Cria-se um array com 6 elementos, 3 para cada entrada.
pesosCamada1 = np.random.rand(3,1) # Cria-se um array para a segunda camada 
momento = 1
taxaAprendizagem = 0.05
epocas = 100000 # Para nosso algoritmo não ficar muito extenso, colocamos um limite para ele se repetir
for j in range(epocas): 
    CamadaEntrada = entradas # Copia 
    SomaSinapse0 = np.dot(CamadaEntrada, pesosCamada0) ## Multiplicamos as entradas com os pesos respctivios e somamos
    ValoresAtivacaoCamadaOculta = sigmoid(SomaSinapse0) ## Utilizando a função sigmoid calculo os valores de ativação dos meu neuronios
    SomaSinapse1 = np.dot(ValoresAtivacaoCamadaOculta, pesosCamada1)
    CamadaSaida = sigmoid(SomaSinapse1)
    #Calculo do erro (erro = RespostaCorreta - RespostaCalculada)
    erroCamadaSaida = saidas - CamadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida)) # Media absoluta do erro em modulo
    print("Erro: " + str(mediaAbsoluta))

    derivadaSaida = sigmoidDerivada(CamadaSaida) 
    deltaSaida = erroCamadaSaida * derivadaSaida ## delta  = erro * derividasigmoid
    # O delta juntamente ao erro será utilizando o ajuste dos pesos, indicando se tevo aumenta-los o diminui-los
    pesosCamada1Transposta = pesosCamada1.T
    # Precisamos realizar a matriz transposta do pesos da camada 2, pois não conseguimos multiplicar a matriz deltaSaida(4x1) por uma 3x1
    deltaCamadaOculta = sigmoidDerivada(ValoresAtivacaoCamadaOculta) * (deltaSaida.dot(pesosCamada1Transposta))
    # Algoritmo de backpropagation
    CamadaOcultaTransposta = ValoresAtivacaoCamadaOculta.T
    pesosNovo1 = CamadaOcultaTransposta.dot(deltaSaida)
    pesosCamada1 = (pesosCamada1 * momento) + (pesosNovo1 * taxaAprendizagem)
     
    camadaEntradaTransposta = CamadaEntrada.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesosCamada0 = (pesosCamada0 * momento) + (pesosNovo0 * taxaAprendizagem)
print('A saida calculada foi: \n {},\nErro medio foi de: {}'.format(CamadaSaida, abs(mediaAbsoluta)))