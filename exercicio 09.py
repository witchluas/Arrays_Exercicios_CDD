#Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e mostrando seu nome e a mensagem, login efetuado com sucesso.
#Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente, após completar a digitação, imprimir: nome, senha e posição dos dados no array.
name = []
password = []
for x in range(5):
    nome = input(f"{x+1}º\nInforme seu nome : ")
    senha = input(f"Informe sua senha: ")
    name.append(nome)
    password.append(senha)
for y in range(5):
    print(f"Posição {y+ 1}º:")
    print(f"Nome: {name[y]}")
    print(f"Senha: {password[y]}")
    print("Login efetuado com sucesso! ")