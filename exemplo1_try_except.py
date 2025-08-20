'''
Tratamento de exceções em Python
try-except

Sintaxe:
try:
    #código que pode gerar uma execeção
except Tipo_de_exceção
    #código para lidar com exceção
    
else: <opcional>

finally: <opcional>

'''

#Exemplo (sem tratamento de erro)
teste = 1
while teste !=0:
    try:
        num = int(input('Número: '))
        print(f'Você digitou o número {num}')
    except ValueError:
        print('Entrada inválida! Por favor, digite um número')
    teste = int(input('Digite 0 pra encerrar! '))