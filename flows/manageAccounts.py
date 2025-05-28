from datetime import datetime
from getpass import getpass
from flows.utils import Utils, MenuBackException
from models.producer import Producer


def manageAccounts(account):
    while True:
        try:
            Utils.menu("Gerenciar Conta")
            print("Escolha uma opção:")
            print("1. Editar Conta")
            print("2. Excluir Conta")
            print("0. Voltar")
            option = Utils.inputBack("Escolha uma opção: ")

            if option == "1":
                try:
                    Utils.menu("Editar Conta")
                    print("Digite os novos dados da conta (ou deixe em branco para não alterar):")

                    newName = Utils.inputBack(f"Nome (atual: {account.name}): ")
                    if not newName.strip():
                        newName = account.name

                    newBirth = Utils.inputBack(f"Data de Nascimento (atual: {account.birth}): ")
                    if not newBirth.strip():
                        birthObj = account.birth
                    else:
                        try:
                            birthObj = datetime.strptime(newBirth, "%d/%m/%Y").date()
                        except ValueError:
                            print("Formato de data inválido. Use DD/MM/AAAA.")
                            Utils.pause()
                            continue

                    newEmail = None
                    if hasattr(account, 'email'):
                        newEmail = Utils.inputBack(f"Email (atual: {account.email}): ")
                        if not newEmail.strip():
                            newEmail = account.email

                    newPassword = None
                    changePass = Utils.inputBack("Deseja alterar a senha? \n1- Sim \n2- Não: ")
                    if changePass == "1":
                        while True:
                            newPassword = getpass("Digite a nova senha: ")
                            confirmPassword = getpass("Confirme a nova senha: ")
                            if newPassword == confirmPassword:
                                break
                            print("As senhas não coincidem. Tente novamente.")

                    if isinstance(account, Producer):
                        newCnpj = Utils.inputBack(f"CNPJ (atual: {Utils.formatCNPJ(account.cnpj)}): ")
                        if not newCnpj.strip():
                            newCnpj = account.cnpj
                        else:
                            newCnpj = ''.join(filter(str.isdigit, newCnpj))
                            if len(newCnpj) != 14:
                                print("CNPJ inválido. Digite 14 dígitos.")
                                Utils.pause()
                                continue
                        newEnterprise = Utils.inputBack(f"Empresa (atual: {account.enterprise}): ")
                        if not newEnterprise.strip():
                            newEnterprise = account.enterprise
                        try:
                            account.updateProfile(
                                name=newName,
                                birth=birthObj,
                                email=newEmail,
                                cnpj=newCnpj,
                                enterprise=newEnterprise,
                                password=newPassword if changePass == "1" else None
                            )
                            print("Conta atualizada com sucesso!")
                            Utils.pause()
                        except Exception as e:
                            print(f"Erro ao atualizar conta: {e}")
                            Utils.pause()
                        continue
                    try:
                        result = account.updateProfile(
                            name=newName,
                            birth=birthObj,
                            email=newEmail,
                            password=newPassword if changePass == "1" else None
                        )
                        if result:
                            print("Conta atualizada com sucesso!")
                        else:
                            print("Erro ao atualizar conta.")
                        Utils.pause()
                    except Exception as e:
                        print(f"Erro ao atualizar conta: {e}")
                        Utils.pause()
                    continue
                except MenuBackException:
                    continue

            elif option == "2":
                try:
                    Utils.menu("Excluir Conta")
                    confirm = Utils.inputBack("Tem certeza que deseja excluir a conta? (s/n): ")
                    if confirm.lower() == 's':
                        try:
                            if account.deleteAccount():
                                print("Conta excluída com sucesso!")
                                Utils.pause()
                                return
                            else:
                                print("Erro ao excluir conta.")
                                Utils.pause()
                        except Exception as e:
                            print(f"Erro ao excluir conta: {e}")
                            Utils.pause()
                    elif confirm.lower() == 'n':
                        print("Exclusão cancelada.")
                        Utils.pause()
                    else:
                        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
                        Utils.pause()
                    continue
                except MenuBackException:
                    continue

            elif option == "0":
                break

            else:
                print("Opção inválida. Tente novamente.")
                Utils.pause()
                continue

        except MenuBackException:
            break