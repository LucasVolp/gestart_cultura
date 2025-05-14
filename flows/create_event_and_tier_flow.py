from models.producer import Producer
from enums.status import Status
from enums.typeEvent import TypeEvent
from models.event import Event


def create_event(producer: Producer) -> Event:
    print("\n=== Criar Evento ===")
    name = input("Nome do evento: ")
    description = input("Descrição: ")
    date_str = input("Data (YYYY-MM-DD): ")
    location = input("Local: ")
    size = int(input("Capacidade do evento: "))

    print("\nTipos de evento disponíveis:")
    for te in TypeEvent:
        print(f"- {te.name}")

    type_input = input("Tipo de evento (FREE_EVENT / PAID_EVENT): ").strip().upper()

    event = producer.createEvent(
        name=name,
        description=description,
        date=date_str,
        local=location,
        size=size,
        typeEvent=TypeEvent[type_input],
        status=Status.OPEN
    )

    print("\n✅ Evento criado com sucesso!")
    print(event)
    return event


def create_tier(event: Event):
    print("\n=== Criar Lote (Tier) ===")
    name = input("Nome do lote: ")
    price = float(input("Preço do ingresso: "))
    quantity = int(input("Quantidade disponível: "))
    start_date = input("Data de início da venda (YYYY-MM-DD): ")
    end_date = input("Data de término da venda (YYYY-MM-DD): ")

    tier = event.createTier(
        amount=quantity,
        nome=name,
        price=price,
        startDate=start_date,
        endDate=end_date,
        status=Status.OPEN
    )

    print("\nLote criado com sucesso!")
    print(tier)
    return tier


def run_create_event_and_tier_flow(producer: Producer):
    print("\n=== FLUXO: CRIAÇÃO DE EVENTO E LOTE ===")
    event = create_event(producer)
    create_tier(event)