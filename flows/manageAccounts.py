from datetime import datetime
from getpass import getpass
from flows.utils import Utils, MenuBackException
from models.producer import Producer


def manageAccounts(account):
    while True:
        Utils.menu("Gerenciar Conta")
        print("Escolha uma opção:")
        print("1. Editar Conta")
        print("2. Excluir Conta")
        print("0. Voltar")
        
        try:
            option = Utils.inputBack("Escolha uma opção: ")
            
            if option == "1":
                # Menu de edição de conta
                while True:
                    try:
                        Utils.menu("Editar Conta")
                        print("Digite os novos dados da conta (ou deixe em branco para não alterar):")
                        
                        # Nome
                        newName = Utils.inputBack(f"Nome (atual: {account.name}): ")
                        if not newName.strip():
                            newName = account.name
                            
                        # Data de nascimento
                        while True:
                            try:
                                newBirth = Utils.inputBack(f"Data de Nascimento (atual: {account.birth}): ")
                                if not newBirth.strip():
                                    birthObj = account.birth
                                    break
                                try:
                                    birthObj = datetime.strptime(newBirth, "%d/%m/%Y").date()
                                    break
                                except ValueError:
                                    print("Formato de data inválido. Use DD/MM/AAAA.")
                            except MenuBackException:
                                raise  # Propaga exceção para sair do menu de edição
                                
                        # Email
                        newEmail = None
                        if hasattr(account, 'email'):
                            newEmail = Utils.inputBack(f"Email (atual: {account.email}): ")
                            if not newEmail.strip():
                                newEmail = account.email
                        
                        # Senha
                        newPassword = None
                        while True:
                            try:
                                changePass = Utils.inputBack("Deseja alterar a senha? \n1- Sim \n2- Não: ")
                                if changePass == "1":
                                    while True:
                                        newPassword = getpass("Digite a nova senha: ")
                                        confirmPassword = getpass("Confirme a nova senha: ")
                                        if newPassword == confirmPassword:
                                            break
                                        print("As senhas não coincidem. Tente novamente.")
                                    break
                                elif changePass == "2":
                                    break
                                else:
                                    print("Opção inválida. Digite 1 para Sim ou 2 para Não.")
                            except MenuBackException:
                                raise  # Propaga exceção para sair do menu de edição
                        
                        # Dados específicos para Producer
                        if isinstance(account, Producer):
                            # CNPJ
                            newCnpj = None
                            while True:
                                try:
                                    newCnpj = Utils.inputBack(f"CNPJ (atual: {Utils.formatCNPJ(account.cnpj)}): ")
                                    if not newCnpj.strip():
                                        newCnpj = account.cnpj
                                        break
                                    # Limpa o CNPJ para armazenar apenas dígitos
                                    newCnpj = ''.join(filter(str.isdigit, newCnpj))
                                    if len(newCnpj) == 14:
                                        break
                                    print("CNPJ inválido. Digite 14 dígitos.")
                                except MenuBackException:
                                    raise  # Propaga exceção para sair do menu de edição
                                
                            # Empresa
                            newEnterprise = Utils.inputBack(f"Empresa (atual: {account.enterprise}): ")
                            if not newEnterprise.strip():
                                newEnterprise = account.enterprise
                                
                            # Atualização do perfil para Producer
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
                                break  # Sai do menu de edição
                            except Exception as e:
                                print(f"Erro ao atualizar conta: {e}")
                                Utils.pause()
                                # Continua no menu de edição
                        else:
                            # Atualização para outros tipos de conta
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
                                break  # Sai do menu de edição
                            except Exception as e:
                                print(f"Erro ao atualizar conta: {e}")
                                Utils.pause()
                                # Continua no menu de edição
                    
                    except MenuBackException:
                        break  # Volta ao menu principal
                
            elif option == "2":
                # Menu de exclusão de conta
                while True:
                    try:
                        Utils.menu("Excluir Conta")
                        confirm = Utils.inputBack("Tem certeza que deseja excluir a conta? (s/n): ")
                        
                        if confirm.lower() == 's':
                            try:
                                if account.deleteAccount():
                                    print("Conta excluída com sucesso!")
                                    Utils.pause()
                                    return  # Sai completamente da função
                                else:
                                    print("Erro ao excluir conta.")
                                    Utils.pause()
                                    break  # Volta ao menu principal
                            except Exception as e:
                                print(f"Erro ao excluir conta: {e}")
                                Utils.pause()
                                break  # Volta ao menu principal
                        elif confirm.lower() == 'n':
                            print("Exclusão cancelada.")
                            Utils.pause()
                            break  # Volta ao menu principal
                        else:
                            print("Opção inválida. Digite 's' para sim ou 'n' para não.")
                            Utils.pause()
                            # Continua no menu de exclusão
                    
                    except MenuBackException:
                        break  # Volta ao menu principal
                
            elif option == "0":
                break  # Sai da função
                
            else:
                print("Opção inválida. Tente novamente.")
                Utils.pause()
                # Continua no menu principal
                
        except MenuBackException:
            break  # Volta ao menu anterior