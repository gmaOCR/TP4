from tinydb import TinyDB
# import os
# import sys
# sys.path.append(os.getcwd())
import modules.View
from .Models import Tournament
from modules.View import Menus
from modules.PlayerManager import PlayerManager
from modules.RoundManager import RoundManager
from modules.MatchManager import MatchManager

TIME_CONTROL = modules.View.TIME_CONTROL
"""Liste des types de chronomètres standardisés"""

db = TinyDB("db.json")
players_table = db.table("players")
tournaments_table = db.table("tournaments")
""" Déclaration de la base de données et des tables """

menu = Menus()
"""Déclare l'objet "Menus" from View.py """
pm = PlayerManager()
"""Déclare l'objet "PlayerManager" from PlayerManager.py """
rm = RoundManager()
"""Déclare l'objet "Roundmanager" from Roundmanager.py """
mm = MatchManager()
"""Déclare l'objet "Matchmanager" from matchmanager.py """


class TournamentManager:

    def start(self):
        "Lance le menu de départ"
        """Message de bienvenue"""
        menu.hello()
        """Menu principal"""
        choice = menu.get_input(menu.main_menu())
        while choice != "9":
            while choice not in ["1", "2", "3", "4", "5"]:
                print("\n Choix incorrect\n")
                choice = menu.get_input(menu.main_menu())
            if choice == "1":
                """instancie et affiche un tournoi"""
                tournament = self.create_tournament()
                menu.display_tournament(tournament)
                """instancie et affiche une liste de 8 joueurs instanciés triée par rang"""
                players_list = self.select_8_players()
                #for i in players_list:
                #    menu.display_player(i)
                round_1 = rm.create_first_round(tournament)
                #menu.display_round(round_1, tournament)
                match_list = mm.create_matches_first_round(round_1, players_list)
                for i in match_list:
                    menu.display_match_without_results(i, tournament)
                    mm.run_match(i)
                    menu.get_result(input("Saisissez le résultat du match: A, B ou (N)ul"))
                #menu.get_input(menu="Verifier la saisie, saisie correcte ? (O/N)")
                choice = menu.get_input(menu.main_menu())
            elif choice == "2":
                self.menu_show_players()
                choice = menu.get_input(menu.main_menu())
            elif choice == "3":
                self.menu_add_players_to_db(choice)
                choice = menu.get_input(menu.main_menu())
            elif choice == "4":
                """ Consulter des informations """
                choice = menu.get_input(menu.main_menu())
                pass
            elif choice == "5":
                self.clear_player_table()
                choice = menu.get_input(menu.main_menu())
        """ Quitter le programme """
        exit("Fin")

    def menu_add_players_to_db(self, choice):
        """ Ajoute des joueurs à la database"""
        while choice in ["O", "o", "3"]:
            if choice == "O" or "o" or "3":
                player = pm.create_player_to_db()
                menu.display_player(player)
                choice = menu.get_input(menu="Verifier la saisie, ajouter à la base ? (O/N)")
                if choice in ["O", "o"]:
                    serialized_player = pm.serialize_player(player)
                    pm.add_player_to_db(serialized_player, players_table)
                    print("\nJoueur ajouté avec succès !\n")
                else:
                    print("\nRetour au menu principal\n")
            if choice in ["N", "n"]:
                print("\nRetour au menu principal\n")
            choice = menu.get_input("Ajouter un autre joueur ? (O/N)\n")
            print("\nRetour au menu principal\n")

    def select_8_players(self):
        """ Fais choisir 8 joueurs à l'opérateur depuis la DB """
        """" Génère la liste des joueurs présent en DB"""
        players_list_full = pm.unserialize_all_players(players_table)
        players_list = []
        all_player_available = players_list_full
        i = 0
        """" Boucle selectionnant 8 joueurs par choix opérateur"""
        while i < 8:
            i = i + 1
            menu.display_players_from_db(all_player_available)
            choice = menu.get_input("\n Choisir le joueur " + str(i) + ": (saisir le numéro de ligne): \n")
            players_list.append(pm.create_player_from_db(all_player_available[int(choice)]))
            del all_player_available[int(choice)]
        """Tri la liste des instances de joueurs par rang"""
        players_list_per_rank = pm.sort_players_per_rank(players_list)
        return players_list_per_rank

    def create_tournament(self):
        "Instancie un tournoi"
        t_name = menu.get_input("Entrez le nom du tournoi:")
        t_place = menu.get_input("Entrez le lieu du tournoi:")
        t_date = menu.get_input("Entrez la date du tournoi: (JJ/MM/AAAA)")
        t_rounds = menu.get_input("Entrez le nombre de rondes: (défaut 4)")
        self.input_round_checker(t_rounds)
        t_time_control = menu.tc_menu("Sélectionner le chiffre du type de chronométrage:\n")
        t_desc = menu.get_input("Entrez un commentaire (facultatif):")
        tournament = Tournament(t_name, t_place, t_date, t_time_control, t_rounds, t_desc)
        return tournament
    @staticmethod
    def menu_show_players():
        """Liste les joueurs depuis la DB"""
        return menu.display_players_from_db(pm.unserialize_all_players(players_table))

    @staticmethod
    def clear_player_table():
        players_table.truncate()  # clear the table
        return print("\nTable Players effacée !\n")

    @staticmethod
    def input_round_checker(choice):
        if choice == "":
            return 4
        elif choice.isnumeric() is False:
            while choice.isnumeric() is False:
                print("La saisie doit être un nombre entier")
                try:
                    choice = menu.get_input("")
                except ValueError:
                    print("Erreur: la saisie doit être un nombre entier")
        elif choice.isnumeric() is True:
            return choice
        else:
            return "Contactez l'administrateur"
