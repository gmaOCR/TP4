import datetime

class Menus:

    def hello(self):
        print("Bienvenue sur votre outil de gestion de tournois d'échecs:")

    def main_menu(self):
        return("1.Créer un tournoi \n"
                "2.Ajouter des joueurs \n"
                "3.Consulter des informations \n"
                "4.Quitter \n")

    def select_menu(self, menu):
        choice = input(menu)
        return choice

    def create_tournament(self):
            name = input()
            """ Nom du tournoi """
            place = input("Entrez le lieu du tournoi:")
            """" Lieu du tournoi """
            date = input("Entrez la date du tournoi: (JJ/MM/AAAA)")
            """ Date du jour du tournoi"""
            rounds = input("Entrez le nombre de rondes: (défaut 4)")
            desc = input("Entre un commentaire (facultatif):")
            return [name, place, date, rounds, desc]
            


