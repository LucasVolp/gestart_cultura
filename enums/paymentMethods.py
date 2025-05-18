from enum import Enum

class PaymentMethods(Enum):
    CREDIT_CARD = "Cartão de Crédito"
    DEBIT_CARD = "Cartão de Débito"
    PIX = "PIX"
    BANK_SLIP = "Boleto Bancário"
    PAYPAL = "PayPal"
    CASH = "Dinheiro"