from menus.menuProducer import menuProducer
from menus.menuSeller import sellerMenu
from menus.userMenu import userMenu
from getpass import getpass
from models.producer import Producer
from models.seller import Seller
from models.user import User
from services.authService import AuthService
from services.createAccountService import CreateAccountService
from flows.utils import MenuBackException, Utils
from seeders import seed_data

def main():
    auth_service = AuthService()
    createAccountService = CreateAccountService()
    while True:
        Utils.menu("Bem vindo ao Gestart Cultura")
        print("Escolha uma opção:")
        print("1. Fazer Login")
        print("2. Criar Conta")
        print("0. Sair")
        option = input()
        match option:
            case "1":
                while True:
                    try:
                        Utils.menu("Fazer Login - ou digite 0 para voltar")
                        try:
                            email = Utils.inputEmail()
                        except MenuBackException:
                            break
                        password = getpass("Digite sua senha: ", stream=None)
                        account = auth_service.authenticar(email, password)
                        if account:
                            print(f"Bem-vindo, {account.name}!")
                            if isinstance(account, Producer):
                                try:
                                    menuProducer(account)
                                except KeyboardInterrupt:
                                    pass
                            elif isinstance(account, User):
                                try:
                                    userMenu(account)
                                except KeyboardInterrupt:
                                    pass
                            elif isinstance(account, Seller):
                                try:
                                    sellerMenu(account)
                                except KeyboardInterrupt:
                                    pass
                        else:
                            print("Email ou senha incorretos.")
                        Utils.pause()
                        continue
                    except KeyboardInterrupt:
                        break
            case "2":
                while True:
                    try:
                        Utils.menu("Criar Conta - ou digite 0 para voltar")
                        accountType = Utils.accountTypes()
                        name = Utils.inputBack("Digite seu nome: ")
                        if not name.strip():
                            print("Nome não pode ser vazio.")
                            Utils.pause()
                            continue

                        email = Utils.inputEmail()
                        cpf = Utils.inputCPF()
                        phone = Utils.inputPhone()
                        birth = Utils.inputBirth("Digite sua data de nascimento (DD/MM/AAAA): ")
                        password = Utils.inputPassword("Digite sua senha (ou 0 para voltar): ")

                        if accountType == "producer":
                            cnpj = Utils.inputCNPJ()
                            enterprise = Utils.inputBack("Digite o nome da sua empresa: ")
                            if not enterprise.strip():
                                print("Nome da empresa não pode ser vazio.")
                                Utils.pause()
                                continue
                            account = createAccountService.createAccount(accountType, name, cpf, birth, email, password, phone, cnpj, enterprise)
                        else:
                            account = createAccountService.createAccount(accountType, name, cpf, birth, email, password, phone)

                        if account:
                            print("Conta criada com sucesso!")
                        Utils.pause()
                        break
                    except MenuBackException:
                        break
                    except Exception as e:
                        print(f"Erro: {e}")
                        Utils.pause()
                        continue
            case "0":
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                Utils.pause()

if __name__ == "__main__":
    main()