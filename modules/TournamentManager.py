from Models import Tournament
from PlayerManager import players_list


def display_tournament(self):
    return (f"Nom du tournoi: {self.name}\n"
            f"Lieur: {self.place}\n"
            f"Jour:  {self.date}\n"
            f"Nombre de tour: {self.rounds}\n"
            f"Type de chrono: {self.timecontrol}\n"
            f"Joueurs: {self.player_list}\n"
            f"Information complémentaire: {self.description}\n")


def add_player_tournament(self, player):
    self.player_list.append(player)


tournament = Tournament("Tournoi de la rue du Stand", "Genève", "05/09/22", "Blitz", 4, players_list, "" )
print(tournament.display_tournament())
