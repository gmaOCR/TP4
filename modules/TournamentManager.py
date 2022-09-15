from modules.Models import Tournament
from modules.View import Menus

class TournamentManager:

    def __init__(self):
        pass

    def get_info(self):
        menu = Menus()
        menu.hello()
        menu.start_menu("1.Créer un tournoi \n"
                       "2.Ajouter des joueurs \n"
                       "3.Consulter des informations \n"
                       "4.Quitter \n")
    def create_tournament(self):
        tournament = Tournament()

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


