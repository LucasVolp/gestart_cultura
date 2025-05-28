from enums.status import Status
from flows.utils import Utils, MenuBackException
from .tierMenu import createTierMenu, editTierMenu, producerTierMenu

def createEventMenu(producer):
    try:
        while True:
            try:
                Utils.menu("Criação de Evento - ou digite 0 para voltar")
                name = Utils.inputBack("Digite o nome do evento: ")
                if not name.strip():
                    print("Nome não pode ser vazio.")
                    Utils.pause()
                    continue
                description = Utils.inputBack("Digite a descrição do evento: ")
                if not description.strip():
                    print("Descrição não pode ser vazia.")
                    Utils.pause()
                    continue
                date = Utils.inputDate("Digite a data do evento (DD/MM/AAAA): ")
                local = Utils.inputBack("Digite o local do evento: ")
                if not local.strip():
                    print("Local não pode ser vazio.")
                    Utils.pause()
                    continue
                size_input = Utils.inputBack("Digite o tamanho do evento: ")
                try:
                    size = int(size_input)
                    if size <= 0:
                        print("Tamanho deve ser maior que zero.")
                        Utils.pause()
                        continue
                except ValueError:
                    print("Tamanho inválido.")
                    Utils.pause()
                    continue
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
                        print("Opção inválida.")
                        Utils.pause()
                    return
                else:
                    print("Erro ao criar evento.")
                    Utils.pause()
                    return
            except MenuBackException:
                return
    except Exception as e:
        print(f"Erro inesperado ao criar evento: {e}")
        Utils.pause()

def editEventMenu(producer):
    try:
        while True:
            try:
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
                    continue
                event = producer.events[eventIndex]
                Utils.menu("O que deseja editar?")
                print("1. Editar dados do evento")
                print("2. Editar lotes do evento")
                print("0. Voltar")
                opcao = Utils.inputBack("Escolha uma opção: ")
                if opcao == "0":
                    return
                elif opcao == "1":
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
                    newSize_input = Utils.inputBack(f"Digite o novo tamanho do evento (atual: {event.size}): ")
                    if newSize_input.strip() == "":
                        newSize = event.size
                    else:
                        try:
                            newSize = int(newSize_input)
                            if newSize <= 0:
                                print("Tamanho inválido.")
                                Utils.pause()
                                continue
                        except ValueError:
                            print("Tamanho inválido.")
                            Utils.pause()
                            continue
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
                    return
                elif opcao == "2":
                    editTierMenu(producer, event)
                    return
                else:
                    print("Opção inválida.")
                    Utils.pause()
                    continue
            except MenuBackException:
                return
            except ValueError:
                print("Entrada inválida. Digite um número.")
                Utils.pause()
                continue
    except Exception as e:
        print(f"Erro inesperado ao editar evento: {e}")
        Utils.pause()

def deleteEventMenu(producer):
    try:
        while True:
            try:
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
                    continue
                event = producer.events[eventIndex]
                if producer.deleteEvent(event):
                    print(f"Evento excluído com sucesso! - Evento: {event}")
                else:
                    print("Erro ao excluir evento.")
                Utils.pause()
                return
            except MenuBackException:
                return
            except ValueError:
                print("Entrada inválida. Digite um número.")
                Utils.pause()
                continue
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
            try:
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
            except MenuBackException:
                break
    except KeyboardInterrupt:
        print("\nSaindo...")
        Utils.pause()
