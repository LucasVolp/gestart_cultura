from flows.utils import Utils, MenuBackException
from flows.manageAccounts import manageAccounts
from flows.notifications import notifications


def sellerMenu(seller):
    while True:
        try:
            Utils.menu(f"Bem vindo(a) ao menu do Vendedor, {seller.name} - Vendas até o momento: {len(seller.purchases) if hasattr(seller, 'purchases') else 0}")
            print("\nEscolha uma opção:")
            print("1. Ver vendas")
            print("2. Gerenciar Conta")
            print("3. Gerenciar Notificações")
            print("0. Sair")
            option = input()
            match option:
                case "1":
                    try:
                        purchases = getattr(seller, "purchases", [])
                        if purchases:
                            print("Suas vendas:")
                            for purchase in purchases:
                                print(f"ID: {purchase.id}, Evento: {purchase.event.name}, Data: {purchase.date}")
                        else:
                            print("Você não tem vendas.")
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao listar vendas: {e}")
                        Utils.pause()
                case "2":
                    try:
                        manageAccounts(seller)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar conta: {e}")
                        Utils.pause()
                case "3":
                    try:
                        notifications(seller)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar notificações: {e}")
                        Utils.pause()
                case "0":
                    print("Saindo do menu do Vendedor. Até logo!")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    Utils.pause()
        except MenuBackException:
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            Utils.pause()