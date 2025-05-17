from flows.utils import Utils, MenuBackException


def createTierMenu(producer, event=None):
    try:
        Utils.menu("Criação de Lote - ou digite 0 para voltar")
        if event is None:
            if not producer.events:
                print("Nenhum evento encontrado.")
                Utils.pause()
                return
            print("Escolha um evento para criar um lote:")
            for idx, ev in enumerate(producer.events, start=1):
                print(f"{idx} - {ev.name}")
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
            selected_event = producer.events[eventIndex]
        else:
            selected_event = event
        try:
            amount = int(Utils.inputBack("Digite a quantidade de ingressos do lote: "))
            price = float(Utils.inputBack("Digite o preço do lote: "))
        except ValueError:
            print("Quantidade ou preço inválido.")
            Utils.pause()
            return
        name = Utils.inputBack("Digite o nome do lote: ")
        startDate = Utils.inputDate("Digite a data de início do lote (DD/MM/AAAA): ")
        endDate = Utils.inputDate("Digite a data de término do lote (DD/MM/AAAA): ")
        status = Utils.statusEnum()
        tier = selected_event.createTier(amount=amount, name=name, price=price, startDate=startDate, endDate=endDate, status=status)
        if tier:
            print(f"Lote criado com sucesso! - Lote: {tier}")
        else:
            print("Erro ao criar lote.")
        Utils.pause()
    except MenuBackException:
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        Utils.pause()


def editTierMenu(producer, event=None):
    try:
        Utils.menu("Edição de Lote - ou digite 0 para voltar")
        if event is None:
            if not producer.events:
                print("Nenhum evento encontrado.")
                Utils.pause()
                return
            print("Escolha um evento para editar um lote:")
            for idx, ev in enumerate(producer.events, start=1):
                print(f"{idx} - {ev.name}")
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
            selected_event = producer.events[eventIndex]
        else:
            selected_event = event
        if not selected_event.tiers:
            print("Nenhum lote encontrado.")
            Utils.pause()
            return
        print("Escolha um lote para editar:")
        for idx, tier in enumerate(selected_event.tiers, start=1):
            print(f"{idx} - {tier.name}")
        try:
            tierIndex = int(Utils.inputBack("Escolha o número do lote: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if tierIndex < 0 or tierIndex >= len(selected_event.tiers):
            print("Lote inválido.")
            Utils.pause()
            return
        tier = selected_event.tiers[tierIndex]
        print("O que deseja fazer?")
        print("1. Abrir Lote")
        print("2. Fechar Lote")
        print("3. Editar informações do Lote")
        opcao = Utils.inputBack("Escolha uma opção: ")
        if opcao == "1":
            result = tier.openTier()
            if result:
                print("Lote aberto com sucesso!")
            else:
                print("Não foi possível abrir o lote.")
        elif opcao == "2":
            result = tier.closeTier()
            if result:
                print("Lote fechado com sucesso!")
            else:
                print("Não foi possível fechar o lote.")
        elif opcao == "3":
            try:
                newAmountStr = Utils.inputBack(f"Digite a nova quantidade de ingressos do lote (atual: {tier.amount}): ")
                if newAmountStr.strip() == "":
                    newAmount = tier.amount
                else:
                    newAmount = int(newAmountStr)
                newName = Utils.inputBack(f"Digite o novo nome do lote (atual: {tier.name}): ")
                if newName.strip() == "":
                    newName = tier.name
                newPriceStr = Utils.inputBack(f"Digite o novo preço do lote (atual: {tier.price}): ")
                if newPriceStr.strip() == "":
                    newPrice = tier.price
                else:
                    newPrice = float(newPriceStr)
            except ValueError:
                print("Quantidade ou preço inválido.")
                Utils.pause()
                return
            newStartDate = Utils.inputDate(f"Digite a nova data de início do lote (atual: {tier.startDate}): ")
            if not newStartDate:
                newStartDate = tier.startDate
            newEndDate = Utils.inputDate(f"Digite a nova data de término do lote (atual: {tier.endDate}): ")
            if not newEndDate:
                newEndDate = tier.endDate
            newStatus = Utils.statusEnum()
            if not newStatus:
                newStatus = tier.status
            updatedTier = selected_event.updateTier(tier, amount=newAmount, name=newName, price=newPrice, startDate=newStartDate, endDate=newEndDate, status=newStatus)
            if updatedTier:
                print(f"Lote editado com sucesso! - Lote: {updatedTier}")
            else:
                print("Erro ao editar lote.")
        else:
            print("Opção inválida.")
        Utils.pause()
    except MenuBackException:
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        Utils.pause()


def deleteTierMenu(producer, event=None):
    try:
        Utils.menu("Excluir Lote - ou digite 0 para voltar")
        if event is None:
            if not producer.events:
                print("Nenhum evento encontrado.")
                Utils.pause()
                return
            print("Escolha um evento para excluir um lote:")
            for idx, ev in enumerate(producer.events, start=1):
                print(f"{idx} - {ev.name}")
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
            selected_event = producer.events[eventIndex]
        else:
            selected_event = event
        if not selected_event.tiers:
            print("Nenhum lote encontrado.")
            Utils.pause()
            return
        print("Escolha um lote para excluir:")
        for idx, tier in enumerate(selected_event.tiers, start=1):
            print(f"{idx} - {tier.name}")
        try:
            tierIndex = int(Utils.inputBack("Escolha o número do lote: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if tierIndex < 0 or tierIndex >= len(selected_event.tiers):
            print("Lote inválido.")
            Utils.pause()
            return
        tier = selected_event.tiers[tierIndex]
        if selected_event.deleteTier(tier):
            print(f"Lote excluído com sucesso! - Lote: {tier}")
        else:
            print("Erro ao excluir lote.")
        Utils.pause()
    except MenuBackException:
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        Utils.pause()


def listTiersMenu(producer, event=None):
    try:
        Utils.menu("Listar Lotes - ou digite 0 para voltar")
        if event is None:
            if not producer.events:
                print("Nenhum evento encontrado.")
                Utils.pause()
                return
            print("Escolha um evento para listar os lotes:")
            for idx, ev in enumerate(producer.events, start=1):
                print(f"{idx} - {ev.name}")
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
            selected_event = producer.events[eventIndex]
        else:
            selected_event = event
        if not selected_event.tiers:
            print("Nenhum lote encontrado.")
            Utils.pause()
            return
        print("Lotes disponíveis:")
        for idx, tier in enumerate(selected_event.tiers, start=1):
            print(f"{idx} - {tier.name} - Preço: {tier.price} - Ingressos restantes: {tier.amount} - Status: {tier.status}")
        Utils.pause()
    except MenuBackException:
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        Utils.pause()


def producerTierMenu(producer, event=None):
    while True:
        try:
            Utils.menu("Gerenciar Lotes - ou digite 0 para voltar")
            print("Escolha uma opção:")
            print("1. Criar Lote")
            print("2. Editar Lote")
            print("3. Excluir Lote")
            print("4. Listar Lotes")
            print("0. Voltar")
            tierOptions = Utils.inputBack("Escolha uma opção: ")
            if tierOptions == "1":
                createTierMenu(producer, event)
            elif tierOptions == "2":
                editTierMenu(producer, event)
            elif tierOptions == "3":
                deleteTierMenu(producer, event)
            elif tierOptions == "4":
                listTiersMenu(producer, event)
            elif tierOptions == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")
                Utils.pause()
        except MenuBackException:
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            Utils.pause()
