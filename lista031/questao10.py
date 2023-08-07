'''
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso,
utilizando a fórmula prestação = valor + (valor	x (taxa	: 100) x tempo	em	dias)

Perguntar ao usuário:

 - valor normal da prestação
 - taxa de juros
 - tempo em dias
'''

valor = float(input("Informe o valor normal de sua prestação: "))
taxa = float(input("Informe a taxa de juros? "))
tempo = float(input("Informe os dias de atraso? "))

prestacao	= valor + (valor * (taxa / 100) * tempo)

print("O valor da prestação em atrasos é R$", prestacao)
