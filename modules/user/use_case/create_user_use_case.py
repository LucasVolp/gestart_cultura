from models.models import User
from modules.user.dto import CreateUserDTO
from modules.user.repository import CreateUserRepository, FindUserByEmailRepository, FindUserByCpfRepository, FindUserByPhoneRepository
from fastapi import HTTPException
from passlib.hash import bcrypt

class CreateUserUseCase:
    def __init__(self, userRepository=None, findUserByEmail=None, findUserByCpf=None, findUserByPhone=None):
        self.repository = userRepository or CreateUserRepository()
        self.findUserByEmail = findUserByEmail or FindUserByEmailRepository()
        self.findUserByCpf = findUserByCpf or FindUserByCpfRepository()
        self.findUserByPhone = findUserByPhone or FindUserByPhoneRepository()

    def execute(self, data: CreateUserDTO) -> User:
        """        Executes the use case to create a new user.

        Args:
            data (CreateUserDTO): Data Transfer Object containing the user information to be created.

        Raises:
            ValueError: If a user with the same email or CPF already exists.
            ValueError: If there is an error during the creation process.
            e: If any other error occurs during the creation process.

        Returns:
            User: Created User model instance.
        """
        try:
            userEmail = self.findUserByEmail.findByEmail(data.email)
            userCPF = self.findUserByCpf.findByCPF(data.cpf)
            userPhone = self.findUserByPhone.findUserByPhone(data.phone)
            if userEmail:
                raise HTTPException(status_code=400, detail="Usuário com este email já cadastrado.")
            if userCPF:
                raise HTTPException(status_code=400, detail="Usuário com este CPF já cadastrado.")
            if userPhone:
                raise HTTPException(status_code=400, detail="Usuário com este telefone já cadastrado.")
            data.password = bcrypt.hash(data.password)
            user = self.repository.create(data)
            print(f"Usuário {user.name} criado com sucesso.")
            return user
        except HTTPException as e:
            print(f"Erro ao criar usuário: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            raise HTTPException(status_code=500, detail="Erro ao criar usuário.")
        finally:
            self.repository.session.close()