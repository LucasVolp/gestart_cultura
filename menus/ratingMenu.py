from flows.utils import Utils
from models.event import Event

def showRatings(user):
    try:
        ratings = user.getRatings()
        if not ratings:
            print("Nenhuma avaliação encontrada.")
        else:
            print("Suas avaliações:")
            for idx, rating in enumerate(ratings, start=1):
                print(f"{idx} - Evento: {rating.event.name} | Nota: {rating.rate} | Comentário: {rating.comment}")
        Utils.pause()
    except Exception as e:
        print(f"Erro ao listar avaliações: {e}")
        Utils.pause()

def createRatingMenu(user):
    try:
        from models.event import Event
        events = [event for event in Event.events if event.status.name == "CLOSED"]
        if not events:
            print("Nenhum evento encerrado disponível para avaliação.")
            Utils.pause()
            return
        print("Eventos encerrados disponíveis para avaliação:")
        for idx, event in enumerate(events, start=1):
            print(f"{idx} - {event.name}")
        try:
            eventIndex = int(Utils.inputBack("Escolha o número do evento: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if eventIndex < 0 or eventIndex >= len(events):
            print("Evento inválido.")
            Utils.pause()
            return
        event = events[eventIndex]
        try:
            rate = int(Utils.inputBack("Dê uma nota de 0 a 5: "))
        except ValueError:
            print("Nota inválida.")
            Utils.pause()
            return
        comment = Utils.inputBack("Deixe um comentário: ")
        rating = user.createRating(event, rate, comment)
        if rating:
            print(f"Avaliação criada com sucesso para o evento {event.name}!")
        else:
            print("Não foi possível criar a avaliação.")
        Utils.pause()
    except Exception as e:
        print(f"Erro ao criar avaliação: {e}")
        Utils.pause()

def deleteRatingMenu(user):
    try:
        ratings = user.getRatings()
        if not ratings:
            print("Nenhuma avaliação encontrada.")
            Utils.pause()
            return
        print("Escolha uma avaliação para deletar:")
        for idx, rating in enumerate(ratings, start=1):
            print(f"{idx} - Evento: {rating.event.name} | Nota: {rating.rate} | Comentário: {rating.comment}")
        try:
            ratingIndex = int(Utils.inputBack("Escolha o número da avaliação: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if ratingIndex < 0 or ratingIndex >= len(ratings):
            print("Avaliação inválida.")
            Utils.pause()
            return
        rating = ratings[ratingIndex]
        user.deleteRating(rating)
        print("Avaliação deletada com sucesso!")
        Utils.pause()
    except Exception as e:
        print(f"Erro ao deletar avaliação: {e}")
        Utils.pause()

def editRatingMenu(user):
    try:
        ratings = user.getRatings()
        if not ratings:
            print("Nenhuma avaliação encontrada.")
            Utils.pause()
            return
        print("Escolha uma avaliação para editar:")
        for idx, rating in enumerate(ratings, start=1):
            print(f"{idx} - Evento: {rating.event.name} | Nota: {rating.rate} | Comentário: {rating.comment}")
        try:
            ratingIndex = int(Utils.inputBack("Escolha o número da avaliação: ")) - 1
        except ValueError:
            print("Entrada inválida. Digite um número.")
            Utils.pause()
            return
        if ratingIndex < 0 or ratingIndex >= len(ratings):
            print("Avaliação inválida.")
            Utils.pause()
            return
        rating = ratings[ratingIndex]
        try:
            newRate = int(Utils.inputBack(f"Nova nota (0-5, atual: {rating.rate}): "))
        except ValueError:
            print("Nota inválida.")
            Utils.pause()
            return
        newComment = Utils.inputBack(f"Novo comentário (atual: {rating.comment}): ")
        user.updateRating(rating, newRate, newComment)
        print("Avaliação atualizada com sucesso!")
        Utils.pause()
    except Exception as e:
        print(f"Erro ao editar avaliação: {e}")
        Utils.pause()

def ratingMenu(user):
    while True:
        try:
            Utils.menu(f"Menu de Avaliações - {user.name}")
            print("\nEscolha uma opção:")
            print("1. Minhas Avaliações")
            print("2. Avaliar Eventos")
            print("3. Deletar avaliação")
            print("4. Editar avaliação")
            print("0. Voltar")
            option = input()
            match option:
                case "1":
                    showRatings(user)
                case "2":
                    createRatingMenu(user)
                case "3":
                    deleteRatingMenu(user)
                case "4":
                    editRatingMenu(user)
                case "0":
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    Utils.pause()
        except Exception as e:
            print(f"Erro inesperado: {e}")
            Utils.pause()
