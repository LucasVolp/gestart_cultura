from uuid import uuid4
from enums.status import Status
from flows.utils import Utils, MenuBackException
from flows.notifications import notifications
from models.producer import Producer
from .eventMenu import producerEventMenu
from .tierMenu import producerTierMenu
from flows.manageAccounts import manageAccounts

def menuProducer(producer):
    while True:
        try:
            Utils.menu(f"Bem vindo(a) ao menu do Produtor, {producer.name}")
            print("\nEscolha uma opção:")
            print("1. Gerenciar Eventos")
            print("2. Gerenciar Conta")
            print("3. Gerenciar Notificações")
            print("0. Sair")
            option = input()
            match option:
                case "1":
                    try:
                        producerEventMenu(producer)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar eventos: {e}")
                        Utils.pause()
                case "2":
                    try:
                        manageAccounts(producer)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar conta: {e}")
                        Utils.pause()
                case "3":
                    try:
                        notifications(producer)
                    except MenuBackException:
                        continue
                    except Exception as e:
                        print(f"Erro ao gerenciar notificações: {e}")
                        Utils.pause()
                case "0":
                    print("Saindo do menu do Produtor. Até logo!")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    Utils.pause()
        except MenuBackException:
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            Utils.pause()