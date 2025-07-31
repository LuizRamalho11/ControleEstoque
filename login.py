import customtkinter as ctk
import os
import json

# caminho do arquivo onde os usuários serão salvos
arquivo_usuarios = 'usuarios.json'

# === função para carregar os usuários salvos ===
def carregar_usuarios():
    if os.path.exists(arquivo_usuarios):    # verifica se o arquivo existe
        with open(arquivo_usuarios, 'r') as a:  # abre o arquivo no modo de leitura
            try:
                return json.load(a) # tenta carregar o arquivo como JSON
            except json.JSONDecodeError:
                return[]    # se o arquivo estiver vazio ou corrompido, retorna uma lista vazia
    return []   # se o arquivo não existir, também retorna uma lista vazia

# === função para salvar usuários ===
def salvar_usuarios(user):
    with open(arquivo_usuarios, 'w') as a:  # abre o arquivo no modo de escrita, substituindo o conteúdo antigo
        json.dump(user, a, indent=4)  # salva os dados (lista de usuários) no formato JSON
    
# === função para autenticar (fazer login) === 
def autenticar_usuarios(user, password):
    usuarios = carregar_usuarios()  # carrega todos os usuários
    for u in usuarios:  # percorre cada usuário na lista
        if u['usuario'] == user and u['senha'] == password: # verifica o usuário e senha
            return True
    return False    # se não encontrar nenhum usuário válido, retorna Falso

# === função para cadastrar novo usuário ===
def cadastrar_usuarios(user, password):
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u['usuario'] == user:    # se o nome de usuário já existir, retorna falso
            return False
    usuarios.append({'usuario': user, 'senha': password})   # adciona novo usuário na lista
    salvar_usuarios(usuarios)   # salva a lista atualizada no arquivo
    return True # retorna True para indicar sucesso no cadastro

# === função de ação do botão "login" ===
def login():
    usuario = entrada_usuario.get() # obtém o texto digitado no campo de usuário
    senha = entrada_senha.get() # Obtém o texto digitado no campo de senha
    if autenticar_usuarios(usuario, senha) == True: # chama a função de autenticação
        resultado_label.configure(text='Login realizado com sucesso!', text_color='green')
    else:
        resultado_label.configure(text='ERRO: Usuário ou senha inválidos!', text_color='red')

# === função de ação do botão "cadastrar" ===
def cadastrar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if cadastrar_usuarios(usuario, senha) == True: # chama a função de cadastro
        resultado_label.configure(text='Cadastro realizado com sucesso!', text_color='green')
    else:
          resultado_label.configure(text='Usuário já existe!', text_color='red')

# === interfáce ===
# configurações da janela
janela = ctk.CTk()
janela.title('Login - Sistema de estoque')
janela.geometry('280x290')

# campo de entrada do usuário
usuario = ctk.CTkLabel(janela, text='Usuário:')
entrada_usuario = ctk.CTkEntry(janela, placeholder_text='Digite o seu usuário')

# campo de entrada da senha do usuário
senha = ctk.CTkLabel(janela, text='Senha:')
entrada_senha = ctk.CTkEntry(janela, placeholder_text='Digite a sua senha', show='●')

# botões de ação de login e cadastro
login_button = ctk.CTkButton(janela, text='Login', command=login)
cadastrar_button = ctk.CTkButton(janela, text='Cadastrar', command=cadastrar)

# label com a mensagem de sucesso ou erro
resultado_label = ctk.CTkLabel(janela, text='', text_color='white')

# adicionando os controles na janela
usuario.pack(pady=10)
entrada_usuario.pack(pady=5)

senha.pack(pady=10)
entrada_senha.pack(pady=5)

login_button.pack(pady=15)
cadastrar_button.pack()

resultado_label.pack(pady=5)

# mantém a janela aberta
janela.mainloop()