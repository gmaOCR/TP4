
from tinydb import TinyDB, where
import pandas as pd

from modules.MatchManager import MatchManager
from modules.PlayerManager import PlayerManager
from modules.RoundManager import RoundManager
from modules.TournamentManager import TournamentManager
from modules.View import Menus

""" Déclaration de la base de données et des tables """
db = TinyDB("db.json", sort_keys=True, indent=4, separators=(',', ': '))
players_table = db.table("players")
tournaments_table = db.table("tournaments")

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
            while choice not in [1, 2, 3, 4, 5, 6, 9]:
                print("\n Choix incorrect !\n")
                choice = menu.get_int(menu.display_main_menu())
            if choice == 1:
                """instancie et affiche un tournoi"""
                tournament = self.create_tournament()
                self.insert_data_to_db(tm.serialize_tournament(tournament), tournaments_table)
                choice = menu.get_int(menu.display_main_menu())
            elif choice == 5:
                """Ajoute 8 joueurs à un tournoi sans joueurs"""
                tournament = self.add_players_to_tournament()
                self.update_tournament_table(tm.serialize_tournament(tournament), tournaments_table)
                choice = menu.get_int(menu.display_main_menu())
            elif choice == 6:
                """Exectuer les matchs d'un round d'un tournoi """
                self.play_specific_round()
                choice = menu.get_int(menu.display_main_menu())
            elif choice == 2:
                pm.menu_add_players_to_db(players_table)
                choice = menu.get_int(menu.display_main_menu())
            elif choice == 3:
                """ Menu: Consulter des informations """
                """Affiche les choix disponibles de consultation"""
                selection = menu.get_int(menu.display_main_reports_menu())
                menu.display_reports_menus(selection, players_datas, tm.unserialize_all_tournaments(tournaments_table))
                choice = menu.get_int(menu.display_main_menu())
            elif choice == 4:
                """Génère la liste des joueurs depuis la table des joueurs"""
                p_list = pm.unserialize_all_players_from_db(players_table)
                """"Affiche les joueurs de la liste"""
                menu.display_players_to_select(p_list)
                """Selection un index de joueur de la liste"""
                index_player = menu.get_int("\n\nSaisir le N° du joueur à éditer:")
                """Envoi le joueur au PlayerManager pour édition du rang"""
                player = pm.edit_player_rank(p_list[index_player])
                """Update la table players"""
                players_table.update(player, where("Identifiant unique") == player["Identifiant unique"])
                """"Affiche les joueurs de la nouvelle liste"""
                menu.display_players_to_select(pm.unserialize_all_players_from_db(players_table))
                choice = menu.get_int(menu.display_main_menu())
            elif choice == 9:
                exit("Fin")
        """ Quitter le programme """
        exit("Fin")

    @staticmethod
    def insert_data_to_db(serialized_data, table):
        """Ajoute des données à une table de tinyDB (en unitaire, pas en liste)"""
        return table.insert(serialized_data)

    @staticmethod
    def create_tournament():
        """instancie et affiche un tournoi"""
        tournament = tm.instance_tournament()
        """ Instancie les rounds au tournoi"""
        tournament.round_list = rm.create_round(tournament, tournament.rounds)
        return tournament

    @staticmethod
    def update_tournament_table(serialized_tournament, table):
        """Update des données à une table de tinyDB (en unitaire, pas en liste)"""
        table.update(serialized_tournament, where("Nom du tournoi") == serialized_tournament["Nom du tournoi"])

    @staticmethod
    def add_players_to_tournament():
        """Ajoute 8 joueurs à un tournoi sans joueurs"""
        """Variable des tournois déserialisés"""
        unserialized_tournaments = tm.unserialize_all_tournaments(tournaments_table)
        """Affiche les tournois"""
        menu.display_tournament_from_db_short(unserialized_tournaments)
        """Choisi un tournoi"""
        selection = menu.get_int("Saisissez le numéro du tounoi:")
        """Instancie un tournoi depuis TinyDB"""
        tournament = tm.instance_tournament_from_db(unserialized_tournaments[selection - 1])
        """Controle si la liste de joueurs du tournoi est vide"""
        if tournament.players_list is None:
            """Affiche et instancie une liste de 8 joueurs instanciés triée par rang"""
            tournament.players_list = tm.select_8_players(players_table)
            """Génère la liste des 4 match du 1er Round"""
            tournament.round_list[0].match_list = mm.create_matches_first_round(tournament.players_list)
            return tournament
        else:
            """La liste de joueur n'est pas vide"""
            menu.players_list_not_empty()
            return tournament

    def play_specific_round(self):
        """Jouer les 4 match d'un round spécifique"""
        """Variable des tournois déserialisés"""
        unserialized_tournaments = tm.unserialize_all_tournaments(tournaments_table)
        """Affiche les tournois"""
        menu.display_tournament_from_db_short(unserialized_tournaments)
        """Choisi un tournoi"""
        selected_tournament = menu.get_int("\nEntrer le numéro du tournoi:")
        """Instancie un tournoi depuis TinyDB"""
        tournament = tm.instance_tournament_from_db(unserialized_tournaments[selected_tournament - 1])
        """Choisi un round du tournoi"""
        menu.display_rounds_from_db(selected_tournament, unserialized_tournaments)
        selected_round = menu.get_int("\nEntrer le numéro du round:")
        if tournament.round_list[selected_round - 1].end_time != 0:
            """Le round est deja joué"""
            menu.round_already_played()
            return
        if selected_round == 1:
            """Contrôle si c'est un round N°1 si selected_round = 1"""
            tournament = self.play_round_1(tournament)
            """Saisi les resultats des matchs du round 1"""
            return tournament
        elif selected_round > 1:
            """Controle si le round précédent est deja joué"""
            if tournament.round_list[selected_round - 2].end_time != 0:
                pass

    @staticmethod
    def play_round_1(tournament):
        """Execute les 4 match du round 1"""
        """Ajoute l'heure de début du round"""
        tournament.round_list[0].start_time = rm.timestamp()
        """Saisi les resultats des matchs du round et renvoie une liste sur match_list_result"""
        """[0] pour la liste des matchs et [1] pour les joueurs avec resultats"""
        match_list_result = mm.run_match(tournament.round_list[0].match_list)
        """Ajoute la liste des match avec resultats au round """
        tournament.round_list[0].match_list = match_list_result[0]
        """Mets à jour liste des joueurs du tournoi avec score"""
        tournament.players_list = match_list_result[1]
        """Ajoute' l'heure de fin du round"""
        tournament.round_list[0].end_time = rm.timestamp()
        """"Cloture le round par ajout de l'heure de fin"""
        menu.display_round_validation()
        return tournament


        # @staticmethod


    # def reste_du_tournoi():

    #     """Run les 4 matchs du Round """
    #     match_list_result = mm.run_match(match_list)

    #     """Ajoute la liste des match avec resultats au round """
    #     tournament.round_list[0].match_list = match_list_result[0]

    #     """Mets à jour liste des joueurs du tournoi avec score"""
    #     tournament.players_list = match_list_result[1]

    #     """"Cloture le round par ajout de l'heure de fin"""
    #     menu.display_round_validation(menu.get_input("Valider la fin du round en cours ? O/N"))
    #
    #     tournament.round_list[0].end_time = rm.timestamp()
    #     """Boucle pour les N round suivant le premier"""
    #     i = 1
    #     while i < len(tournament.round_list):
    #         tournament.round_list[i].start_time = rm.timestamp()
    #         """Genere la liste de match des rounds"""
    #         """Ajoute l'heure de debut du round"""
    #         match_list = mm.create_matches_next_round(tournament.players_list)
    #         """Recupere les resultats des matchs et la nouvelle liste de joueurs avec scores"""
    #         match_list_result = mm.run_match(match_list)
    #         """Ajouter la liste de match du round en cours"""
    #         tournament.round_list[i].match_list = match_list_result[0]
    #         match_list_result[0] = []
    #         """Renvoie la liste de joueurs avec scores sur le tournoi"""
    #         tournament.players_list = match_list_result[1]
    #         menu.display_round_validation(menu.get_input("Valider la fin du round en cours ? O/N"))
    #         """Ajoute l'heure de fin du round"""
    #         tournament.round_list[i].end_time = rm.timestamp()
    #         tournament.tournament.round_list = tournament.round_list
    #         i = i + 1
    #     """Affiche le gagnant du tournoi"""
    #     menu.display_winner(tournament.players_list)
    #     """Ajoute le tournoi terminé à la table tournament"""
    #     self.insert_data_to_db(tm.serialize_tournament(tournament), tournaments_table)
    #
