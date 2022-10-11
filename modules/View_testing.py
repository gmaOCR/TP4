tournament = {
    "1": {"description": "Créer un nouveau tournoi", "choice": "C"},
    "2": {"description": "Consulter un tournoi", "choice": "C"}
    # "3": {"description": "Reprendre un  tournoi", "choice": "C"}
}
rondes = {
    "1": {"description": "Terminer le round en cours", "choice": "C"}
}
match = {
    "1": {"description": "Ajouter les resultats", "choice": "C"}
}
player = {
    "1": {"description": "Sélectionner des joueurs pour un tournoi", "choice": "C"},
    "2": {"description": "Créer de nouveaux joueurs", "choice": "C"},
}
report = {
    "1": {"description": "Afficher les joueurs par rang", "choice": "C"},
    "2": {"description": "Afficher les joueurs par nom", "choice": "C"},
    "3": {"description": "Afficher les tournois terminés", "choice": "C"},
    "4": {"description": "Afficher les rounds d'un tournoi", "choice": "C"},
    "5": {"description": "Afficher les matchs d'un tournoi", "choice": "C"},
}
home = {
    "1": {"description": "Gestion des tournois", "choice": tournament},
    "2": {"description": "Gestion des rounds", "choice": rondes},
    "3": {"description": "Gestion des matchs", "choice": match},
    "4": {"description": "Gestion des joueurs", "choice": player},
    "5": {"description": "Gestion des rapports", "choice": report},
}