from datetime import datetime
import os
import re

from enums.status import Status
from enums.typeEvent import TypeEvent
from models.person import Person

class MenuBackException(Exception):
    pass

class Utils:

    @staticmethod
    def menu(msg):
        Utils.clearScreen()
        print("="*30)
        print(f"{msg}")
        print("="*30)

    @staticmethod
    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def inputBack(msg):
        value = input(f"{msg}")
        if value == "0":
            raise MenuBackException
        return value

    @staticmethod
    def pause():
        input("\nPressione Enter para continuar...")

    @staticmethod
    def accountTypes():
        accountType = [
            ("Usuário", "user"),
            ("Vendedor", "seller"),
            ("Produtor", "producer")
        ]
        print("Selecione o tipo de conta:")
        for idx, (name, value) in enumerate(accountType, start=1):
            print(f"{idx} - {name}")
        while True:
            try:
                option = int(Utils.inputBack("Escolha o tipo de conta: "))
                if 1 <= option <= len(accountType):
                    return accountType[option - 1][1]
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")

    @staticmethod
    def statusEnum():
        status = {
            Status.OPEN: "Aberto",
            Status.CLOSED: "Fechado"
        }
        print("Selecione o status do Lote:")
        for idx, (key, value) in enumerate(status.items(), start=1):
            print(f"{idx} - {value}")
        while True:
            try:
                option = int(Utils.inputBack("Escolha o status do Lote: "))
                if 1 <= option <= len(status):
                    return list(status.keys())[option - 1]
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")
    
    @staticmethod
    def typeEvents():
        namesPortuguese = {
            TypeEvent.MUSIC_FESTIVAL: "Festival de Música",
            TypeEvent.ART_EXHIBITION: "Exposição de Arte",
            TypeEvent.THEATER: "Teatro",
            TypeEvent.FILM_FESTIVAL: "Festival de Cinema",
            TypeEvent.HANDICRAFT_FAIR: "Feira de Artesanato",
            TypeEvent.DISCUSSION_CIRCLE: "Roda de Conversa",
            TypeEvent.MUSEUM_EXHIBIT: "Exposição de Museu",
            TypeEvent.FOLKLORE_EVENT: "Evento Folclórico",
            TypeEvent.ONLINE_EVENT: "Evento Online",
            TypeEvent.IN_PERSON_EVENT: "Evento Presencial",
            TypeEvent.FREE_EVENT: "Evento Gratuito"
        }
        print("Selecione o tipo de evento:")
        events = list(TypeEvent)
        for idx, tipo in enumerate(events, start=1):
            print(f"{idx} - {namesPortuguese[tipo]}")
        while True:
            try:
                option = int(Utils.inputBack("Escolha o tipo de evento: "))
                if 1 <= option <= len(events):
                    return events[option - 1]
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")

    @staticmethod
    def inputEmail(msg="Digite seu email: "):
        while True:
            email = Utils.inputBack(msg)
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if re.match(pattern, email):
                return email
            print("Email inválido. Tente novamente.")

    @staticmethod
    def inputCPF(msg="Digite seu CPF (xxx.xxx.xxx-xx): "):
        while True:
            cpf = Utils.inputBack(msg)
            pattern = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
            if re.match(pattern, cpf) and Person.validateCPF(cpf):
                return cpf
            print("CPF inválido. Use o formato xxx.xxx.xxx-xx e um número válido.")

    @staticmethod
    def inputPhone(msg="Digite seu telefone ((xx) 9xxxx-xxxx): "):
        while True:
            phone = Utils.inputBack(msg)
            pattern = r"^\(\d{2}\)\s9\d{4}-\d{4}$"
            if re.match(pattern, phone):
                return phone
            print("Telefone inválido. Use o formato (xx) 9xxxx-xxxx.")

    @staticmethod
    def inputDate(msg="Digite a data (DD/MM/AAAA): "):
        while True:
            dateStr = Utils.inputBack(msg)
            try:
                dateObj = datetime.strptime(dateStr, "%d/%m/%Y").date()
                return dateObj
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")

    @staticmethod
    def inputPassword(msg="Digite sua senha: "):
        while True:
            password = Utils.inputBack(msg)
            if len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password):
                return password
            print("Senha inválida. A senha deve ter pelo menos 8 caracteres, incluindo letras e números.")
    
    @staticmethod
    def inputCNPJ(msg="Digite seu CNPJ (xx.xxx.xxx/xxxx-xx): "):
        while True:
            cnpj = Utils.inputBack(msg)
            pattern = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
            if re.match(pattern, cnpj):
                return cnpj
            print("CNPJ inválido. Use o formato xx.xxx.xxx/xxxx-xx.")