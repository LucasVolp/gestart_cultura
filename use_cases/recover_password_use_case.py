from repository import FindAccountRepository

class RecoverPasswordUseCase:
    def __init__(self, repository: FindAccountRepository):
        self.repository = repository

    def execute(self, email: str, identifier: str, account_type: str = None) -> bool:
        account = self.repository.find_account(email, identifier, account_type)
        if not account:
            raise ValueError("Conta não encontrada para o email e identificador fornecidos.")
        success = account.recoverPassword(email, identifier)
        if success:
            recipient = account.phone if hasattr(account, "phone") else email
            account.sendNotification(recipient, "Um link de recuperação de senha foi enviado para você.")
        return success