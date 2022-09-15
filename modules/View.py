import datetime

class Menus:

    def hello(self):
        print("Bienvenue sur votre outil de gestion de tournois d'échecs:")

    def start_menu(self, menu):
        choice = input(menu)
        return choice

    def create_tournament(self):
            name = input("Entrez le nom du tournoi")
            """ Nom du tournoi """
            place = input("Entrez le lieu du tournoi")
            """" Lieu du tournoi """
            date_input = input("Entrez la date du tournoi (JJ/MM/AAAA)")
            """ A retravailler """
            #date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date
            #print(date)
            


