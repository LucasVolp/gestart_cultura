from flows.utils import Utils
from models.event import Event
from models.seller import Seller

def listTickets(user):
        Utils.menu(f"Meus Ingressos - {user.name}")
        tickets = user.getTickets()
        if not tickets:
            print("Nenhum ingresso encontrado.")
        else:
            print("Ingressos disponíveis:")
            for idx, ticket in enumerate(tickets, start=1):
                print(f"{idx} - {ticket}")
        Utils.pause()

def buyTicket(user):
    Utils.menu(f"Comprar Ingressos - {user.name}")
    events = Event.events
    sellers = Seller.sellers
    
    if not events:
        print("Nenhum evento encontrado.")
        Utils.pause()
        return
    
    print("Escolha um evento para comprar ingressos:")
    for idx, event in enumerate(events, start=1):
        print(f"{idx} - {event.name} - {event.description} - {event.date} - {event.local} ")
    eventIndex = int(Utils.inputBack("Escolha o número do evento: ")) - 1
    
    if eventIndex < 0 or eventIndex >= len(events):
        print("Evento inválido.")
        Utils.pause()
        return
    
    selectedEvent = events[eventIndex]
    print(f"Escolha um lote para o evento {selectedEvent.name}:")
    tiers = selectedEvent.getTiers()
    if not tiers:
        print("Nenhum lote encontrado.")
        Utils.pause()
        return
    
    for idx, tier in enumerate(tiers, start=1):
        print(f"{idx} - {tier.name} - {tier.price} - {tier.startDate} - {tier.endDate} - {tier.status.name}")
    tierIndex = int(Utils.inputBack("Escolha o número do lote: ")) - 1
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
    amount = int(Utils.inputBack("Quantidade: "))
    if amount <= 0 or amount > selectedTier.getDisponibility():
        print("Quantidade inválida.")
        Utils.pause()
        return
    
    print(f"Escolha um vendedor para o evento {selectedEvent.name}:")
    for idx, seller in enumerate(sellers, start=1):
        print(f"{idx} - {seller.name} - {seller.email}")
    sellerIndex = int(Utils.inputBack("Escolha o número do vendedor: ")) - 1
    if sellerIndex < 0 or sellerIndex >= len(sellers):
        print("Vendedor inválido.")
        Utils.pause()
        return
    selectedSeller = sellers[sellerIndex]
    if selectedSeller.createPurchase(selectedTier, amount, user, "cartão de crédito"):
        print(f"Compra realizada com sucesso! Você comprou {amount} ingressos do lote {selectedTier.name} para o evento {selectedEvent.name}.")
        print(f"Pague a quantia de R$ {selectedTier.price * amount} no menu de minhas compras para receber os ingressos.")
    else:
        print("Erro ao realizar a compra.")
    Utils.pause()

def ticketMenu(user):
    while True:
        Utils.menu(f"Bem vindo(a) ao menu de Ingressos, {user.name}")
        print("\nEscolha uma opção:")
        print("1. Comprar Ingressos")
        print("2. Meus Ingressos")
        print("3. Transferir Ingressos")
        print("0. Sair")
        option = input()
        match option:
            case "1":
                pass
            case "2":
                listTickets(user)
            case "3":
                pass
            case "0":
                print("Saindo do menu de ingressos...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
        