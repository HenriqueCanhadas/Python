import secrets

token = secrets.token_hex(8)  # Gera um token hexadecimal com 16 bytes (32 caracteres)
print(token)


import uuid

token = str(uuid.uuid4())  # Gera um token UUID aleatório
print(token)