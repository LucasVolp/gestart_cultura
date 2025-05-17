from flows.utils import Utils
from models.purchase import Purchase
from models.receipt import Receipt

def showPurchases(user):
    try:
        purchases = user.getPurchases()
        if not purchases:
            print("Nenhuma compra encontrada.")
        else:
            print("Suas compras:")
            for idx, purchase in enumerate(purchases, start=1):
                print(f"{idx} - {purchase}")
        Utils.pause()
    except Exception as e:
        print(f"Erro ao listar compras: {e}")
        Utils.pause()

def refundPurchaseMenu(user):
    try:
        purchases = user.getPurchases()
        if not purchases:
            print("Nenhuma compra encontrada.")
            Utils.pause()
            return
        print("Escolha uma compra para reembolsar:")
        for idx, purchase in enumerate(purchases, start=1):
            print(f"{idx} - {purchase}")
        try:
            purchaseIndex = int(Utils.inputBack("Escolha o número da compra: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if purchaseIndex < 0 or purchaseIndex >= len(purchases):
            print("Compra inválida.")
            Utils.pause()
            return
        purchase = purchases[purchaseIndex]
        result = user.refundPurchase(purchase)
        if result:
            print("Reembolso solicitado com sucesso!")
        else:
            print("Não foi possível solicitar o reembolso.")
        Utils.pause()
    except Exception as e:
        print(f"Erro ao reembolsar compra: {e}")
        Utils.pause()

def showReceipts(user):
    try:
        if hasattr(user, '_User__receipts'):
            receipts = user._User__receipts
        else:
            receipts = []
        if not receipts:
            print("Nenhum recibo encontrado.")
        else:
            print("Seus recibos:")
            for idx, receipt in enumerate(receipts, start=1):
                print(f"{idx} - {receipt}")
        Utils.pause()
    except Exception as e:
        print(f"Erro ao listar recibos: {e}")
        Utils.pause()

def purchaseMenu(user):
    while True:
        try:
            Utils.menu(f"Menu de Compras - {user.name}")
            print("\nEscolha uma opção:")
            print("1. Minhas Compras")
            print("2. Reembolsar compra")
            print("3. Meus Recibos")
            print("0. Voltar")
            option = input()
            match option:
                case "1":
                    showPurchases(user)
                case "2":
                    refundPurchaseMenu(user)
                case "3":
                    showReceipts(user)
                case "0":
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    Utils.pause()
        except Exception as e:
            print(f"Erro inesperado: {e}")
            Utils.pause()
