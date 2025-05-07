from models.user import User
from models.seller import Seller
from models.producer import Producer
from uuid import UUID, uuid4

def create_user():
    print("\n-- Criar Usuário --")
    name = input("Nome: ")
    cpf = input("CPF: ") 
    birth = input("Data de nascimento (AAAA-MM-DD): ")
    email = input("Email: ")
    password = input("Senha: ")
    phone = input("Telefone: ")
    status = "ativo"

    usuario = User(uuid4(), name, cpf, birth, email, password, phone, status)
    print("Usuário criado com sucesso!")
    return usuario

def create_seller():
    print("\n-- Criar Vendedor --")
    name = input("Nome: ")
    cpf = input("CPF: ") 
    birth = input("Data de nascimento (AAAA-MM-DD): ")
    email = input("Email: ")
    password = input("Senha: ")
    phone = input("Telefone: ")
    status = "ativo"

    vendedor = Seller(uuid4(), name, cpf, birth, email, password, phone, status)
    print("Vendedor criado com sucesso!")
    return vendedor

def create_productor():
    print("\n-- Criar Produtor Cultural --")
    name = input("Nome: ")
    cpf = input("CPF: ") 
    birth = input("Data de nascimento (AAAA-MM-DD): ")
    email = input("Email: ")
    password = input("Senha: ")
    phone = input("Telefone: ")
    status = "ativo"
    cnpj = input("CNPJ: ")
    enterprise = input("Nome da Empresa: ")

    produtor = Producer(uuid4(), name, cpf, birth, email, password, phone, status, cnpj, enterprise)
    print("Produtor criado com sucesso!")
    return produtor



