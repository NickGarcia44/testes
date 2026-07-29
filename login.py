import json
import getpass
import os

# Aponta para o mesmo arquivo users.json na mesma pasta
DB_PATH = os.path.join(os.path.dirname(__file__), 'users.json')

def load_users():
    """Lê o arquivo de usuários salvos."""
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def login():
    """Solicita credenciais e valida a autenticação."""
    users = load_users()
    
    if not users:
        print('Nenhum usuário cadastrado no sistema ainda.')
        return

    print('--- Autenticação de Usuário ---')
    username = input('Usuário: ').strip()
    pwd = getpass.getpass('Senha: ')

    # 1. Verifica se o usuário existe nas chaves do dicionário
    if username not in users:
        print('Usuário ou senha incorretos.')
        return

    # 2. Verifica se a senha informada coincide com a armazenada
    if users[username]['password'] == pwd:
        print(f'\nLogin realizado com sucesso! Bem-vindo(a), {username}.')
        # Aqui entra a lógica pós-login (ex: abrir o menu principal)
    else:
        print('Usuário ou senha incorretos.')

if __name__ == '__main__':
    try:
        login()
    except KeyboardInterrupt:
        print('\nOperação cancelada.')
