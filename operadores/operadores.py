a = 3
b = -4

# Operadores Aritméticos

soma = a + b
sub = a - b
mult = a * b
div = a / b
div_inteiros = a // b

print(f"Soma: { soma }")
print(f"Subtração: { sub }")
print(f"Multiplicação: { mult }")
print(f"Divisão: { div }")
print(f"Divisão de inteiros: { div_inteiros }")
print(f"Cálculos dentro do print: { a * b }")
print(f"Resto da divisão de 16 por a: { 16 % a }")

# Operadores Relacionais

print(f"a == b: { a == b }") # =: recebe ; ==: comparação de igualdade
print(f"a < 5: { a < 5 }") # menor <
print(f"a > b: { a > b }") # maior: >
print(f"a <= 3: { a <= 3 }") # menor ou igual: <=
print(f"a >= 4: { a >= 4 }") # maior ou igual: >=
print(f"a != b: { a != b }") # diferente: !=

c = a != b
print(f"c: {c}")
print(f"tipo da var c: {type(c)}") # type é o tipo que a variável que tá recebendo e bool é o tipo booleano ou lógico

# Operadores Lógicos

logic1 = True
logic2 = False
print(f"type(logic1): {type(logic1)}")
print(f"type(logic2): {type(logic2)}")

print(f"logic1: {logic1}")
print(f"not logic1: {not logic1}")
print(f"logic1 or logic2: {logic1 or logic2}")
print(f"logic1 and logic2: {logic1 and logic2}")

