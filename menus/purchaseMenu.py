from flows.utils import Utils, MenuBackException

def showPurchases(user):
    try:
        purchases = user.getPurchases()
        print("Suas compras:")
        for idx, purchase in enumerate(purchases, start=1):
            print(f"{idx} - ID: {purchase.id} | Data: {purchase.purchaseDate} | Total: {purchase.totalPrice} | Status: {purchase.status.name} | Método: {purchase.paymentMethod.name}")
        Utils.pause()
    except Exception as e:
        print(str(e))
        Utils.pause()
    except MenuBackException:
       return
    
def refundPurchaseMenu(user):
    try:
        purchases = user.getPurchases()
        if not purchases:
            print("Nenhuma compra encontrada.")
            Utils.pause()
            return
        print("Escolha uma compra para reembolsar:")
        for idx, purchase in enumerate(purchases, start=1):
            print(f"{idx} - ID: {purchase.id} | Data: {purchase.purchaseDate} | Total: {purchase.totalPrice} | Status: {purchase.status.name} | Método: {purchase.paymentMethod.name}")
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
    except MenuBackException:
        return
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
                print(f"{idx} - ID: {receipt.id} | ID da compra: {receipt.purchase.id} | Proprietário: {receipt.purchase.buyer.name} | Vendedor: {receipt.purchase.seller.name} | Data: {receipt.date} | Total: {receipt.purchase.totalPrice} | Descrição: {receipt.description} | Status: {receipt.purchase.status.name} | Método: {receipt.purchase.paymentMethod.name}")
        Utils.pause()
    except MenuBackException:
        return
    except Exception as e:
        print(f"Erro ao listar recibos: {e}")
        Utils.pause()

def payPurchaseMenu(user):
    try:
        
        purchases = user.getPurchases()
        pendingPurchases = [p for p in purchases if hasattr(p, 'status') and getattr(p, 'status').name == 'PENDING']
        if not pendingPurchases:
            print("Nenhuma compra pendente para pagamento.")
            Utils.pause()
            return
        print(f"Escolha uma compra para pagar - Saldo atual: {user.balance}")
        for idx, purchase in enumerate(pendingPurchases, start=1):
            itens = ", ".join([f"{item.tier.name} ({item.quantity})" for item in purchase.items])
            print(f"{idx} - ID: {purchase.id} - Itens: {itens} | Data: {purchase.purchaseDate} | Total: {purchase.totalPrice} | Status: {purchase.status.name} | Método: {purchase.paymentMethod.name}")
        try:
            purchaseIndex = int(Utils.inputBack("Escolha o número da compra: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if purchaseIndex < 0 or purchaseIndex >= len(pendingPurchases):
            print("Compra inválida.")
            Utils.pause()
            return
        purchase = pendingPurchases[purchaseIndex]
        user.payPurchase(purchase)
        Utils.pause()
    except MenuBackException:
        return
    except Exception as e:
        print(f"Erro ao pagar compra: {e}")
        Utils.pause()

def purchaseMenu(user):
    while True:
        try:
            Utils.menu(f"Menu de Compras - {user.name} - Saldo atual: {user.balance}")
            print("\nEscolha uma opção:")
            print("1. Minhas Compras")
            print("2. Reembolsar compra")
            print("3. Meus Recibos")
            print("4. Pagar Compra/Pagamento de Ingresso")
            print("0. Voltar")
            option = input()
            match option:
                case "1":
                    showPurchases(user)
                case "2":
                    refundPurchaseMenu(user)
                case "3":
                    showReceipts(user)
                case "4":
                    payPurchaseMenu(user)
                case "0":
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    Utils.pause()
        except MenuBackException:
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            Utils.pause()
