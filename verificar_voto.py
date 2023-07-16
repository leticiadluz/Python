#Crie um programa que tenha uma função chamada voto que vai receber como parâmetros o ano do nascimento
#de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGAGO, OPCIONAL OU OBRIGATÓRIO
#<18 anos e >70anos =opcional,entre 18 e 69 anos é obrigatório.

from datetime import date
ano_atual = date.today().year

def voto(nascimento):
    idade = ano_atual - nascimento
    print(idade,"anos")
    if idade < 16:
        print("Não pode votar")
    elif idade >= 16 and idade < 18 or idade >= 70:
        print("Voto opcional")
    else:
        print("Voto obrigatório")
        
nascimento=int(input("Qual seu ano de nascimento?"))
voto(nascimento)
