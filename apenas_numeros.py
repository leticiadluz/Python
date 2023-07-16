#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do Python,
#só que fazendo a validação para aceitar apenas um valor numérico.
def leia():
    while True:
        n = input("Digite um número: ")
        if n.isdigit():
            return n
        else:
            print("ERRO! Digite um número válido.")
#Retorno da função leia será atribuído a variável numero
numero = leia()
print("Você acabou de digitar o número:", numero)

#O método isdigit() é utilizado para verificar se uma string contém apenas números
