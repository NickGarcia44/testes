import sys
from cadastro import register
from login import login

def menu_principal():
    """Exibe o menu interativo e gerencia as escolhas do usuário."""
    while True:
        print("\n" + "=" * 30)
        print("    SISTEMA DE AUTENTICAÇÃO   ")
        print("=" * 30)
        print("[1] - Criar nova conta (Cadastrar)")
        print("[2] - Fazer Login")
        print("[3] - Sair")
        print("=" * 30)
        
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == '1':
            print("\n--- NOVO CADASTRO ---")
            register()
        elif opcao == '2':
            print("\n--- AUTENTICAÇÃO ---")
            login()
        elif opcao == '3':
            print("\nSaindo do sistema... Até logo!")
            sys.exit(0)
        else:
            print("\nOpção inválida! Digite 1, 2 ou 3.")

if __name__ == '__main__':
    try:
        menu_principal()
    except KeyboardInterrupt:
        print('\n\nOperação interrompida pelo usuário. Encerrando...')