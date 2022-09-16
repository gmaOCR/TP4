from modules.Models import Tournament
from modules.View import Menus

class TournamentManager:

    def get_info(self):
        menu = Menus()
        """Déclare l'objet "Menus" """
        menu.hello()
        """Message de bienvenue"""
        choice = menu.select_menu(menu.main_menu())
        """Menu principal"""
        while choice not in ["1","2","3","4"]:
            print("\n Choix incorrect\n")
            choice = menu.select_menu(menu.main_menu())
        if choice == "1":
            """ Créer un tournoi"""
            tournament_input = menu.create_tournament("Entrez le nom du tournoi:")
           # tournament = Tournament()
        elif choice == "2":
            """ Ajouter des joueurs à la database"""
            pass
        elif choice == "3":
            """ Consulter des informations """
            pass
        elif choice == "4":
            """ Quitter le programme """
            exit

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


