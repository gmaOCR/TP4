import datetime

TIME_CONTROL = ["1. bullet", "2. blitz", "3. coup rapide"]

class Menus:

    def hello(self):
        print("Bienvenue sur votre outil de gestion de tournois d'échecs:")

    def main_menu(self):
        return("1.Créer un tournoi \n"
                "2.Ajouter des joueurs \n"
                "3.Consulter des informations \n"
                "4.Quitter \n")

    def get_input(self, menu):
        choice = input(menu)
        return choice


    # def get_time_control(self, menu):
    #     choice = input(menu)
    #
    #     while ValueError is not None:
    #         try:
    #             print("try")
    #             choice = input(menu)
    #             return int(choice)
    #         except ValueError:
    #             print("err")
    #             return Menus.tc_out_of_range()


    def tc_menu(self,menu):
        """Retourne le menu de choix de TIMECONTROL """
        menu = input(menu + str("\n".join(TIME_CONTROL)))
        return menu


    def display_tournament(self,name ,place, date, rounds, timecontrol, players_list, round_list, desc ):
        return (f"Nom du tournoi: {name}\n"
                f"Lieu: {place}\n"
                f"Jour:  {date}\n"
                f"Nombre de tour: {rounds}\n"
                f"Type de chrono: {timecontrol}\n"
                f"Liste des rondes: {round_list}\n"
                f"Joueurs: {players_list}\n"
                f"Information complémentaire: {desc}\n")


