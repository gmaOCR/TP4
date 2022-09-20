import modules.View
from modules.Models import Tournament, Player
from modules.View import Menus

TIME_CONTROL = modules.View.TIME_CONTROL

menu = Menus()

class TournamentManager:


    def get_info(self):
        """Déclare l'objet "Menus" """
        menu.hello()
        """Message de bienvenue"""
        choice = menu.get_input(menu.main_menu())
        """Menu principal"""
        while choice not in ["1","2","3","4"]:
            print("\n Choix incorrect\n")
            choice = menu.get_input(menu.main_menu())
        if choice == "1":
            """ Créer un tournoi et récupère ses propriétés"""
            self.create_tournament()
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
        t_name = menu.get_input("Entrez le nom du tournoi:")
        t_place = menu.get_input("Entrez le lieu du tournoi:")
        t_date = menu.get_input("Entrez la date du tournoi: (JJ/MM/AAAA)")
        t_rounds = menu.get_input("Entrez le nombre de rondes: (défaut 4)")
        self.input_round_checker(t_rounds)
        t_time_control = menu.tc_menu("Sélectionner le chiffre du type de chronométrage:\n")
        """Vérifier et récupère le type de chrono dans la constante TIME_CONTROL"""

        # while t_time_control.isnumeric() is False:
        #     try:
        #         print("\n Choix incorrect\n")
        #         t_time_control = menu.tc_menu()
        #         int(t_time_control)
        #     except ValueError:
        #         print("\n Entrez un chiffre:\n")
        #         menu.tc_menu()
        #
        # while int(t_time_control) > len(TIME_CONTROL):
        #     print("\n Sélectionnez dans la liste\n")
        #     t_time_control = menu.tc_menu()
        #     print(TIME_CONTROL[int(t_time_control)])
        # if int(t_time_control) == 1:
        #     t_time_control = TIME_CONTROL[0]
        # if int(t_time_control) == 2:
        #     t_time_control = TIME_CONTROL[1]
        # if int(t_time_control) == 3:
        #     t_time_control = TIME_CONTROL[2]
        # else:
        #     while t_time_control.isnumeric() is False:
        #         try:
        #             t_time_control.isnumeric() is True
        #         except ValueError:
        #             print("\n Choix incorrect\n")
        #             menu.tc_menu()
        t_desc = menu.get_input("Entrez un commentaire (facultatif):")
        tournament = Tournament(t_name, t_place, t_date, t_time_control, t_rounds,None,None,t_desc)
        print(self.display_tournament(t_name))

    def input_round_checker(self,choice):
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



    def display_tournament(self,t_name):
        return (f"Nom du tournoi: {t_name}\n")
                # f"Lieu: {self.place}\n"
                # f"Jour:  {self.date}\n"
                # f"Nombre de tour: {self.rounds}\n"
                # f"Type de chrono: {self.timecontrol}\n"
                # f"Joueurs: {self.players_list}\n"
                # f"Information complémentaire: {self.description}\n")


