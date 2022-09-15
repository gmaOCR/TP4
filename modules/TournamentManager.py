from Models import Tournament
from PlayerManager import players_list


class TournamentManager:
    
    def __init__(self):
        self.tourmament = Tournament("Tournoi de la rue du Stand", "Genève", "05/09/22", "Blitz", 4, players_list, "" )

    def display_tournament(self):
        return (f"Nom du tournoi: {self.name}\n"
                f"Lieu: {self.place}\n"
                f"Jour:  {self.date}\n"
                f"Nombre de tour: {self.rounds}\n"
                f"Type de chrono: {self.timecontrol}\n"
                f"Joueurs: {self.players_list}\n"
                f"Information complémentaire: {self.description}\n")


    def add_player_tournament(self, player):
        self.players_list.append(player)


tournament = TournamentManager()
tournament.display_tournament()
#tournament.add_player_tournament()
