from menus.menuProducer import menuProducer
from menus.menuSeller import sellerMenu
from menus.userMenu import userMenu
from models.producer import Producer
from models.seller import Seller
from models.user import User
from services.authService import AuthService
from services.createAccountService import CreateAccountService
from flows.utils import MenuBackException, Utils
from seeders import seed_data

def main():
    auth_service = AuthService()
    create_account_service = CreateAccountService()
    while True:
        Utils.menu("Bem vindo ao Gestart Cultura")
        print("Escolha uma opção:")
        print("1. Fazer Login")
        print("2. Criar Conta")
        print("0. Sair")
        option = input()
        match option:
            case "1":
                try:
                    Utils.menu("Fazer Login - ou digite 0 para voltar")
                    try:
                        email = Utils.inputEmail()
                    except MenuBackException:
                        continue
                    password = Utils.inputBack("Digite sua senha: ")
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
                except KeyboardInterrupt:
                    pass
            case "2":
                try:
                    Utils.menu("Criar Conta - ou digite 0 para voltar")
                    account_type = Utils.accountTypes()
                    name = Utils.inputBack("Digite seu nome: ")
                    email = Utils.inputEmail()
                    cpf = Utils.inputCPF()
                    phone = Utils.inputPhone()
                    birth = Utils.inputDate("Digite sua data de nascimento (DD/MM/AAAA): ")
                    password = Utils.inputPassword()

                    if account_type == "producer":
                        cnpj = Utils.inputCNPJ()
                        enterprise = Utils.inputBack("Digite o nome da sua empresa: ")
                        account = create_account_service.createAccount(account_type, name, cpf, birth, email, password, phone, cnpj, enterprise)
                    else:
                        account = create_account_service.createAccount(account_type, name, cpf, birth, email, password, phone)
                    
                    if account:
                        print("Conta criada com sucesso!")
                    else:
                        print("Erro ao criar conta.")
                    Utils.pause()
                except KeyboardInterrupt:
                    pass
            case "0":
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                Utils.pause()

if __name__ == "__main__":
    main()