#Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela. Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha.
vetor = []

for x in range(5):
    nome = input(f"Digite o {x+1}º nome: ")
    vetor.append(nome)
print(f"Os nomes digitados foram")
for nome in vetor:
    print(nome)

print("Nomes em ordem decrescente")
for x in range (4,-1,-1):
    print(vetor[x])