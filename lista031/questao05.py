'''
Fazer um programa que pergunte o salário de um funcionário e apresente este salário com um aumento de 15%.
'''

a = float(input("Insira o valor de seu salário: "))

aumento = 0.15

final = a + (a * aumento)

print("Seu salário final com aumento de 15% será de: R$", final)
