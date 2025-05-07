

def cadastra_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor: ')
        valor = input('Informe valor da venda: ')

        pessoas = {
            'Nome': nome,
            'Valor': valor,
        }

        list_cadastro.append(pessoas)


list_cadastro = []

# programa principal
qnt = int(input('Quantas pessoas: '))
cadastra_pessoa(qnt)
print(list_cadastro)