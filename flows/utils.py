from datetime import datetime
import os
import re
from getpass import getpass

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
    def formatCPF(cpf: str) -> str:
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) == 11:
            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        return cpf

    @staticmethod
    def formatPhone(phone: str) -> str:
        phone = ''.join(filter(str.isdigit, phone))
        if len(phone) == 11:
            return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
        elif len(phone) == 10:
            return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"
        return phone

    @staticmethod
    def formatCNPJ(cnpj: str) -> str:
        cnpj = ''.join(filter(str.isdigit, cnpj))
        if len(cnpj) == 14:
            return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
        return cnpj
    
    @staticmethod
    def inputEmail(msg="Digite seu email: "):
        while True:
            email = Utils.inputBack(msg)
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if re.match(pattern, email):
                return email
            print("Email inválido. Tente novamente.")

    @staticmethod
    def inputCPF(msg="Digite seu CPF (apenas números): "):
        while True:
            cpf = Utils.inputBack(msg)
            cpf_digits = ''.join(filter(str.isdigit, cpf))
            if len(cpf_digits) == 11:
                return cpf_digits
            print("CPF inválido. Digite 11 dígitos.")

    @staticmethod
    def inputPhone(msg="Digite seu telefone (apenas números, com DDD): "):
        while True:
            phone = Utils.inputBack(msg)
            phone_digits = ''.join(filter(str.isdigit, phone))
            if len(phone_digits) == 11 and phone_digits[2] == '9':
                return phone_digits
            elif len(phone_digits) == 10:
                return phone_digits
            print("Telefone inválido. Digite 10 ou 11 dígitos (com DDD).")

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
    def inputPassword(msg="Digite sua senha (ou 0 para voltar): "):
        """Solicita ao usuário que digite uma senha, com opção de voltar ao menu anterior.
        A senha é mascarada (não exibida) durante a digitação.
        Retorna ao menu anterior se o usuário digitar '0'.
        
        Args:
            msg (str): Mensagem a ser exibida ao solicitar a senha
            
        Returns:
            str: A senha digitada
            
        Raises:
            MenuBackException: Se o usuário digitar '0'
        """
        while True:
            password = getpass(msg)
            if password == "0":
                raise MenuBackException()
            if len(password) >= 6:  # Validação básica de tamanho
                return password
            print("A senha deve ter pelo menos 6 caracteres.")
    
    @staticmethod
    def inputCNPJ(msg="Digite seu CNPJ (apenas números): "):
        while True:
            cnpj = Utils.inputBack(msg)
            cnpj_digits = ''.join(filter(str.isdigit, cnpj))
            if len(cnpj_digits) == 14:
                return cnpj_digits
            print("CNPJ inválido. Digite 14 dígitos.")