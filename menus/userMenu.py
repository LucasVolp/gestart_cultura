from flows.utils import Utils, MenuBackException
from models.event import Event
from menus.ticketMenu import ticketMenu
from menus.purchaseMenu import purchaseMenu
from menus.ratingMenu import ratingMenu
from flows.manageAccounts import manageAccounts
from flows.notifications import notifications


def userMenu(user):
    while True:
        try:
            Utils.menu(f"Bem vindo(a) ao menu do Usuário, {user.name} - Saldo atual: {user.balance}")
            print("\nEscolha uma opção:")
            print("1. Ver eventos")
            print("2. Gerenciar Ingressos")
            print("3. Gerenciar Compras")
            print("4. Gerenciar Avaliações")
            print("5. Gerenciar Conta")
            print("6. Gerenciar Notificações")
            print("0. Sair")
            option = input()
            match option:
                case "1":
                    try:
                        for idx, event in enumerate(Event.events, start=1):
                            print(f"{idx} - {event.name} - {event.description} - {event.date} - {event.local} - {event.size} - {event.typeEvent.name} - {event.status.name}")
                        Utils.pause()
                    except MenuBackException:
                        break
                    except Exception as e:
                        print(f"Erro ao listar eventos: {e}")
                        Utils.pause()
                case "2":
                    try:
                        ticketMenu(user)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar ingressos: {e}")
                        Utils.pause()
                case "3":
                    try:
                        purchaseMenu(user)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar compras: {e}")
                        Utils.pause()
                case "4":
                    try:
                        ratingMenu(user)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar avaliações: {e}")
                        Utils.pause()
                case "5":
                    try:
                        manageAccounts(user)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar conta: {e}")
                        Utils.pause()
                case "6":
                    try:
                        notifications(user)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar notificações: {e}")
                        Utils.pause()
                case "0":
                    print("Saindo do menu do usuário...")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    Utils.pause()
        except MenuBackException:
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            Utils.pause()