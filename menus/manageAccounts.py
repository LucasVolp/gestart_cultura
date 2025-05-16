from flows.utils import Utils
from models.producer import Producer


def manageAccounts(account):
    while True:
        Utils.menu("Gerenciar Conta")
        print("Escolha uma opção:")
        print("1. Editar Conta")
        print("2. Excluir Conta")
        print("0. Voltar")
        option = Utils.inputBack("Escolha uma opção: ")
        if option == "1":
            print("Digite os novos dados da conta (ou deixe em branco para não alterar):")
            newName = Utils.inputBack(f"Nome (atual: {account.name}): ")
            if not newName.strip():
                newName = account.name
            newBirth = Utils.inputBack(f"Data de Nascimento (atual: {account.birth}): ")
            if not newBirth.strip():
                newBirth = account.birth
            newEmail = Utils.inputBack(f"Email (atual: {account.email}): ") if hasattr(account, 'email') else None
            if newEmail is not None and not newEmail.strip():
                newEmail = account.email

            if isinstance(account, Producer):
                newCnpj = Utils.inputBack(f"CNPJ (atual: {account.cnpj}): ")
                if not newCnpj.strip():
                    newCnpj = account.cnpj
                newEnterprise = Utils.inputBack(f"Empresa (atual: {account.enterprise}): ")
                if not newEnterprise.strip():
                    newEnterprise = account.enterprise
                try:
                    account.updateProfile(name=newName, birth=newBirth, email=newEmail, cnpj=newCnpj, enterprise=newEnterprise)
                    print("Conta atualizada com sucesso!")
                except Exception as e:
                    print(f"Erro ao atualizar conta: {e}")
            else:
                try:
                    if newEmail is not None:
                        account.updateProfile(name=newName, birth=newBirth, email=newEmail)
                    else:
                        account.updateProfile(name=newName, birth=newBirth)
                    print("Conta atualizada com sucesso!")
                except Exception as e:
                    print(f"Erro ao atualizar conta: {e}")
            Utils.pause()
        elif option == "2":
            confirm = Utils.inputBack("Tem certeza que deseja excluir a conta? (s/n): ")
            if confirm.lower() == 's':
                if account.deleteAccount():
                    print("Conta excluída com sucesso!")
                    Utils.pause()
                    break
                else:
                    print("Erro ao excluir conta.")
                    Utils.pause()
            else:
                print("Exclusão cancelada.")
                Utils.pause()
        elif option == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            Utils.pause()