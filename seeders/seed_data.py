from db import SessionLocal
from models.models import Producer, Seller, User, Event, Tier, Rating, Status, TypeEvent, Role
from uuid import uuid4
from datetime import date

session = SessionLocal()

# Usuário comum
if not session.query(User).filter_by(email="joao@email.com").first():
    user1 = User(
        id=uuid4(),
        name="João da Silva",
        cpf="12345678901",
        birth=date(1990, 1, 1),
        email="joao@email.com",
        password="senha123",
        phone="67912345678",
        status=Status.ACTIVE,
        balance=500.0,
        role=Role.USER
    )
    session.add(user1)

# Produtor
if not session.query(Producer).filter_by(email="produtora@email.com").first():
    producer1 = Producer(
        id=uuid4(),
        name="Produtora Eventos",
        cpf="98765432100",
        birth=date(1980, 10, 10),
        email="produtora@email.com",
        password="produtor123",
        phone="67998765432",
        status=Status.ACTIVE,
        role=Role.PRODUCER,
        cnpj="12345678000199",
        enterprise="Eventos Top"
    )
    session.add(producer1)

# Vendedor
if not session.query(Seller).filter_by(email="vendedor@email.com").first():
    seller1 = Seller(
        id=uuid4(),
        name="Vendedor Legal",
        cpf="11122233344",
        birth=date(1985, 5, 5),
        email="vendedor@email.com",
        password="vendedor123",
        phone="67934567890",
        status=Status.ACTIVE,
        role=Role.SELLER
    )
    session.add(seller1)

# EVENTO 1: Pago, com tiers e rating
if not session.query(Event).filter_by(name="Show de Rock").first():
    event1 = Event(
        id=uuid4(),
        name="Show de Rock",
        description="O melhor show de rock do ano!",
        date=date(2025, 6, 20),
        local="Arena MS",
        size=1000,
        typeEvent=TypeEvent.PAID_EVENT,
        status=Status.OPEN
    )
    session.add(event1)
# Tiers para evento 1
    tier1_1 = Tier(id=uuid4(), amount=100, name="Pista", price=100.0, startDate=date(2025, 5, 1), endDate=date(2025, 6, 19), status=Status.OPEN, event=event1)
    tier1_2 = Tier(id=uuid4(), amount=50, name="VIP", price=200.0, startDate=date(2025, 5, 1), endDate=date(2025, 6, 19), status=Status.OPEN, event=event1)
    session.add_all([tier1_1, tier1_2])
# Rating para evento 1
    rating1 = Rating(id=uuid4(), user=user1, event=event1, rate=5, comment="Incrível!")
    session.add(rating1)

# EVENTO 2: Gratuito, com rating
if not session.query(Event).filter_by(name="Feira de Livros").first():
    event2 = Event(
        id=uuid4(),
        name="Feira de Livros",
        description="Evento cultural gratuito para toda a família.",
        date=date(2025, 7, 10),
        local="Praça Central",
        size=500,
        typeEvent=TypeEvent.FREE_EVENT,
        status=Status.OPEN
    )
    session.add(event2)
    rating2 = Rating(id=uuid4(), user=user1, event=event2, rate=4, comment="Muito bom!")
    session.add(rating2)

# EVENTO 3: Pago, com tiers e rating
if not session.query(Event).filter_by(name="Festival de Jazz").first():
    event3 = Event(
        id=uuid4(),
        name="Festival de Jazz",
        description="Jazz ao vivo com grandes artistas.",
        date=date(2025, 8, 15),
        local="Teatro Municipal",
        size=800,
        typeEvent=TypeEvent.PAID_EVENT,
        status=Status.OPEN
    )
    session.add(event3)
    tier3_1 = Tier(id=uuid4(), amount=80, name="Plateia", price=120.0, startDate=date(2025, 6, 1), endDate=date(2025, 8, 14), status=Status.OPEN, event=event3)
    tier3_2 = Tier(id=uuid4(), amount=30, name="Camarote", price=250.0, startDate=date(2025, 6, 1), endDate=date(2025, 8, 14), status=Status.OPEN, event=event3)
    session.add_all([tier3_1, tier3_2])
    rating3 = Rating(id=uuid4(), user=user1, event=event3, rate=5, comment="Jazz maravilhoso!")
    session.add(rating3)

session.commit()
session.close()
