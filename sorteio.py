#Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteio e soma par.
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
#mostrar a soma entre todos os valores pares sorteados pela função anterior. 

#Etapas:
#Definir uma função com quantidade de números sorteados, início e fim
#Criar uma lista vazia para ir armazenando os números sorteados
#Cada numero é adicionado a lista vazia pelo código: numeros_sorteados.append(numero_sorteado)

import random
def sortear(quan, i, f):
    numeros_sorteados = []
    for x in range(quan):
        numero_sorteado = random.randint(i, f)
        numeros_sorteados.append(numero_sorteado)
        print(numero_sorteado)
    return numeros_sorteados

def somar_pares(lista):
    soma = 0
    for a in lista:
        if a % 2 == 0: 
            soma += a
    return soma

#Entrada de valores
quantidade = int(input("Digite a quantidade de números a serem sorteados: "))
inicio = int(input("Digite o valor inicial para o sorteio: "))
fim = int(input("Digite o valor final para o sorteio: "))

#Chamando a função sortear e soma_pares para realizar as operações.
numeros_sorteados = sortear(quantidade, inicio, fim)
print("Números sorteados:", numeros_sorteados)

soma_pares = somar_pares(numeros_sorteados)
print("Soma dos valores pares:", soma_pares)
