from tinydb import TinyDB
from operator import itemgetter
import json

import modules.View
from modules.Models import Tournament
from modules.View import Menus
from modules.PlayerManager import PlayerManager
from modules.RoundManager import RoundManager

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
"""Déclare l'objet "Roudnmanager" from Roundmanager.py """



class TournamentManager:

    def start(self):
        "Lance le menu de départ"
        menu.hello()
        """Message de bienvenue"""
        choice = menu.get_input(menu.main_menu())
        """Menu principal"""
        while choice != "9":
            while choice not in ["1", "2", "3", "4", "5"]:
                print("\n Choix incorrect\n")
                choice = menu.get_input(menu.main_menu())
            if choice == "1":
                self.menu_1()
                choice = menu.get_input(menu.main_menu())
            elif choice == "2":
                self.menu_2()
                choice = menu.get_input(menu.main_menu())
            elif choice == "3":
                self.menu_3(choice)
                choice = menu.get_input(menu.main_menu())
            elif choice == "4":
                """ Consulter des informations """
                choice = menu.get_input(menu.main_menu())
                pass
            elif choice == "5":
                self.clear_db()
                choice = menu.get_input(menu.main_menu())
        """ Quitter le programme """
        exit("Fin")

    def create_tournament(self):
        t_name = menu.get_input("Entrez le nom du tournoi:")
        t_place = menu.get_input("Entrez le lieu du tournoi:")
        t_date = menu.get_input("Entrez la date du tournoi: (JJ/MM/AAAA)")
        t_rounds = menu.get_input("Entrez le nombre de rondes: (défaut 4)")
        self.input_round_checker(t_rounds)
        t_time_control = menu.tc_menu("Sélectionner le chiffre du type de chronométrage:\n")
        t_desc = menu.get_input("Entrez un commentaire (facultatif):")
        tournoi = Tournament(t_name, t_place, t_date, t_time_control, t_rounds, None, None, t_desc)
        return tournoi
        # print(menu.display_tournament(t_name, t_place, t_date, t_time_control, t_rounds, None, None, t_desc))

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
    def add_player_to_db(serialized_players):
        players_table.insert(serialized_players)
        print(db)

    @staticmethod
    def clear_db():
        players_table.truncate()  # clear the table first
        return print("\nTable Players effacée !\n")

    def menu_3(self, choice):
        """ Ajoute des joueurs à la database"""
        while choice in ["O", "3"]:
            if choice == "O" or "3":
                player = pm.create_player()
                menu.display_player(player.lastname, player.surname, player.birthday, player.genre, player.rank,
                                    player.ident)
                choice = menu.get_input(menu="Verifier la saisie, ajouter à la base ? (O/N)")
                if choice == "O":
                    serialized_player = pm.serialize_player(player)
                    self.add_player_to_db(serialized_player)
                    print("\nJoueur ajouté avec succès !\n")
                else:
                    print("\nRetour au menu précédent\n")
            if choice == "N":
                print("\nRetour au menu principal\n")
            choice = menu.get_input("Ajouter un autre joueur ? (O/N)\n")

    def menu_1(self):
        """ Créer une instance tournoi et récupère ses propriétés
        Fais choisir 8 joueurs à l'opérateur depuis la DB et les ajoutent au tournoi"""
        players_list_full = pm.unserialize_table_of_players(players_table)
        print(players_list_full)
        players_list = []
        i = 0
        while i < 8:
            i = i + 1
            menu.display_players_from_db(players_table)
            choice = menu.get_input("Choisir le joueur "+ str(i) + ": (saisir le numéro de ligne): \n")
            print(int(choice))
            players_list = players_list.append(players_list_full[int(choice)])
            print(players_list.append(players_list_full[int(choice)]))
            r = set(players_list_full) - set(players_list)
            print(r)
            #player = pm.unserialize_player(int(choice), serialized_player)
            #players_list.append(player)
            #print(player_list)
        tm = TournamentManager()
        tournoi = tm.create_tournament()
        menu.display_tournament(tournoi.name, tournoi.place, tournoi.date, tournoi.rounds,tournoi.timecontrol,
                                tournoi.round_list, tournoi.player_list, tournoi.description)
        menu.get_input(menu="Verifier la saisie, ajouter à la base ? (O/N)")


    @staticmethod
    def menu_2():
        """Liste les joueurs depuis la DB"""
        return menu.display_players_from_db(pm.unserialize_table_of_players(players_table))


