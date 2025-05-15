from uuid import uuid4
from enums.status import Status
from flows.utils import Utils
from models.producer import Producer
from eventMenu import producerEventMenu
from tierMenu import producerTierMenu

def menuProducer(producer):
    while True:
        Utils.menu(f"Bem vindo(a) ao menu do Produtor, {producer.name}")
        print("\nEscolha uma opção:")
        print("1. Gerênciar Eventos")
        print("2. Gerênciar Lotes")
        print("3. Gerênciar Conta")
        print("0. Sair")
        option = input()
        match option:
            case "1":
                try:
                    producerEventMenu(producer)
                except KeyboardInterrupt:
                    continue
            case "2":
                try:
                    producerTierMenu(producer)
                except KeyboardInterrupt:
                    continue
            case "3":
                pass
            case "0":
                print("Saindo do menu do Produtor. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                Utils.pause()

producer = Producer(id=uuid4(), name="Produtor Teste", cpf="12345678900", birth="01/01/2000", email="teste@teste.com", password="senha123", phone="(11) 91234-5678", cnpj="12.345.678/0001-90", enterprise="Empresa Teste", status=Status.ACTIVE)

if __name__ == "__main__":
    menuProducer(producer)
