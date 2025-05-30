from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, Date, DateTime, ForeignKey, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum
import uuid
from db import Base

class Status(enum.Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    DELETED = 'DELETED'
    VALID = 'VALID'
    CANCELLED = 'CANCELLED'
    CLOSED = 'CLOSED'
    OPEN = 'OPEN'

class TypeEvent(enum.Enum):
    FREE_EVENT = 'FREE_EVENT'
    PAID_EVENT = 'PAID_EVENT'

class PaymentStatus(enum.Enum):
    PENDING = 'PENDING'
    PAID = 'PAID'
    REFUNDED = 'REFUNDED'

class PaymentMethod(enum.Enum):
    CREDIT = 'CREDIT'
    DEBIT = 'DEBIT'
    PIX = 'PIX'
    CASH = 'CASH'

class Role(enum.Enum):
    USER = 'USER'
    PRODUCER = 'PRODUCER'
    SELLER = 'SELLER'
    ADMIN = 'ADMIN'

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    birth = Column(Date, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    status = Column(Enum(Status), default=Status.ACTIVE)
    role = Column(Enum(Role), nullable=False)
    balance = Column(Float, default=1000)
    createdAt = Column(DateTime, nullable=False, default=datetime.now)
    updatedAt = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    __mapper_args__ = {
        "polymorphic_identity": Role.USER,
        "polymorphic_on": role,
    }

    tickets = relationship('Ticket', back_populates='owner', foreign_keys='Ticket.ownerId')
    ratings = relationship('Rating', back_populates='user')
    purchases = relationship('Purchase', back_populates='buyer', foreign_keys='Purchase.buyerId')
    receipts = relationship('Receipt', back_populates='user')
    events = relationship('Event', secondary='eventProducers', back_populates='producers')

class Producer(User):
    __tablename__ = 'producers'

    id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)
    cnpj = Column(String(14), unique=True, nullable=False)
    enterprise = Column(String, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": Role.PRODUCER,
    }

class Seller(User):
    __tablename__ = 'sellers'

    id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": Role.SELLER,
    }

    sales = relationship('Purchase', back_populates='seller', foreign_keys='Purchase.sellerId')

class Event(Base):
    __tablename__ = 'events'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(Text)
    date = Column(Date, nullable=False)
    local = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    typeEvent = Column(Enum(TypeEvent), nullable=False)
    status = Column(Enum(Status), default=Status.ACTIVE)

    tiers = relationship('Tier', back_populates='event')
    ratings = relationship('Rating', back_populates='event')
    producers = relationship('User', secondary='eventProducers', back_populates='events')

class EventProducer(Base):
    __tablename__ = 'eventProducers'
    eventId = Column(UUID(as_uuid=True), ForeignKey('events.id'), primary_key=True)
    producerId = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)

class Tier(Base):
    __tablename__ = 'tiers'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    amount = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    status = Column(Enum(Status), default=Status.OPEN)
    eventId = Column(UUID(as_uuid=True), ForeignKey('events.id'))
    createdAt = Column(DateTime, nullable=False, default=datetime.now)
    updatedAt = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    event = relationship('Event', back_populates='tiers')
    tickets = relationship('Ticket', back_populates='tier')
    

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ownerId = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    tierId = Column(UUID(as_uuid=True), ForeignKey('tiers.id'))
    sellerId = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    status = Column(Enum(Status), default=Status.VALID)
    code = Column(String, unique=True, nullable=False)
    createdAt = Column(DateTime, nullable=False, default=datetime.now)
    updatedAt = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    owner = relationship('User', back_populates='tickets', foreign_keys=[ownerId])
    tier = relationship('Tier', back_populates='tickets')
    seller = relationship('User', foreign_keys=[sellerId])

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    userId = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    eventId = Column(UUID(as_uuid=True), ForeignKey('events.id'))
    rate = Column(Integer, nullable=False)
    comment = Column(Text)
    createdAt = Column(DateTime, nullable=False, default=datetime.now)
    updatedAt = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    user = relationship('User', back_populates='ratings')
    event = relationship('Event', back_populates='ratings')

class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    buyerId = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    sellerId = Column(UUID(as_uuid=True), ForeignKey('sellers.id'))
    purchaseDate = Column(DateTime, nullable=False)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    totalPrice = Column(Float, nullable=False)
    paymentMethod = Column(Enum(PaymentMethod), nullable=False)
    createdAt = Column(DateTime, nullable=False, default=datetime.now)
    updatedAt = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    buyer = relationship('User', back_populates='purchases', foreign_keys=[buyerId])
    seller = relationship('Seller', back_populates='sales', foreign_keys=[sellerId])
    items = relationship('PurchaseItem', back_populates='purchase')
    receipt = relationship('Receipt', uselist=False, back_populates='purchase')

class PurchaseItem(Base):
    __tablename__ = 'purchaseItems'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    purchaseId = Column(UUID(as_uuid=True), ForeignKey('purchases.id'))
    tierId = Column(UUID(as_uuid=True), ForeignKey('tiers.id'))
    quantity = Column(Integer, nullable=False)
    unitPrice = Column(Float, nullable=False)
    totalPrice = Column(Float, nullable=False)
    createdAt = Column(DateTime, nullable=False, default=datetime.now)
    updatedAt = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    purchase = relationship('Purchase', back_populates='items')
    tier = relationship('Tier')

class Receipt(Base):
    __tablename__ = 'receipts'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    userId = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    purchaseId = Column(UUID(as_uuid=True), ForeignKey('purchases.id'))
    description = Column(Text)
    createdAt = Column(DateTime, nullable=False, default=datetime.now)
    updatedAt = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    user = relationship('User', back_populates='receipts')
    purchase = relationship('Purchase', back_populates='receipt')