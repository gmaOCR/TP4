from tinydb import TinyDB
import pandas as pd

import modules.View
from modules.MatchManager import MatchManager
from modules.PlayerManager import PlayerManager
from modules.RoundManager import RoundManager
from modules.TournamentManager import TournamentManager
from modules.View import Menus

"""Liste des types de chronomètres standardisés"""
TIME_CONTROL = modules.View.TIME_CONTROL

""" Déclaration de la base de données et des tables """
db = TinyDB("db.json", sort_keys=True, indent=4, separators=(',', ': '))
players_table = db.table("players")
tournaments_table = db.table("tournaments")
rounds_table = db.table('rounds')
match_table = db.table("matchs")

"""Creation de la variable dataset pour les rapports de joueurs"""
players_datas = pd.read_json('db.json')
pd.set_option('display.max_columns', None)

"""Déclare l'objet "Menus" from View.py """
menu = Menus()
"""Déclare l'objet "Tournament Manager" from TournamentManager.py """
tm = TournamentManager()
"""Déclare l'objet "PlayerManager" from PlayerManager.py """
pm = PlayerManager()
"""Déclare l'objet "Roundmanager" from Roundmanager.py """
rm = RoundManager()
"""Déclare l'objet "Matchmanager" from matchmanager.py """
mm = MatchManager()


class MainManager:

    def start(self):
        """Lance le menu de départ"""
        """Message de bienvenue"""
        menu.hello()
        """Menu principal"""
        choice = menu.get_int(menu.display_main_menu())
        while choice != 9:
            while choice not in [1, 2, 3, 9]:
                print("\n Choix incorrect !\n")
                choice = menu.get_int(menu.display_main_menu())
            if choice == 1:
                """instancie et affiche un tournoi"""
                tournament = tm.create_tournament()
                """Affiche et instancie une liste de 8 joueurs instanciés triée par rang"""
                tournament.players_list = tm.select_8_players(players_table)
                """ Instancie les rounds"""
                round_list = rm.create_round(tournament, tournament.rounds)
                """Ajoute les rounds à la liste de round du tournoi"""
                tournament.round_list = round_list
                """Génère la liste des 4 match du 1er Round"""
                match_list = mm.create_matches_first_round(tournament.players_list)
                """Run les 4 matchs du Round """
                match_list_result = mm.run_match(match_list)
                """Ajoute la liste des match avec resultats au round """
                round_list[0].match_list = match_list_result[0]
                """Mets à jour liste des joueurs du tournoi avec score"""
                tournament.players_list = match_list_result[1]
                """"Cloture le round par ajout de l'heure de fin"""
                menu.display_round_validation(menu.get_input("Valider la fin du round en cours ? O/N"))
                round_list[0].end_time = rm.timestamp()
                """Boucle pour les N round suivant le premier"""
                i = 1
                while i < len(round_list):
                    """Ajoute l'heure de debut du round"""
                    round_list[i].start_time = rm.timestamp()
                    """Genere la liste de match des rounds"""
                    match_list = mm.create_matches_next_round(tournament.players_list)
                    """Recupere les resultats des matchs et la nouvelle liste de joueurs avec scores"""
                    match_list_result = mm.run_match(match_list)
                    """Ajouter la liste de match du round en cours"""
                    round_list[i].match_list = match_list_result[0]
                    """Renvoie la liste de joueurs avec scores sur le tournoi"""
                    tournament.players_list = match_list_result[1]
                    menu.display_round_validation(menu.get_input("Valider la fin du round en cours ? O/N"))
                    """Ajoute l'heure de fin du round"""
                    round_list[i].end_time = rm.timestamp()
                    # if i + 1 < len(round_list):
                    #     round_list[i + 1].start_time = rm.timestamp()
                    tournament.round_list = round_list
                    i = i + 1
                """Affiche le gagnant du tournoi"""
                menu.display_winner(tournament.players_list)
                """Ajoute le tournoi terminé à la table tournament"""
                self.add_data_to_db(tm.serialize_tournament_dev(tournament, tournament.round_list, tournament.players_list)
                                    ,tournaments_table)
                # self.add_data_to_db(tm.serialize_tournament(tournament, round_list, match_list, tournament.players_list)
                #                     ,tournaments_table)
                choice = menu.get_int(menu.display_main_menu())
            elif choice == 2:
                self.menu_add_players_to_db()
                choice = menu.get_int(menu.display_main_menu())
            elif choice == 3:
                """ Menu: Consulter des informations """
                """Affiche les choix disponibles de consultation"""
                selection = menu.get_int(menu.display_main_reports_menu())
                menu.display_reports_menus(selection, players_datas, tm.unserialize_all_tournaments(tournaments_table))
                choice = menu.get_int(menu.display_main_menu())
            elif choice == 9:
                exit("Fin")
        """ Quitter le programme """
        exit("Fin")

    def menu_add_players_to_db(self):
        """ Ajoute des joueurs à la database"""
        choice = True
        while choice is True:
            player = pm.create_player_to_db()
            menu.display_player(player)
            choice = menu.yes_or_no("Verifier la saisie, ajouter à la base ?")
            if choice is True:
                serialized_player = pm.serialize_player(player)
                self.add_data_to_db(serialized_player, players_table)
                print("\nJoueur ajouté avec succès !\n")
                choice = menu.yes_or_no("Ajouter un autre joueur ?")
                if choice is False:
                    break
            elif choice is False:
                choice = menu.yes_or_no("Ajouter un autre joueur ?")
                if choice is False:
                    break
        else:
            print("\nRetour au menu principal\n")


    @staticmethod
    def add_data_to_db(serialized_data, table):
        return table.insert(serialized_data)
