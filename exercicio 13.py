#Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor. A seguir, o algoritmo deverá informar (1) todos os números pares que existem no vetor; (2) o menor e o maior valor existente no vetor; (3) quantos dos valores do vetor são maiores que a média desses valores:

vetor = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor inteiro: "))
    vetor.append(valor)
pares = [num for num in vetor if num % 2 == 0]
print("Números pares no vetor:", pares)
menorvalor = min(vetor)
maiorvalor = max(vetor)
print("Menor valor:", menorvalor)
print("Maior valor:", maiorvalor)

media = sum(vetor) / len(vetor)
valoresmaiores = [num for num in vetor if num > media]
print(f"Quantidade de valores maiores que a média:",(valoresmaiores))
