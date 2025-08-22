'''
Principais métodos (mais comuns)
- keys(): retorna uma "visão" de todas as chaves do dicionário
- values(): retorna uma "visão" de todos os valores do dicionário
- items(): retorna uma "visão" dos pares de chave-valor do dicionário
- get(): acessa um valor de forma segura (retornado um valor padrão quando não encontrar o elemento)
'''

carro = {
    "marca": "Jeep",
    "modelo": "Compass",
    "ano": 2025
}

#Iterando sobre as chaves do dicionário - método keys()
for chave in carro.keys():
    print(chave)

#Iterando sobre os valores do dicionário - método values()
for valor in carro.values():
    print(valor)

#Iterando sobre a chave e valor do dicionário - método items()
for chave, valor in carro.items():
    print(f'{chave} : {valor}')

#Acesso a uma chave inexistente
#print(carro['motor']) 

#Acesso a uma chave com o método get()
motor = carro.get('motor', 'não especificado!')
print(f'motor: {motor}')

print(f'marca: {carro.get('marca')}')