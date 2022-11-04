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
        while True:
            choice = menu.get_int(menu.display_main_menu())
            if choice == 1:
                """instancie et affiche un tournoi"""
                tournament = tm.create_tournament()
                self.insert_data_to_db(tm.serialize_tournament(tournament), tournaments_table)
            elif choice == 2:
                """Ajoute 8 joueurs à un tournoi sans joueurs"""
                tournament = self.add_players_to_tournament()
                self.update_tournament_table(tm.serialize_tournament(tournament), tournaments_table)
            elif choice == 3:
                """Exectuer les matchs d'un round d'un tournoi """
                self.play_round_selector()
            elif choice == 5:
                """Ajoute des joueurs à la DB"""
                pm.menu_add_players_to_db(players_table)
            elif choice == 4:
                """ Menu: Consulter des informations """
                """Affiche les choix disponibles de consultation"""
                selection = menu.get_int(menu.display_main_reports_menu())
                tournaments_obj_list = tm.instance_tournaments_list_obj(
                    tm.unserialize_all_tournaments(tournaments_table))
                menu.display_reports_menus(selection, players_datas, tournaments_obj_list)
            elif choice == 6:
                """Modifie le rang d'un joueur"""
                """Génère la liste des joueurs depuis la table des joueurs"""
                p_list = pm.unserialize_all_players_from_db(players_table)
                p_list_obj = pm.create_players_from_db(p_list)
                """"Affiche les joueurs de la liste"""
                menu.display_players_list_obj_by_line(p_list_obj)
                """Selection un index de joueur de la liste"""
                index_player = menu.get_int("\n\nSaisir le N° du joueur à éditer:")
                """Envoi le joueur au PlayerManager pour édition du rang"""
                player = pm.edit_player_rank(p_list_obj[index_player-1])
                """Update la table players"""
                players_table.update(player, where("Identifiant unique") == player["Identifiant unique"])
            elif choice == 9:
                exit("Fin")
            else:
                print("\n Choix incorrect !")

    @staticmethod
    def insert_data_to_db(serialized_data, table):
        """Ajoute des données à une table de tinyDB (en unitaire, pas en liste)"""
        return table.insert(serialized_data)

    @staticmethod
    def update_tournament_table(serialized_tournament, table):
        """Update des données à une table de tinyDB (en unitaire, pas en liste)"""
        table.update(serialized_tournament, where("Nom du tournoi") == serialized_tournament["Nom du tournoi"])

    @staticmethod
    def add_players_to_tournament():
        """Ajoute 8 joueurs à un tournoi sans joueurs"""
        """Variable des tournois déserialisés"""
        unserialized_tournaments = tm.unserialize_all_tournaments(tournaments_table)
        """Génère la liste de tournois disponibles"""
        tournaments_obj_list = tm.instance_tournaments_list_obj(unserialized_tournaments)
        """Sélectionne un tournoi"""
        tournament = tm.tournament_selection(tournaments_obj_list)
        """Controle si la liste de joueurs du tournoi est vide"""
        if tournament.players_list is None:
            """Variable des joueurs déserialisées"""
            unserialized_players = pm.unserialize_all_players_from_db(players_table)
            """Génère la liste des joueurs objets disponibles"""
            players_obj_list = pm.create_players_from_db(unserialized_players)
            """Envoie la liste au sélecteur de joueurs"""
            tournament.players_list = pm.select_8_obj_players_for_tournmanent(players_obj_list)
            """Génère la liste des 4 match du 1er Round"""
            tournament.round_list[0].match_list = mm.create_matches_first_round(tournament.players_list)
            return tournament
        else:
            """La liste de joueur n'est pas vide"""
            menu.players_list_not_empty()
            return tournament

    def play_round_selector(self):
        """Selecteur et controleur des rounds à jouer"""
        """Variable des tournois déserialisés"""
        unserialized_tournaments = tm.unserialize_all_tournaments(tournaments_table)
        tournaments_obj_list = tm.instance_tournaments_list_obj(unserialized_tournaments)
        """Filtre les tournois avec joueurs assignés uniquements"""
        tournaments_filtered = tm.tournaments_with_players_list(tournaments_obj_list)
        """Return si la liste de tournoi est vide"""
        if len(tournaments_filtered) == 0:
            return print("\n Aucun tournoi en attente, retour au menu principal.")
        """Affiche les tournois"""
        menu.display_tournament_obj_list_short(tournaments_filtered)
        """Choisi un tournoi"""
        selected_tournament = menu.get_int("\nEntrer le numéro du tournoi:")
        """Instancie un tournoi depuis TinyDB"""
        tournament = tm.instance_tournament_from_db(unserialized_tournaments[selected_tournament - 1])
        """Choisi un round du tournoi"""
        menu.display_rounds_from_db(selected_tournament, unserialized_tournaments)
        selected_round = menu.get_int("\nEntrer le numéro du round:")
        "Condition de round: round 1 ou round N"
        if tournament.round_list[selected_round - 1].end_time != 0:
            """Le round est deja joué"""
            menu.round_already_played()
            return
        elif selected_round == 1:
            """Contrôle si c'est un round N°1 si selected_round = 1"""
            """Saisi les resultats des matchs du round 1"""
            tournament = self.play_round_1(tournament)
            self.update_tournament_table(tm.serialize_tournament(tournament), tournaments_table)
            return tournament
        elif selected_round > 1:
            """Controle si le round précédent est deja joué"""
            if tournament.round_list[selected_round - 2].end_time != 0:
                tournament = self.play_round_n(tournament, selected_round)
                self.update_tournament_table(tm.serialize_tournament(tournament), tournaments_table)
                return tournament
            else:
                return print("\nLe round précédent n'est pas clôturé !\n")

    @staticmethod
    def play_round_1(tournament):
        """Execute les 4 match du round 1"""
        """Ajoute l'heure de début du round"""
        tournament.round_list[0].start_time = rm.timestamp()
        """Saisi les resultats des matchs du round et renvoie une liste sur match_list_result"""
        """[0] pour la liste des matchs et [1] pour les joueurs avec resultats"""
        match_list_result = mm.input_results_in_matchs(tournament.round_list[0].match_list)
        """Ajoute la liste des match avec resultats au round """
        if tournament.round_list[0].match_list is None:
            menu.no_matchs_avalaible()
            return tournament
        else:
            tournament.round_list[0].match_list = match_list_result[0]
        """Mets à jour liste des joueurs du tournoi avec score"""
        tournament.players_list = match_list_result[1]
        """Ajoute' l'heure de fin du round"""
        tournament.round_list[0].end_time = rm.timestamp()
        """Créer le round suivant"""
        tournament.round_list = rm.create_round(tournament, tournament.rounds)
        """Update le tournoi"""
        menu.display_round_validation()
        tm.check_tournament_done(tournament)
        return tournament

    @staticmethod
    def play_round_n(tournament, index):
        """Execute les 4 match du round N"""
        """Ajoute l'heure de début du round"""
        tournament.round_list[index - 1].start_time = rm.timestamp()
        """Recupere les resultats des matchs et la nouvelle liste de joueurs avec scores"""
        match_list = mm.create_matches_next_round(tournament.players_list)
        """Saisi les resultat des 4 matchs"""
        match_list_result = mm.input_results_in_matchs(match_list)
        """Saisi les resultats des matchs du round et renvoie une liste sur match_list_result"""
        """[0] pour la liste des matchs et [1] pour les joueurs avec resultats"""
        tournament.round_list[index - 1].match_list = match_list_result[0]
        """Mets à jour liste des joueurs du tournoi avec score"""
        tournament.players_list = match_list_result[1]
        """Ajoute' l'heure de fin du round"""
        tournament.round_list[index - 1].end_time = rm.timestamp()
        """Créer le round suivant"""
        tournament.round_list = rm.create_round(tournament, tournament.rounds)
        menu.display_round_validation()
        tm.check_tournament_done(tournament)
        return tournament
