from modules.PlayerManager import PlayerManager
from modules.RoundManager import RoundManager
from modules.View import Menus
from modules.Models import Tournament

"""Déclare l'objet "Menus" from View.py """
menu = Menus()
"""Déclare l'objet "PlayerManager"""
pm = PlayerManager()
"""Déclare l'objet "PlayerManager"""
rm = RoundManager()


class TournamentManager:
    def create_tournament(self):
        "Instancie un tournoi"
        t_name = menu.get_input("Entrez le nom du tournoi:")
        t_place = menu.get_input("Entrez le lieu du tournoi:")
        t_date = menu.get_input("Entrez la date du tournoi: (JJ/MM/AAAA)")
        t_rounds = menu.get_input("Entrez le nombre de rondes: (défaut 4)")
        self.input_round_checker(t_rounds)
        t_time_control = menu.tc_menu("Sélectionner le chiffre du type de chronométrage:\n")
        t_round_list = []
        t_desc = menu.get_input("Entrez un commentaire (facultatif):")
        tournament = Tournament(t_name, t_place, t_date, t_time_control, t_rounds, t_round_list, t_desc)
        return tournament

    @staticmethod
    def select_8_players(players_table):
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
            while True:
                try:
                    choice = menu.get_input("\n Choisir le joueur " + str(i) + ": (saisir le numéro de ligne): \n")
                    int(choice)
                    break
                except ValueError:
                    print("Entrez un nombre entier !")
            players_list.append(pm.create_player_from_db(all_player_available[int(choice)]))
            del all_player_available[int(choice)]
        return players_list

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

    @staticmethod
    def serialize_tournament(tournament):
        """Sérialise le tournoi pour TinyDB"""
        serialized_tournament = {
            'Nom du tournoi': tournament.name,
            'Lieu': tournament.place,
            'Date': tournament.date,
            'Nb de rounds': tournament.rounds,
            'Liste des rounds': tournament.round_list,
            'Nature du chronométrage': tournament.timecontrol,
        }
        return serialized_tournament
