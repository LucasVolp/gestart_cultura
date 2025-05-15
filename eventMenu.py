from enums.status import Status
from flows.utils import Utils
from tierMenu import createTierMenu, editTierMenu

def createEventMenu(producer):
    Utils.menu("Criação de Evento - ou digite 0 para voltar")
    name = Utils.inputBack("Digite o nome do evento: ")
    description = Utils.inputBack("Digite a descrição do evento: ")
    date = Utils.inputDate("Digite a data do evento (DD/MM/AAAA): ")
    local = Utils.inputBack("Digite o local do evento: ")
    size = int(Utils.inputBack("Digite o tamanho do evento: "))
    typeEvent = Utils.typeEvents()
    event = producer.createEvent(name=name, description=description, date=date, local=local, size=size, typeEvent=typeEvent, status=Status.OPEN)
    if event:
        print(f"Evento criado com sucesso! - Evento: {event}")
        Utils.pause()
        Utils.menu("Deseja criar um lote para este evento agora?")
        print("1. Sim")
        print("2. Não")
        opcao = Utils.inputBack("Escolha uma opção: ")
        if opcao == "1":
            createTierMenu(producer, event)
        elif opcao == "2":
            print("Voltando ao menu de eventos.")
    else:
        print("Erro ao criar evento.")
    Utils.pause()

def editEventMenu(producer):
    Utils.menu("Edição de Evento - ou digite 0 para voltar")
    if not producer.events:
        print("Nenhum evento encontrado.")
        Utils.pause()
        return
    print("Escolha um evento para editar:")
    for idx, event in enumerate(producer.events, start=1):
        print(f"{idx} - {event.name}")
    eventIndex = int(Utils.inputBack("Escolha o número do evento: ")) - 1
    if eventIndex < 0 or eventIndex >= len(producer.events):
        print("Evento inválido.")
        Utils.pause()
        return
    event = producer.events[eventIndex]
    Utils.menu("O que deseja editar?")
    print("1. Editar dados do evento")
    print("2. Editar lotes do evento")
    opcao = Utils.inputBack("Escolha uma opção: ")
    if opcao == "1":
        newName = Utils.inputBack(f"Digite o novo nome do evento (atual: {event.name}): ")
        if newName.strip() == "":
            newName = event.name
        newDescription = Utils.inputBack(f"Digite a nova descrição do evento (atual: {event.description}): ")
        if newDescription.strip() == "":
            newDescription = event.description
        newDate = Utils.inputDate(f"Digite a nova data do evento (atual: {event.date}): ")
        if not newDate:
            newDate = event.date
        newLocal = Utils.inputBack(f"Digite o novo local do evento (atual: {event.local}): ")
        if newLocal.strip() == "":
            newLocal = event.local
        newSize = Utils.inputBack(f"Digite o novo tamanho do evento (atual: {event.size}): ")
        if newSize.strip() == "":
            newSize = event.size
        else:
            newSize = int(newSize)
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
    elif opcao == "2":
        editTierMenu(producer, event)
    else:
        print("Opção inválida.")
        Utils.pause()

def deleteEventMenu(producer):
    Utils.menu("Excluir Evento - ou digite 0 para voltar")
    if not producer.events:
        print("Nenhum evento encontrado.")
        Utils.pause()
        return
    print("Escolha um evento para excluir:")
    for idx, event in enumerate(producer.events, start=1):
        print(f"{idx} - {event.name}")
    eventIndex = int(Utils.inputBack("Escolha o número do evento: ")) - 1
    if eventIndex < 0 or eventIndex >= len(producer.events):
        print("Evento inválido.")
        Utils.pause()
        return
    event = producer.events[eventIndex]
    if producer.deleteEvent(event):
        print("Evento excluído com sucesso!")
    else:
        print("Erro ao excluir evento.")
    Utils.pause()

def listEventsMenu(producer):
    producer.listEvents()
    Utils.pause()

def producerEventMenu(producer):
    while True:
        Utils.menu("Gerenciar Eventos - ou digite 0 para voltar")
        print("Escolha uma opção:")
        print("1. Criar Evento")
        print("2. Editar Evento")
        print("3. Excluir Evento")
        print("4. Listar Eventos")
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
        elif eventOption == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            Utils.pause()
