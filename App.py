from modules.TournamentManager import TournamentManager


class App:

    def run(self):
        start = TournamentManager()
        start.get_info()


if __name__ == "__main__":
    app = App()
    app.run()



















# #Code client provisoire
# view = Menus()
# """Déclare l'objet "view" """

# view.hello()
# """Affiche le message de bienvenue"""

# choice = view.start_menu()
# """Récupère la sélection"""
# while choice not in ["1","2","3","4"]:
#     print("\n Choix incorrect\n")
#     view.start_menu()  
# if choice == "1":
#     """ Créer un tournoi"""
#     view.create_tournament()
# elif choice == "2":
#     """ Ajouter des joueurs à la database"""
#     pass
# elif choice == "3":
#     """ Consulter des informations """
#     pass
# elif choice == "4":
#     """ Quitter le programme """
#     exit
# #A continuer
