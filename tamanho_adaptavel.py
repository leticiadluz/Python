#Faça um programa que tenha uma função chamada escreva que receba um texto qualquer como parâmetro e mostre uma mensagem com 
#tamanho adaptável

def escreva (mensagem):
    tamanho = len(mensagem)
    print("~" * tamanho)
    print(mensagem)
    print("~" * tamanho)
