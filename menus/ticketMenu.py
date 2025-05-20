from flows.utils import Utils, MenuBackException
from enums.paymentMethods import PaymentMethods
from enums.typeEvent import TypeEvent
from models.event import Event
from models.seller import Seller

def listTickets(user):
    try:
        Utils.menu(f"Meus Ingressos - {user.name}")
        tickets = user.getTickets()
        print("Ingressos disponíveis:")
        for idx, ticket in enumerate(tickets, start=1):
            print(f"{idx} - Dono: {ticket.owner.name} - Lote: {ticket.tier.name} - Vendedor: {ticket.seller.name} - Código do Ingresso: {ticket.code} - Status: {ticket.status.name}")
        Utils.pause()

    except ValueError as e:
        print(str(e))  
        Utils.pause()
    except MenuBackException:
        return

def buyTicket(user):
    try:
        Utils.menu(f"Comprar Ingressos - {user.name}")
        events = Event.events
        sellers = Seller.sellers

        if not events:
            print("Nenhum evento encontrado.")
            Utils.pause()
            return

        print("Escolha um evento para comprar ingressos:")
        for idx, event in enumerate(events, start=1):
            if event.status == "CLOSED":
                continue
            print(f"{idx} - {event.name} - {event.description} - {event.date} - {event.local} ")
        try:
            eventIndex = int(Utils.inputBack("Escolha o número do evento: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if eventIndex < 0 or eventIndex >= len(events):
            print("Evento inválido.")
            Utils.pause()
            return

        selectedEvent = events[eventIndex]
        if selectedEvent.typeEvent == TypeEvent.FREE_EVENT:
            print("Este evento é gratuito. Você não precisa comprar ingressos. - Deseja registrar-se?")
            print("1 - Sim")
            print("2 - Não")
            option = Utils.inputBack("Escolha uma opção: ")
            if option == "1":
                if user.registerInFreeEvent(selectedEvent):
                    print(f"Você se registrou com sucesso no evento {selectedEvent.name}.")
                else:
                    print("Erro ao registrar-se no evento.")
                    Utils.pause()
                    return
            elif option == "2":
                print("Você não se registrou no evento.")
                Utils.pause()
                return

        print(f"Escolha um lote para o evento {selectedEvent.name}:")
        tiers = selectedEvent.getTiers()
        if not tiers:
            print("Nenhum lote encontrado.")
            Utils.pause()
            return

        for idx, tier in enumerate(tiers, start=1):
            print(f"{idx} - {tier.name} - {tier.price} - {tier.startDate} - {tier.endDate} - {tier.status.name}")
        try:
            tierIndex = int(Utils.inputBack("Escolha o número do lote: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if tierIndex < 0 or tierIndex >= len(tiers):
            print("Lote inválido.")
            Utils.pause()
            return

        selectedTier = tiers[tierIndex]
        if selectedTier.getDisponibility() <= 0:
            print("Nenhum ingresso disponível neste lote.")
            Utils.pause()
            return

        print(f"Escolha a quantidade de ingressos para o lote {selectedTier.name}:")
        try:
            amount = int(Utils.inputBack("Quantidade: "))
        except ValueError:
            print("Quantidade inválida.")
            Utils.pause()
            return
        if amount <= 0 or amount > selectedTier.getDisponibility():
            print("Quantidade inválida.")
            Utils.pause()
            return

        print(f"Escolha um vendedor para o evento {selectedEvent.name}:")
        for idx, seller in enumerate(sellers, start=1):
            print(f"{idx} - {seller.name} - {seller.email}")
        try:
            sellerIndex = int(Utils.inputBack("Escolha o número do vendedor: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if sellerIndex < 0 or sellerIndex >= len(sellers):
            print("Vendedor inválido.")
            Utils.pause()
            return
        selectedSeller = sellers[sellerIndex]

        print("Escolha o método de pagamento:")
        for idx, method in enumerate(PaymentMethods, start=1):
            print(f"{idx} - {method.name}")
        try:
            paymentMethodIndex = int(Utils.inputBack("Escolha o número do método de pagamento: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if paymentMethodIndex < 0 or paymentMethodIndex >= len(PaymentMethods):
            print("Método de pagamento inválido.")
            Utils.pause()
            return
        selectedPaymentMethod = list(PaymentMethods)[paymentMethodIndex]
        purchase = user.buyTicket(selectedTier, amount, selectedSeller, selectedPaymentMethod)
        if purchase:
            print(f"Compra realizada com sucesso! Você comprou {amount} ingressos do lote {selectedTier.name} para o evento {selectedEvent.name}.")
            print(f"Pague a quantia de R$ {selectedTier.price * amount} no menu de minhas compras para receber os ingressos.")
        else:
            print("Erro ao realizar a compra.")
        Utils.pause()
    except MenuBackException:
        return
    except Exception as e:
        print(f"Erro inesperado ao comprar ingresso: {e}")
        Utils.pause()

def transferTicketMenu(user):
    try:
        Utils.menu(f"Transferir Ingressos - {user.name}")
        tickets = user.getTickets()
        if not tickets:
            print("Nenhum ingresso disponível para transferência.")
            Utils.pause()
            return
        print("Ingressos disponíveis para transferência:")
        for idx, ticket in enumerate(tickets, start=1):
            print(f"{idx} - {ticket}")
        try:
            ticketIndex = int(Utils.inputBack("Escolha o número do ingresso para transferir: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if ticketIndex < 0 or ticketIndex >= len(tickets):
            print("Ingresso inválido.")
            Utils.pause()
            return
        ticket = tickets[ticketIndex]
        newCPF = Utils.inputBack("Digite o CPF do novo proprietário: ")
        try:
            user.transferTicket(ticket, newCPF)
            print("Ingresso transferido com sucesso!")  
        except ValueError as e:
            print(f"Erro inesperado ao transferir ingresso: {e}")
        Utils.pause()
    except MenuBackException:
      return

def ticketMenu(user):
    while True:
        try:
            Utils.menu(f"Bem vindo(a) ao menu de Ingressos, {user.name}")
            print("\nEscolha uma opção:")
            print("1. Comprar Ingressos")
            print("2. Meus Ingressos")
            print("3. Transferir Ingressos")
            print("0. Sair")
            option = input()
            match option:
                case "1":
                    buyTicket(user)
                case "2":
                    listTickets(user)
                case "3":
                    transferTicketMenu(user)
                case "0":
                    print("Saindo do menu de ingressos...")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    Utils.pause()
        except MenuBackException:
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            Utils.pause()
