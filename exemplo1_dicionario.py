'''
Dicionários 

cria um dicionário com informações sobre uma pessoa

construtor: dict()

Sintaxe:
nome = {"chave" : valor}
'''

pessoa = {
    'nome':'João',
    'idade': 30,
    'cidade':'São Paulo'
}

#Imprimindo o dicionário pessoa
print(pessoa)

#Acessando um elemento através da chave
print(f'Nome: {pessoa['nome']}')

#Adicionando um novo elemento ao dicionário
pessoa['profissão'] = 'Desenvolvedor'
print(pessoa)

#Alterando o valor de uma chave
pessoa['idade'] = 40
print(f'Nova idade: {pessoa['idade']}')

print(pessoa)

#Removendo um elemento do dicionário
del pessoa['cidade']
print(pessoa)