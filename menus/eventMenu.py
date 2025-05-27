from enums.status import Status
from flows.utils import Utils
from .tierMenu import createTierMenu, editTierMenu, producerTierMenu

def createEventMenu(producer):
    try:
        Utils.menu("Criação de Evento - ou digite 0 para voltar")
        while True:
            name = Utils.inputBack("Digite o nome do evento: ")
            if not name.strip():
                print("Nome não pode ser vazio.")
                Utils.pause()
                continue
            break
        while True:
            description = Utils.inputBack("Digite a descrição do evento: ")
            if not description.strip():
                print("Descrição não pode ser vazia.")
                Utils.pause()
                continue
            break
        date = Utils.inputDate("Digite a data do evento (DD/MM/AAAA): ")
        while True:
            local = Utils.inputBack("Digite o local do evento: ")
            if not local.strip():
                print("Local não pode ser vazio.")
                Utils.pause()
                continue
            break
        while True:
            try:
                size = int(Utils.inputBack("Digite o tamanho do evento: "))
                if size <= 0:
                    print("Tamanho deve ser maior que zero.")
                    Utils.pause()
                    continue
                break
            except ValueError:
                print("Tamanho inválido.")
                Utils.pause()
        typeEvent = Utils.typeEvents()
        event = producer.createEvent(name=name, description=description, date=date, local=local, size=size, typeEvent=typeEvent, status=Status.OPEN)
        if event:
            print(f"Evento criado com sucesso! - Evento: {event}")
            Utils.pause()
            Utils.menu("Deseja criar um lote para este evento agora?")
            print("1. Sim")
            print("2. Não")
            while True:
                opcao = Utils.inputBack("Escolha uma opção: ")
                if opcao == "1":
                    createTierMenu(producer, event)
                    return
                elif opcao == "2":
                    print("Voltando ao menu de eventos.")
                    break
                else:
                    print("Opção inválida.")
                    Utils.pause()
        else:
            print("Erro ao criar evento.")
        Utils.pause()
    except Exception as e:
        print(f"Erro inesperado ao criar evento: {e}")
        Utils.pause()

def editEventMenu(producer):
    try:
        Utils.menu("Edição de Evento - ou digite 0 para voltar")
        if not producer.events:
            print("Nenhum evento encontrado.")
            Utils.pause()
            return
        print("Escolha um evento para editar:")
        for idx, event in enumerate(producer.events, start=1):
            print(f"{idx} - {event.name}")
        while True:
            try:
                eventIndex = int(Utils.inputBack("Escolha o número do evento: ")) - 1
                if eventIndex < 0 or eventIndex >= len(producer.events):
                    print("Evento inválido.")
                    Utils.pause()
                    continue
                event = producer.events[eventIndex]
                break
            except ValueError:
                print("Entrada inválida. Digite um número.")
                Utils.pause()
        Utils.menu("O que deseja editar?")
        print("1. Editar dados do evento")
        print("2. Editar lotes do evento")
        while True:
            opcao = Utils.inputBack("Escolha uma opção: ")
            if opcao == "1":
                while True:
                    newName = Utils.inputBack(f"Digite o novo nome do evento (atual: {event.name}): ")
                    if newName.strip() == "":
                        newName = event.name
                    break
                while True:
                    newDescription = Utils.inputBack(f"Digite a nova descrição do evento (atual: {event.description}): ")
                    if newDescription.strip() == "":
                        newDescription = event.description
                    break
                newDate = Utils.inputDate(f"Digite a nova data do evento (atual: {event.date}): ")
                if not newDate:
                    newDate = event.date
                while True:
                    newLocal = Utils.inputBack(f"Digite o novo local do evento (atual: {event.local}): ")
                    if newLocal.strip() == "":
                        newLocal = event.local
                    break
                while True:
                    newSize = Utils.inputBack(f"Digite o novo tamanho do evento (atual: {event.size}): ")
                    if newSize.strip() == "":
                        newSize = event.size
                        break
                    try:
                        newSize = int(newSize)
                        if newSize <= 0:
                            print("Tamanho inválido.")
                            Utils.pause()
                            continue
                        break
                    except ValueError:
                        print("Tamanho inválido.")
                        Utils.pause()
                newTypeEvent = Utils.typeEvents()
                if not newTypeEvent:
                    newTypeEvent = event.typeEvent
                producer.updateEvent(
                    event,
                    name=newName,
                    description=newDescription,
                    date=newDate,
                    local=newLocal,
                    size=newSize,
                    typeEvent=newTypeEvent
                )
                print(f"Evento editado com sucesso! - Evento: {event}")
                Utils.pause()
                break
            elif opcao == "2":
                editTierMenu(producer, event)
                break
            else:
                print("Opção inválida.")
                Utils.pause()
                continue
    except Exception as e:
        print(f"Erro inesperado ao editar evento: {e}")
        Utils.pause()

def deleteEventMenu(producer):
    try:
        Utils.menu("Excluir Evento - ou digite 0 para voltar")
        if not producer.events:
            print("Nenhum evento encontrado.")
            Utils.pause()
            return
        print("Escolha um evento para excluir:")
        for idx, event in enumerate(producer.events, start=1):
            print(f"{idx} - {event.name}")
        try:
            eventIndex = int(Utils.inputBack("Escolha o número do evento: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if eventIndex < 0 or eventIndex >= len(producer.events):
            print("Evento inválido.")
            Utils.pause()
            return
        event = producer.events[eventIndex]
        if producer.deleteEvent(event):
            print(f"Evento excluído com sucesso! - Evento: {event}")
        else:
            print("Erro ao excluir evento.")
        Utils.pause()
    except Exception as e:
        print(f"Erro inesperado ao excluir evento: {e}")
        Utils.pause()

def listEventsMenu(producer):
    producer.listEvents()
    Utils.pause()

def producerEventMenu(producer):
    try:
        while True:
            Utils.menu("Gerenciar Eventos - ou digite 0 para voltar")
            print("Escolha uma opção:")
            print("1. Criar Evento")
            print("2. Editar Evento")
            print("3. Excluir Evento")
            print("4. Listar Eventos")
            print("5. Gerenciar Lotes")
            print("0. Voltar")
            eventOption = Utils.inputBack("Escolha uma opção: ")
            if eventOption == "1":
                createEventMenu(producer)
            elif eventOption == "2":
                editEventMenu(producer)
            elif eventOption == "3":
                deleteEventMenu(producer)
            elif eventOption == "4":
                listEventsMenu(producer)
            elif eventOption == "5":
                producerTierMenu(producer)
            elif eventOption == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")
                Utils.pause()
    except KeyboardInterrupt:
        print("\nSaindo...")
        Utils.pause()
