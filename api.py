#Primeiro: Instalar bibliotecas
#pip install requests

#Segundo passo: adicionar/importar ao código
import requests
nome = input("Digite o seu nome: ")
email = input ("Digite seu email: ")
telefone = input ("Digite seu telefone: ")
#Recebe o cep digitado pelo o ususario
cep = input ("Digite seu cep: ")
#Criar uma variável e atribuir o resultado do link
url = f"https://viacep.com.br/ws/{cep}/json/"


dados = requests.get(url).json()

print(f"Bem vindo ao Mecado Livre {nome}! O seu email é {email}. O seu telefone é {telefone}. Você mora na rua {dados['logradouro']}, na cidade {dados['localidade']}, seu estado é {dados['bairro']}.")

#Atribuir variávis oara cada um dos resultados
# rua = dados['logradouro']
# bairro= dados ['bairro']
# cidade = dados ['localidade']



