import adivinhacao
import forca
print("*********************************")
print("********Escolha seu jogo!********")
print("*********************************")

print("(1) - Jogo da Forca")
print("(2) - Jogo da Adivinhação")
option = int(input("Digite sua escolha de jogo: "))

if(option == 1):
    print("Jogo da Forca")
    forca.jogar()
elif(option == 2):
    print("Jogo da Adivinhação")
    adivinhacao.jogar()

