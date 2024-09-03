import streamlit as st
import hashlib

# Função para criar o hash da senha
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Defina o hash da senha que será usada
PASSWORD_HASH = "f46735b4ce0cf00b71921b0add415a53989038409ff12ff991e56241683d6a2a"

# Função para verificar o login
def login(username, password):
    if username == "usuario" and hash_password(password) == PASSWORD_HASH:
        return True
    else:
        return False

# Título do aplicativo
st.title("Tela de Login")

# Inputs de nome de usuário e senha
username = st.text_input("Nome de usuário")
password = st.text_input("Senha", type="password")

# Botão de login
if st.button("Login"):
    if login(username, password):
        st.success(f"Bem-vindo, {username}!")
    else:
        st.error("Nome de usuário ou senha incorretos.")
