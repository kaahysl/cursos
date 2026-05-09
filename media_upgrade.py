listaNotas = [] #criamos uma

print("-" * 100)
print("Bem vindos a I.A que calcula notas e médias final 🤖✨")
print("-" * 100)

while True:
    notas = (input("Digite a nota que deseja inserir (digite sair para parar): "))

    if notas.lower() == "sair": #comando lower obriga se a entrada em minusculo
        break
    else:
        listaNotas.append(float (notas))

        media = sum(listaNotas) / len(listaNotas)
    
print(f"A media final do aluno é {media:.2f}")

if media >= 6:
     print("Parabéns! Você está aprovado!")
else:
    print("Você está reprovado! estude mais bimestre que vem")
