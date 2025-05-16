from flows.utils import Utils
from manageAccounts import manageAccounts
from menus.notifications import notifications


def sellerMenu(seller):
    while True:
        Utils.menu(f"Bem vindo(a) ao menu do Vendedor, {seller.name}")
        print("\nEscolha uma opção:")
        print("1. Ver vendas")
        print("2. Gerênciar Conta")
        print("3. Gerênciar Notificações")
        print("0. Sair")
        option = input()
        match option:
            case "1":
                try:
                    if seller.purchases:
                        print("Suas vendas:")
                        for purchase in seller.purchases:
                            print(f"ID: {purchase.id}, Evento: {purchase.event.name}, Data: {purchase.date}")
                    else:
                        print("Você não tem vendas.")
                except KeyboardInterrupt:
                    continue
            case "2":
                try:
                    manageAccounts(seller)
                except KeyboardInterrupt:
                    continue
            case "3":
                try:
                    notifications(seller)
                except KeyboardInterrupt:
                    continue
            case "0":
                print("Saindo do menu do Vendedor. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                Utils.pause()