# Este arquivo permite que o diretório models seja tratado como um pacote Python

# Primeiro as classes base e independentes
from models.person import Person
from models.tier import Tier

# Depois as classes que dependem das bases
from models.event import Event
from models.purchaseItems import PurchaseItems

# Classes de usuário
from models.user import User
from models.seller import Seller
from models.producer import Producer

# Por último as classes mais dependentes
from models.purchase import Purchase
from models.ticket import Ticket
from models.rating import Rating
from models.receipt import Receipt

__all__ = [
    'Person',
    'Tier',
    'Event',
    'PurchaseItems',
    'User',
    'Seller',
    'Producer',
    'Purchase',
    'Ticket',
    'Rating',
    'Receipt'
] 