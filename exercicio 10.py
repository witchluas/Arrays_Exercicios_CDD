#Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.

N = int(input("Digite o tamanho dos vetores (N): "))
A = []
B = []
Soma = []
print("Digite os elementos do vetor A:")
for i in range(N):
    elementoA = float(input(f"Digite o {i+1}º elemento: "))
    A.append(elementoA)
print("Digite os elementos do vetor B:")
for i in range(N):
    elementoB = float(input(f"Digite o {i+1}º elemento: "))
    B.append(elementoB)
for i in range(N):
    resultado = A[i] + B[i]
    Soma.append(resultado)
print("Vetor Soma:")
for elemento in Soma:
    print(elemento)
