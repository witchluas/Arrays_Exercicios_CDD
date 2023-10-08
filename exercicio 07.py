#Faça um código para ler 5 números e armazenar em num vetor. após a leitura total dos 5 números, o código deve escrever esses 5 números lidos na ordem inversa.
A = []
for x in range(5):
    num = int(input(f"Informe o {x+1}º número: "))
    A.append(num)
for x in range(4, -1, -1):
    print(A[x], end= " ")