''' 
1) Escreva uma função para criar uma matriz numérica n x m
                         
2) Escreva uma função que receba uma mtriz numérica por parâmetro
e retorne a soma de todos os elementos contidos na matriz, utilizando 
estrutura de repetição e variáveis

3) Escreva uma função para imprimir a soma (resultado)

4) Escreva uma função main() para testar o programa
'''

# 1) Escreva uma função para criar uma matriz numérica n x m

def criar_matriz(n_linhas, n_colunas): #função - nome - parâmetros que vou receber
    matriz = [] #Lista vazia
    for i in range(n_linhas):
        linha = [] #Lista Vazia 
        for j in range(n_colunas):
            n = int(input('Número: ')) #Usuario digitando um número
            linha.append(n) #Pega o que o usuario digito e coloca na primeira linha
        matriz.append(linha) #Monta a matriz em lista 
    return matriz #Retorna os valores da matriz

# 2) Escreva uma função que receba uma mtriz numérica por parâmetro
# e retorne a soma de todos os elementos contidos na matriz, utilizando 
# estrutura de repetição e variáveis

def somar_elementos(matriz): #(matriz é uma lista que contem outra lista)
    soma = 0 #Variável acumuladora
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            soma += matriz[linha][coluna]
    return soma

#3) Escreva uma função para imprimir a soma (resultado)

def imprimir(soma):
    print(f'Soma: {soma}')
    

# 4) Escreva uma função main() para testar o programa
# Função main() para testar o programa

def main():
    matriz = criar_matriz(3, 3)
    soma = somar_elementos(matriz)
    imprimir(soma) #Void
    
#Principal
main()
