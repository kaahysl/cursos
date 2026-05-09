print("-" * 50)
print("Bem vindo ao coletor de dados do Chat GPT 🤖")
print("-" * 50)

#
nome = input("Digite o seu nome: ") #Input recebe dados do teclado do usuário
email = input("Digite o seu email: ") #criei uma variavel email que irá armezenar o email de usuário
cidade = input ("Digite a sua cidade: ")
estado =input ("Digite o seu estado: ")
país= input("Digite o seu país: ")
qualseuAno= int(input("Digite seu ano: "))
idadeAtual= 2026 - qualseuAno
 
print(f"Olá {nome}, seus dados são {email}, sua cidade é {cidade}, seu estado é {estado}, seu país é {país}, sua idade atual {idadeAtual} está correto?") #o f minusculo antes das aspas, permite que eu trabalhe com variáveis na frase. As chaves {} servem pareou chamar variavel dentro da frase

