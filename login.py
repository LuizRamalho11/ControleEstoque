import customtkinter as ctk
import os
import json

arquivo_usuarios = 'usuarios.json'

def carregar_usuarios():
    if os.path.exists(arquivo_usuarios):    # Verifica se o arquivo existe
        with open(arquivo_usuarios, 'r') as a:  # Se existir, abre o arquivo no modo de leitura
            return json.load(a)
    return []


def salvar_usuarios(user):
    with open(arquivo_usuarios, 'w') as a:  # abre o arquivo no modo de escrita, substituindo o conteúdo antigo
        json.dump(user, a, indent=4)  # salva a lista 'usuarios' no arquivo '.json'
    

def autenticar_usuarios(user, password):
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u['usuario'] == user and u['senha'] == password:
            return True
    return False


def cadastrar_usuarios(user, password):
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u['usuario'] == user:
            return False    # usuário já existe
    usuarios.append({'usuario': user, 'senha': password})
    salvar_usuarios(usuarios)
    return True