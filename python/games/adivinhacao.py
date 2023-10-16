import random
def jogar():
    print("********************************")
    print("Bem vindo ao jogo da adivinhação")
    print("********************************")

    # Declaração
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    print(numero_secreto)

    print("Qual nivel de dificultade gostari?")
    print("(1) - Facil (2) - Medio (3) - Dificil")
    nivel = int(input("Defina o nivel: "))

    if(nivel == 1): 
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Logica para acertar um numero em N tentativas, com dicas
    for tentativa in range(1, total_de_tentativas + 1):   
        print("Tentativa {} de {}".format(tentativa, total_de_tentativas)) # .format(variavel1, variavel2) = interpolação

        # Ler a entrada do usuario
        chute = float(input("Digite o numero que deseja chutar, entre 1 e 100: "))
        print("Voce digitou:", chute)

        #validar entrada
        if(chute < 1 or chute > 100):
            print("Digite um numero entre 1 e 100")
            continue # reiniciar Loop, ignorando a logica abaixo

        # Verificar numero de chute
        if(numero_secreto == chute):
            print("Voce acertou!")
            break
        else:
            if(numero_secreto > chute):
                print("o seu chute foi menor que o numero secreto")
            elif(numero_secreto < chute):
                print("seu chute foi maior que o numero secreto")

if(__name__ == "__main__"):
    jogar()