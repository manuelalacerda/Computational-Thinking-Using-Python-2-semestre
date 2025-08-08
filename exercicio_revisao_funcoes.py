'''
Escreva um programa em Python que simule o calculo de notas de um aluno em diferentes disciplinas. 
O programa deve modular e utilizar estruturas de controle e funções.

1. Requisitos de sistema
- Função calcular_media(notas)
    - deve receber uma LISTA de notas com parâmetro
    - deve ter uma estrutura de repetição (for ou while) para percorrer a lista de notas
    - deve retornar a média das notas

- Função verificar_aprovacao(media, media_minima)
    - deve receber a média do aluno e a média minima para aprovação
    - deve usar condicionais para verificar o status do aluno
    - se a médoa for maior ou igual a média minima retornar a String "Aprovado"
    - se a média for maior ou igual a 5.0 e menor que a média minima , retornar a String "recuperação"
    - caso contrário , deve retornar a String "Reprovado"

- Função principal main()
    - lista de disciplinas 
    - média minima de aprovação (constante)
    - estrutura de repetição para inter a lista de disciplinas
    - para cada disciplina, o usuário deverá inserir 3 notas
    - chamar a função calcular_media para obter a média de cada disciplina
    - chamar a função verificar_aprovação para obter o status do aluno
    - imprimir a média e o status para cada disciplina
'''

def calcular_media(notas):
    '''
    Calcular a média de uma lista de notas 
        - recebe como parâmetro uma lista de notas
        - retorna a média das notas
    '''

    soma = 0

    #Percorrer a lista de notas
    for nota in notas:
        soma += nota #acumulando o somatório das notas em soma
        
    #validar a divisão por ZERO
    if len(notas) > 0:
        return soma/len(notas)
    else:
        return 0
    
    return soma/len(notas)

def verificar_aprovacao(media, media_minima):
    '''
    Verifica o status de aprovação do aluno
        - recebe a média e a média  mínima por parâmetro
        - retorna o status  - "Aprovação",  "Recuperação" ou "Reprovado"
    '''
    if media >= media_minima:
        return "Aprovado"
    elif media >= 5 and media < media_minima:
        return "Recuperação"
    else:
        return "Reprovado"
    
def main():
    '''
    Função principal do programa 
        - lista com as disciplinas
        - média mínima para aprovação
        - deve testar as funções calcular_media() e verificar_aprovacao()
    '''

    disciplinas = ["Python," "Java", "Front-End"]
    media_aprovacao = 7.0

    print('*--\n Sistema de Cálculo de notas --*\n')

    #percorrer a lista de disciplinas 
    for disciplina in disciplinas:
        print(f'Disciplina: {disciplina}')

        #lista de notas da disciplina
        notas = []

        for i in range(3):
            nota  = float(input(f'Digite a nota {i+1}: '))
            notas.append(nota)

        media_final = calcular_media(notas)
        status = verificar_aprovacao(media_final, media_aprovacao)

        #imprimir os resultados
        print(f'Média em {disciplina}: {media_final:.2f} ')
        print(f'Status: {status}')


#Programa Principal 
main()