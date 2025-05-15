from uuid import uuid4
from enums.status import Status
from flows.utils import Utils
from models.producer import Producer

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
                    Utils.menu("Gerênciar Eventos - ou digite 0 para voltar")
                    print("Escolha uma opção:")
                    print("1. Criar Evento")
                    print("2. Editar Evento")
                    print("3. Excluir Evento")
                    print("4. Listar Eventos")
                    eventOption = Utils.inputBack("Escolha uma opção: ")
                    if eventOption == "1":
                        Utils.menu("Criação de Evento - ou digite 0 para voltar")
                        name = Utils.inputBack("Digite o nome do evento: ")
                        description = Utils.inputBack("Digite a descrição do evento: ")
                        date = Utils.inputBack("Digite a data do evento (DD/MM/AAAA): ")
                        local = Utils.inputBack("Digite o local do evento: ")
                        size = int(Utils.inputBack("Digite o tamanho do evento: "))
                        typeEvent = Utils.typeEvents()
                        event = producer.createEvent(name=name, description=description, date=date, local=local, size=size, typeEvent=typeEvent, status=Status.OPEN)
                        if event:
                            print(f"Evento criado com sucesso! - Evento: {event}")
                        else:
                            print("Erro ao criar evento.")
                    elif eventOption == "2":
                        pass
                    elif eventOption == "3":
                        pass
                    elif eventOption == "4":
                        producer.listEvents()
                        Utils.pause()
                except KeyboardInterrupt:
                    continue
            case "2":
                pass
            case "3":
                pass
            case "0":
                pass
            case _:
                print("Opção inválida. Tente novamente.")
                Utils.pause()

producer = Producer(id=uuid4(), name="Produtor Teste", cpf="12345678900", birth="01/01/2000", email="teste@teste.com", password="senha123", phone="(11) 91234-5678", cnpj="12.345.678/0001-90", enterprise="Empresa Teste", status=Status.ACTIVE)

if __name__ == "__main__":
    menuProducer(producer)
