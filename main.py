from services.auth_service import AuthService
from services.create_account_service import CreateAccountService
from flows.utils import Utils

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
                    email = Utils.input_email()
                    password = Utils.inputBack("Digite sua senha")
                    account = auth_service.authenticar(email, password)
                    if account:
                        print(f"Bem-vindo, {account.name}!")
                    else:
                        print("Email ou senha incorretos.")
                    Utils.pause()
                except KeyboardInterrupt:
                    continue
            case "2":
                try:
                    Utils.menu("Criar Conta - ou digite 0 para voltar")
                    account_type = Utils.accountTypes()
                    name = Utils.inputBack("Digite seu nome")
                    email = Utils.input_email()
                    cpf = Utils.input_cpf()
                    phone = Utils.input_phone()
                    birth = Utils.input_date("Digite sua data de nascimento (DD/MM/AAAA): ")
                    password = Utils.input_password()

                    if account_type == "producer":
                        cnpj = Utils.input_cnpj()
                        enterprise = Utils.inputBack("Digite o nome da sua empresa")
                        account = create_account_service.createAccount(account_type, name, cpf, birth, email, password, phone, cnpj, enterprise)
                    
                    account = create_account_service.createAccount(account_type, name, cpf, birth, email, password, phone)
                    
                    if account:
                        print("Conta criada com sucesso!")
                    else:
                        print("Erro ao criar conta.")
                    Utils.pause()
                except KeyboardInterrupt:
                    continue
            case "0":
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                Utils.pause()

if __name__ == "__main__":
    main()