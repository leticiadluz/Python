#Criar uma calculadora que exiba mensagem de erro ao verificar que usuário forneceu uma entrada inválida, 
#ou tentou realizar divisão por 0.

def obter_numero():
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

valor1 = obter_numero()
valor2 = obter_numero()

operador = str(input( "Digite um operador: "))

if operador == "-": 
    print( "Resultado:", valor1 - valor2)
elif operador == "*":
    print( "Resultado:", valor1 * valor2)
elif operador == "+":
    print( "Resultado:", valor1 + valor2)
elif operador == "/":
    try:
        print( "Resultado:", valor1 / valor2) 
    except ZeroDivisionError:
        print ("Operação Inválida, não é possível realizar divisão por 0")
else:
    print ("Operador inválido!")
