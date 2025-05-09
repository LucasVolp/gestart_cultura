from interacao import create_user 
from interacao import create_seller
from interacao import create_productor

def main():
    pessoas = []

    while True:
        print("\n== Menu ==")
        print("1 - Criar Usuário")
        print("2 - Criar Vendedor")
        print("3 - Criar Produtor")
        print("4 - Listar pessoas")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            user = create_user()
            pessoas.append(user)
        elif opcao == "2":
            seller = create_seller()
            pessoas.append(seller)
        elif opcao == "3":
            productor = create_productor()
            pessoas.append(productor)
        elif opcao == "4":
            print("\n-- Pessoas Cadastradas --")
            for p in pessoas:
                print(p)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
