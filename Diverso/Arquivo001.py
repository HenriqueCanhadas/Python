import secrets

token = secrets.token_hex(8)  # Gera um token hexadecimal com 16 bytes (32 caracteres)
print(token)


import uuid

token = str(uuid.uuid4())  # Gera um token UUID aleatório
print(token)

# Suponha que você tenha uma lista chamada 'lista_origem'
lista_origem = ['item1', 'item2', 'item3']

# Crie uma nova lista chamada 'nova_lista' e adicione o valor de 'item2' a ela
nova_lista = []
valor_a_copiar = lista_origem[1]  # índice 1 corresponde a 'item2'
nova_lista.append(valor_a_copiar)

print(lista_origem)
print(valor_a_copiar)
print(nova_lista)