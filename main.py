import json
import getpass
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'users.json')

def load_users():
	if not os.path.exists(DB_PATH):
		return {}
	with open(DB_PATH, 'r', encoding='utf-8') as f:
		try:
			return json.load(f)
		except json.JSONDecodeError:
			return {}

def save_users(users):
	with open(DB_PATH, 'w', encoding='utf-8') as f:
		json.dump(users, f, ensure_ascii=False, indent=2)

def register():
	users = load_users()
	print('Cadastro de usuário')
	username = input('Usuário: ').strip()
	if not username:
		print('Nome de usuário inválido.')
		return
	if username in users:
		print('Usuário já existe.')
		return
	pwd = getpass.getpass('Senha: ')
	pwd2 = getpass.getpass('Confirmar senha: ')
	if pwd != pwd2:
		print('Senhas não conferem.')
		return
	if not pwd:
		print('Senha inválida.')
		return
	# Nota: em produção, armazene hashes, não senhas em texto simples.
	users[username] = {'password': pwd}
	save_users(users)
	print('Cadastro realizado com sucesso.')

if __name__ == '__main__':
	try:
		register()
	except KeyboardInterrupt:
		print('\nOperação cancelada.')
