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

    def get_input_str(self, menu):
        choice = input(menu)
        return choice

    def get_input_int(self, menu):
        if input(menu) == "":
            return None
        else:
            while ValueError is not None:
                try:
                    choice = input(menu)
                    return int(choice)
                except ValueError:
                    print("Le nombre de rounds doit être un nombre entier")

    def get_time_control(self, menu):
        while ValueError is not None:
            try:
                choice = input(menu)
                return int(choice)
            except ValueError:
                return Menus.tc_out_of_range()


    def tc_out_of_range(self):
        """Retourne le menu de choix de TIMECONTROL """
        return("Entrez le chiffre correspondant:\n"
                + print(*TIME_CONTROL, sep = "\n"))

    def create_tournament(self):
        """A coder"""
        pass



