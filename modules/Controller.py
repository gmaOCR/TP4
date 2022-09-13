from View import Menus
from Tournois import Tournament


#Code client provisoire
view = Menus()
"""Déclare l'objet "View" """

view.hello()
"""Affiche le message de bienvenue"""

choice_lvl1 = view.start_menu()
"""Récupère la sélection"""

print(choice_lvl1)
if choice_lvl1 == "1":
    view
else:
    view.start_menu()

