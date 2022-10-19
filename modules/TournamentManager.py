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
        t_rounds = self.input_round_checker("Entrez le nombre de rondes: (défaut 4)")
        t_time_control = menu.tc_menu("Sélectionner le chiffre du type de chronométrage:\n")
        t_round_list = []
        t_p_list = []
        t_desc = menu.get_input("Entrez un commentaire (facultatif):")
        tournament = Tournament(t_name, t_place, t_date, t_time_control, t_rounds, t_round_list, t_desc, t_p_list)
        print("\nLe tournoi a été créée avec succès !\n")
        menu.display_tournament(tournament)
        return tournament

    @staticmethod
    def select_8_players(players_table):
        """ Fais choisir 8 joueurs à l'opérateur depuis la DB """
        """" Génère la liste des joueurs présent en DB"""
        all_player_available = pm.unserialize_all_players(players_table)
        players_list = []
        i = 0
        """" Boucle selectionnant 8 joueurs par choix opérateur"""
        while i < 8:
            i = i + 1
            print("LISTE DES JOUEURS DISPONIBLES EN BASE DE DONNEES")
            menu.display_players_to_select(all_player_available)
            while True:
                try:
                    choice = menu.get_input("\nChoisir le joueur " + str(i) + " du tournoi en cours: "
                                                                               "(saisir le numéro): \n")
                    int(choice)
                    players_list.append(pm.create_player_from_db(all_player_available[int(choice)]))
                    del all_player_available[int(choice)]
                    break
                except (ValueError, IndexError):
                    menu.display_players_to_select(all_player_available)
                    print("\n")
                    print("\nEntrez un numero de ligne de la liste !\n")
        return players_list

    @staticmethod
    def input_round_checker(choice):
        choice = input(choice)
        if choice == "":
            choice = 4
            return choice
        elif choice.isnumeric() is True:
            return choice
        else:
            menu.get_int("Entrez un nombre entier:")

    @staticmethod
    def serialize_tournament(tournament, round_list, match_list, players_list):
        """Sérialise le tournoi pour TinyDB"""
        serialized_tournament = {
            'Nom du tournoi': tournament.name,
            'Lieu': tournament.place,
            'Date': tournament.date,
            'Nb de rounds': tournament.rounds,
            'Liste des rounds': rm.serialize_rounds(round_list, match_list, tournament),
            'Nature du chronométrage': menu.tc_selection(tournament)[3:],
            'Liste des joueurs': pm.serialize_players(players_list),
            'Commentaires': tournament.description
        }
        return serialized_tournament

    # def unserialize_tournament_from_db(self, tournament, choice):
    #     print(tournament[choice-1])
    #     serialized_tournament = tournament[choice-1]
    #     name = serialized_tournament['Nom du tournoi']
    #     place = serialized_tournament['Lieu']
    #     rounds = serialized_tournament['Nb de rounds']
    #     tc_selection = serialized_tournament['Nature du chonométrage']
    #     description = serialized_tournament['Commentaires']
    #     return [name, place, rounds, tc_selection, description]

    @staticmethod
    def unserialize_all_tournaments(tournaments_table):
        """Déserialise la table complète des joueurs"""
        unserialized_tournaments = tournaments_table.all()
        return unserialized_tournaments
