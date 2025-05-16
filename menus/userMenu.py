from flows.utils import Utils
from models.event import Event


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
        match option:
            case "1":
                for idx, event in enumerate(Event.events, start=1):
                    print(f"{idx} - {event.name} - {event.description} - {event.date} - {event.local} - {event.size} - {event.typeEvent.name} - {event.status.name}")
                Utils.pause()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "0":
                print("Saindo do menu do usuário...")
                break
            case _:
                print("Opção inválida. Tente novamente.")