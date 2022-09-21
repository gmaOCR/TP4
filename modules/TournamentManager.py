from tinydb import TinyDB

import modules.View
from modules.Models import Tournament
from modules.View import Menus
from modules.PlayerManager import PlayerManager

TIME_CONTROL = modules.View.TIME_CONTROL

menu = Menus()
"""Déclare l'objet "Menus" """

player_list_to_db = []

class TournamentManager:


    def start(self):
        "Lance le menu de départ"
        menu.hello()
        """Message de bienvenue"""
        choice = menu.get_input(menu.main_menu())
        """Menu principal"""
        while choice != "5":
            while choice not in ["1","2","3","4","5"]:
                print("\n Choix incorrect\n")
                choice = menu.get_input(menu.main_menu())
            if choice == "1":
                """ Créer une instance tournoi et récupère ses propriétés"""
                tm = TournamentManager()
                tournoi = tm.create_tournament()
                print(menu.display_tournament(tournoi.name, tournoi.place, tournoi.date, tournoi.rounds,tournoi.timecontrol,
                      tournoi.round_list, tournoi.player_list, tournoi.description))
            elif choice == "3":
                """ Instancie et ajoute des joueurs à la database"""
                pm = PlayerManager()
                player = pm.create_player()
                player_list_to_db.append(player)
                print(vars(player))
                print(pm.add_player_to_db(player))
                print(player_list_to_db)
                choice = menu.get_input(menu.main_menu())
            elif choice == "4":
                """ Consulter des informations """
                choice = menu.get_input(menu.main_menu())
                pass
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
        tournoi = Tournament(t_name, t_place, t_date, t_time_control, t_rounds,None,None,t_desc)
        return tournoi
        #print(menu.display_tournament(t_name, t_place, t_date, t_time_control, t_rounds, None, None, t_desc))



    def input_round_checker(self, choice):
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




