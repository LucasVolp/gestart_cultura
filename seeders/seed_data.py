from models.user import User
from models.producer import Producer
from models.seller import Seller
from models.event import Event
from models.tier import Tier
from models.rating import Rating
from enums.status import Status
from enums.typeEvent import TypeEvent
from uuid import uuid4
from datetime import datetime

# Usuário comum
user1 = User(
    id=uuid4(),
    name="João da Silva",
    cpf="12345678901",
    birth="01/01/1990",
    email="joao@email.com",
    password="senha123",
    phone="(67) 91234-5678",
    status=Status.ACTIVE,
    balance=500.0
)
User.users.append(user1)

# Produtor
producer1 = Producer(
    id=uuid4(),
    name="Produtora Eventos",
    cpf="98765432100",
    birth="10/10/1980",
    email="produtora@email.com",
    password="produtor123",
    phone="(67) 99876-5432",
    cnpj="12.345.678/0001-99",
    enterprise="Eventos Top",
    status=Status.ACTIVE
)
Producer.producers.append(producer1)

# Vendedor
seller1 = Seller(
    id=uuid4(),
    name="Vendedor Legal",
    cpf="11122233344",
    birth="05/05/1985",
    email="vendedor@email.com",
    password="vendedor123",
    phone="(67) 93456-7890",
    status=Status.ACTIVE
)
Seller.sellers.append(seller1)

# EVENTO 1: Pago, com tiers e rating

event1 = Event(
    id=uuid4(),
    name="Show de Rock",
    description="O melhor show de rock do ano!",
    date="20/06/2025",
    local="Arena MS",
    size=1000,
    typeEvent=TypeEvent.THEATER,
    status=Status.OPEN
)
# Tiers para evento 1

tier1_1 = Tier(id=uuid4(), amount=100, name="Pista", price=100.0, startDate="01/05/2025", endDate="19/06/2025", status=Status.OPEN, event=event1)
tier1_2 = Tier(id=uuid4(), amount=50, name="VIP", price=200.0, startDate="01/05/2025", endDate="19/06/2025", status=Status.OPEN, event=event1)
event1.addTier(tier1_1)
event1.addTier(tier1_2)
# Rating para evento 1
rating1 = Rating(id=uuid4(), user=user1, event=event1, rate=5, comment="Incrível!")
event1.addRating(rating1)
Event.events.append(event1)

# EVENTO 2: Gratuito, com rating

event2 = Event(
    id=uuid4(),
    name="Feira de Livros",
    description="Evento cultural gratuito para toda a família.",
    date="10/07/2025",
    local="Praça Central",
    size=500,
    typeEvent=TypeEvent.FREE_EVENT,
    status=Status.OPEN
)
rating2 = Rating(id=uuid4(), user=user1, event=event2, rate=4, comment="Muito bom!")
event2.addRating(rating2)
Event.events.append(event2)

# EVENTO 3: Pago, com tiers e rating

event3 = Event(
    id=uuid4(),
    name="Festival de Jazz",
    description="Jazz ao vivo com grandes artistas.",
    date="15/08/2025",
    local="Teatro Municipal",
    size=800,
    typeEvent=TypeEvent.THEATER,
    status=Status.OPEN
)
tier3_1 = Tier(id=uuid4(), amount=80, name="Plateia", price=120.0, startDate="01/06/2025", endDate="14/08/2025", status=Status.OPEN, event=event3)
tier3_2 = Tier(id=uuid4(), amount=30, name="Camarote", price=250.0, startDate="01/06/2025", endDate="14/08/2025", status=Status.OPEN, event=event3)
event3.addTier(tier3_1)
event3.addTier(tier3_2)
rating3 = Rating(id=uuid4(), user=user1, event=event3, rate=5, comment="Jazz maravilhoso!")
event3.addRating(rating3)
Event.events.append(event3)

# Nenhum ticket criado diretamente aqui. Se necessário, criar Ticket com seller=algum_seller
