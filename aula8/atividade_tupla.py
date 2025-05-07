# pratica 01
estados = ('Mato Grosso', 'Minas Gerais', 'Rio de Janeiro', 'Parana', 'São Paulo')
print(estados)

# pratica 02
dados = ('João', 'Analista', 4000.00, 'Pedro', 'Vendedor', 2500.00)

print(dados[0:2])
print(dados[3:-1])

# pratica 03

dicionario = {'nome': 'Notbook',
              'preco': 3500.00,
              'estoque': 15}
print(dicionario)

dicionario.pop('estoque')   # pop apaga a chave
print(dicionario)

dicionario['preco'] = 4000.00
print(dicionario)

print(f"nome: {dicionario['nome']} R$: {dicionario['preco']:.2f}")
