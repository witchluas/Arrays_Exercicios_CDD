#Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente, após completar a digitação, imprimir: nome, senha e posição dos dados no array.
name = []
password = []
for x in range(5):
    nome = input(f"{x+1}º Informe seu nome : ")
    senha = input(f"{x+1}º Informe sua senha: ")
    name.append(nome)
    password.append(senha)
for y in range(5):
    print(f"Posição {y+ 1}º:")
    print(f"Nome: {name[y]}")
    print(f"Senha: {password[y]}")