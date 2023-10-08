#Ler um vetor A de 10 NÚMEROS. Logo em seguida, ler mais um úemro e guardar em uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.

A = []
for x in range(10):
    num = float(input(f"Informe o {x+1}º número: "))
    A.append(num)

n1 = float(input("Informe um número para multiplicar os valores em A: "))

n2 = [num * n1 for num in A]
print("VETOR N2:'")

for resultado in n2:
    print(resultado)