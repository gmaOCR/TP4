from tinydb import TinyDB

import modules.View
from modules.View import Menus
from modules.TournamentManager import TournamentManager
from modules.PlayerManager import PlayerManager
from modules.RoundManager import RoundManager
from modules.MatchManager import MatchManager

TIME_CONTROL = modules.View.TIME_CONTROL
"""Liste des types de chronomètres standardisés"""

db = TinyDB("db.json")
players_table = db.table("players")
tournaments_table = db.table("tournaments")
match_table = db.table("matchs")
""" Déclaration de la base de données et des tables """

menu = Menus()
"""Déclare l'objet "Menus" from View.py """
tm = TournamentManager()
"""Déclare l'objet "Tournament Manager" from TournamentManager.py """
pm = PlayerManager()
"""Déclare l'objet "PlayerManager" from PlayerManager.py """
rm = RoundManager()
"""Déclare l'objet "Roundmanager" from Roundmanager.py """
mm = MatchManager()
"""Déclare l'objet "Matchmanager" from matchmanager.py """


class MainManager:

    def start(self):
        "Lance le menu de départ"
        """Message de bienvenue"""
        menu.hello()
        """Menu principal"""
        choice = menu.get_input(menu.main_menu())
        while choice != "9":
            while choice not in ["1", "2", "3", "4", "5", "9"]:
                print("\n Choix incorrect !\n")
                choice = menu.get_input(menu.main_menu())
            if choice == "1":
                """instancie et affiche un tournoi"""
                tournament = tm.create_tournament()
                menu.display_tournament(tournament)
                """instancie et affiche une liste de 8 joueurs instanciés triée par rang"""
                players_list = tm.select_8_players(players_table)
                """ Instancie le round N° 1"""
                r_input = menu.get_input("Saisir le numéro du round")
                round = rm.create_round(tournament, r_input)
                """Ajoute le round 1 à la liste de round du tournoi"""
                tournament.round_list.append(round)
                """Génère la liste des 4 match du Round 1"""
                match_list = mm.create_matches_first_round( players_list)
                """Run les 4 matchs du Round 1"""
                match_list_result = mm.run_match(match_list)
                """Ajoute la liste des match avec resultats au round 1"""
                round_1.match_list = match_list_result
                """"Cloture le round 1 par ajout de l'heure de fin"""
                menu.get_input("Valider la fin du round en cours ? O/N")
                round_1.end_time = rm.timestamp()



                choice = menu.get_input(menu.main_menu())
            elif choice == "2":
                self.menu_show_players()
                choice = menu.get_input(menu.main_menu())
            elif choice == "3":
                self.menu_add_data_to_db(choice)
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

    def menu_add_data_to_db(self, choice):
        """ Ajoute des joueurs à la database"""
        while choice in ["O", "o", "3"]:
            if choice == "O" or "o" or "3":
                player = pm.create_player_to_db()
                menu.display_player(player)
                choice = menu.get_input(menu="Verifier la saisie, ajouter à la base ? (O/N)")
                if choice in ["O", "o"]:
                    serialized_player = pm.serialize_player(player)
                    self.add_data_to_db(serialized_player, players_table)
                    print("\nJoueur ajouté avec succès !\n")
                else:
                    print("\nRetour au menu principal\n")
            if choice in ["N", "n"]:
                print("\nRetour au menu principal\n")
            choice = menu.get_input("Ajouter un autre joueur ? (O/N)\n")
            print("\nRetour au menu principal\n")

    @staticmethod
    def menu_show_players():
        """Liste les joueurs depuis la DB"""
        return menu.display_players_from_db(pm.unserialize_all_players(players_table))

    @staticmethod
    def clear_player_table():
        players_table.truncate()  # clear the table
        return print("\nTable Players effacée !\n")

    @staticmethod
    def add_data_to_db(serialized_data, table):
        return table.insert(serialized_data)