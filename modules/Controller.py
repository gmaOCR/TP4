from View import Menus
from Models import Tournament
from Models import Player


#Lignes de test

players_list = {Player("A", "1", "01/01/01", "M", "100", 1000), Player("B", "2", "02/02/02", "M", "95", 1001),
               Player("C","3", "03/03/03","M","103", 1002), Player("D", "4", "04/04/04", "F", "140", 1003),
               Player("E", "5", "05/05/05", "M", "65", 1004), Player("F", "6", "06/06/06", "F", "233", 1005),
               Player("G", "7", "07/07/07", "M", "230", 1006), Player("H", "8", "08/08/08", "F", "324", 1007)}
for players in players_list:
    print(players.display_player())
"""Génère 8 joueurs provisoires"""


























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
