from repository import AccountRepository
from use_cases import CreateAccountUseCase

def main():
    repo = AccountRepository()
    use_case = CreateAccountUseCase(repo)
    try:
        user = use_case.execute(
            account_type="user",
            name="Fulano",
            cpf="123.456.789-00",
            birth="2000-01-01",
            email="fulano@email.com",
            password="senha123",
            phone="67999999999"
        )
        print("Conta criada com sucesso:", user)
    except ValueError as e:
        print("Erro ao criar conta:", e)

if __name__ == "__main__":
    main()