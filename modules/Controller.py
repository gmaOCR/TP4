from View import Menus
from Models import Tournament


#Code client provisoire
view = Menus()
"""Déclare l'objet "view" """

view.hello()
"""Affiche le message de bienvenue"""

choice = view.start_menu()
"""Récupère la sélection"""
while choice not in ["1","2","3","4"]:
    print("\n Choix incorrect\n")
    view.start_menu() 
    
if choice == "1":
    """ Créer un tournoi"""
    view.create_tournament()
else:
    view.start_menu()

