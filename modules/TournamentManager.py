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
        choice = menu.get_input_str(menu.main_menu())
        """Menu principal"""
        while choice not in ["1","2","3","4"]:
            print("\n Choix incorrect\n")
            choice = menu.get_input_str(menu.main_menu())
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
        t_name = menu.get_input_str("Entrez le nom du tournoi:")
        t_place = menu.get_input_str("Entrez le lieu du tournoi:")
        t_date = menu.get_input_str("Entrez la date du tournoi: (JJ/MM/AAAA)")
        t_rounds = menu.get_input_int("Entrez le nombre de rondes: (défaut 4)")
        self.input_int_checker(t_rounds)
        t_time_control = menu.get_time_control("Entrez le type de chrono: (1. bullet 2. blitz 3. coup rapide)")
        while t_time_control > len(TIME_CONTROL):
            print("\n Choix incorrect\n")
            t_time_control = menu.get_time_control(menu.tc_out_of_range())
        """Vérifier et récupère le type de chrono dans la constante TIME_CONTROL"""
        if t_time_control == 1:
            t_time_control = TIME_CONTROL[0]
        if t_time_control == 2:
            t_time_control = TIME_CONTROL[1]
        if t_time_control == 3:
            t_time_control = TIME_CONTROL[2]
        else:
            menu.get_time_control(menu.tc_out_of_range())
        t_desc = menu.get_input_str("Entrez un commentaire (facultatif):")
        #tournament = Tournament()


    def input_int_checker(self,choice):
        if choice == "":
            return 4
        elif choice.isnumeric() is True:
            return choice
        elif choice.isnumeric() is False:
            print("La saisie doit être un nombre entier")
            while ValueError is not None:
                try:
                    menu.get_input_int(int)
                    return choice
                except ValueError:
                    print("La saisie doit être un nombre entier")
        else:
            return "Contactez l'administrateur"

    def display_tournament(self):
        return (f"Nom du tournoi: {self.name}\n"
                f"Lieu: {self.place}\n"
                f"Jour:  {self.date}\n"
                f"Nombre de tour: {self.rounds}\n"
                f"Type de chrono: {self.timecontrol}\n"
                f"Joueurs: {self.players_list}\n"
                f"Information complémentaire: {self.description}\n")


    def add_player_tournament(self, player):
        self.players_list.append(player)


