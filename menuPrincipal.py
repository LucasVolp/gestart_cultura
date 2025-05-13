from interacao import create_user, create_seller, create_productor
from flows.create_event_and_tier_flow import run_create_event_and_tier_flow
from models.producer import Producer

def main():
    pessoas = []

    while True:
        print("\n== MENU PRINCIPAL ==")
        print("1 - Criar Usuário")
        print("2 - Criar Vendedor")
        print("3 - Criar Produtor")
        print("4 - Listar Pessoas Cadastradas")
        print("5 - Criar Evento e Lote (somente produtor)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            user = create_user()
            pessoas.append(user)

        elif opcao == "2":
            seller = create_seller()
            pessoas.append(seller)

        elif opcao == "3":
            producer = create_productor()
            pessoas.append(producer)

        elif opcao == "4":
            print("\n-- Pessoas Cadastradas --")
            if not pessoas:
                print("Nenhuma pessoa cadastrada.")
            else:
                for p in pessoas:
                    print(p)

        elif opcao == "5":
            if not pessoas:
                print("Nenhuma pessoa cadastrada.")
                continue

            print("\n-- Selecione um produtor pelo CPF --")
            cpf_input = input("Digite o CPF: ")
            produtor = next((p for p in pessoas if isinstance(p, Producer) and p._cpf == cpf_input), None)

            if produtor:
                run_create_event_and_tier_flow(produtor)
            else:
                print("Produtor não encontrado com esse CPF.")

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()