#Faça um código para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

vetor = []
for x in range (30):
    num = float(input(f"Digite o {x+1}º número: "))
    vetor.append(num)

num1 = float(input("Digite um número que você deseja encontrar no vetor: "))
cont = 0
for elemento in vetor:
    if elemento == num1:
        cont+= 1
print(f"O número {num1} aparece {cont} vezes no vetor.")