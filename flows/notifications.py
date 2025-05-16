from flows.utils import Utils

def notifications(account):
    while True:
        Utils.menu("Notificações")
        print("1. Enviar notificação agora")
        print("2. Agendar notificação")
        print("0. Voltar")
        option = Utils.inputBack("Escolha uma opção: ")
        if option == "1":
            recipient = Utils.inputEmail("Digite o email do destinatário: ")
            message = Utils.inputBack("Digite a mensagem: ")
            try:
                account.sendNotification(recipient, message)
                print("Notificação enviada com sucesso!")
            except Exception as e:
                print(f"Erro ao enviar notificação: {e}")
            Utils.pause()
        elif option == "2":
            recipient = Utils.inputEmail("Digite o email do destinatário: ")
            message = Utils.inputBack("Digite a mensagem: ")
            date = Utils.inputDate("Digite a data de agendamento (DD/MM/AAAA): ")
            try:
                account.scheduleNotification(recipient, message, date)
                print("Notificação agendada com sucesso!")
            except Exception as e:
                print(f"Erro ao agendar notificação: {e}")
            Utils.pause()
        elif option == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            Utils.pause()
