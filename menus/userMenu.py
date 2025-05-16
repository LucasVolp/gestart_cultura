from flows.utils import Utils


def userMenu(user):
    while True:
        Utils.menu(f"Bem vindo(a) ao menu do Usuário, {user.name}")
        print("\nEscolha uma opção:")
        print("1. Ver eventos")
        print("2. Gerênciar Ingressos")
        print("3. Gerênciar Compras")
        print("4. Gerênciar Avaliações")
        print("5. Gerênciar Conta")
        print("6. Gerênciar Notificações")
        print("0. Sair")
        option = input()
        
