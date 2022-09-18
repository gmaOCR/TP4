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
        choice = input(menu)
        # return int(choice)
        if choice == "":
            return None
        elif choice.isnumeric() is True:
            return choice
        elif choice.isnumeric() is False:
            print("La saisie doit être un nombre entier")
            while ValueError is not None:
                try:
                    choice = input(menu)
                    return int(choice)
                except ValueError:
                    print("La saisie doit être un nombre entier")
        else:
            return "Contactez l'administrateur"


    def get_time_control(self, menu):
        choice = input(menu)

        while ValueError is not None:
            try:
                print("try")
                choice = input(menu)
                return int(choice)
            except ValueError:
                print("err")
                return Menus.tc_out_of_range()


    def tc_out_of_range(self):
        """Retourne le menu de choix de TIMECONTROL """
        return("Entrez le chiffre correspondant:\n"
                + str("\n".join(TIME_CONTROL)))




