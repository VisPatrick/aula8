dicionario = {}

print(dicionario)

aluno = {'Nome': 'Maria',
         'Idade': 29,
         'Curso': 'Analise de dados'}

print(aluno)
print(aluno['Idade'])

aluno['Nome'] = 'Pedro'
print(aluno)
aluno['E-mail'] = 'pedro@gmail.com'
print(aluno)

if 'tel' in aluno:
    aluno.pop('E-mail')
print(aluno)

aluno.clear()  limpa a chave 
print(aluno)

del aluno  apaga tudo 
print(aluno)

for chave, valor in aluno.items():
    print(chave, valor)