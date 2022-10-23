# @staticmethod
# def menu_display_players():
#     """Appelle la liste des joueurs depuis la DB"""
#     return menu.display_players_from_db(pm.unserialize_all_players(players_table))


# @staticmethod
# def display_match_without_results(match, tournament):
#     return print(f"\nTournoi: {tournament.name}"
#                  f"\nJoueur a: {match.score[0][0].lastname} rang: {match.player_a.rank}\n"
#                  f"VS\n"
#                  f"Joueur b: {match.player_b.lastname} rang: {match.player_b.rank}\n"
#                  )

# @staticmethod
# def display_round(one_round, tournament):
#     return print(f"\nN° du tour: {one_round.name}"
#                  f"\nNom du tournoi: {tournament.name}"
#                  f"\nHeure de début: {one_round.start_time}"
#                  f"\nHeure de fin: {one_round.end_time}"
#                  )

# @staticmethod
# def display_match_with_results(match, tournament):
#     return print(f"\nTournoi: {tournament.name}"
#                  f"\nJoueur 1: {(match.score[0][0]).lastname} rang: {(match.score[0][0]).rank}\n"
#                  f"VS\n"
#                  f"Joueur 2: {(match.score[1][0]).lastname} rang: {(match.score[1][0]).rank}\n"
#                  f"\nResultat joueur 1: {match.score[0][1]}"
#                  f"\nResultat joueur 2: {match.score[1][1]}"
#                  f"\nTuple de TP: {match.score}"
#                  )


# def unserialize_tournament_from_db(self, tournament, choice):
#     print(tournament[choice-1])
#     serialized_tournament = tournament[choice-1]
#     name = serialized_tournament['Nom du tournoi']
#     place = serialized_tournament['Lieu']
#     rounds = serialized_tournament['Nb de rounds']
#     tc_selection = serialized_tournament['Nature du chonométrage']
#     description = serialized_tournament['Commentaires']
#     return [name, place, rounds, tc_selection, description]

Entrer le numéro du tournoi:[{'Date de naissance': '04/04/04', 'Identifiant unique': '', 'Nom': 'Adam', 'Prénom': 'Eve', 'Rang': 1241, 'Score': 2.0, 'Sexe': 'A', 'VS': '5f63'}, {'Date de naissance': '05/05/05', 'Identifiant unique': '', 'Nom': 'Joueur 5', 'Prénom': 'Numero 5', 'Rang': 1212, 'Score': 1.0, 'Sexe': 'A', 'VS': '7bb5'}, {'Date de naissance': '06/06/06', 'Identifiant unique': '', 'Nom': 'Joueur 6', 'Prénom': 'Numero 6', 'Rang': 9301, 'Score': 2.0, 'Sexe': 'NA', 'VS': '9a31'}, {'Date de naissance': '07/07/07', 'Identifiant unique': '', 'Nom': 'Joueur 7', 'Prénom': 'Numero 7', 'Rang': 3134, 'Score': 1.0, 'Sexe': 'F', 'VS': 'e718'}, {'Date de naissance': '08/08/08', 'Identifiant unique': '', 'Nom': 'Joueur 8', 'Prénom': 'Numero 8', 'Rang': 1231, 'Score': 1.0, 'Sexe': 'M', 'VS': '19a1'}, {'Date de naissance': '09/09/09', 'Identifiant unique': '', 'Nom': 'Joueur 9', 'Prénom': 'Numero 9', 'Rang': 1242, 'Score': 2.0, 'Sexe': 'F', 'VS': '4423'}, {'Date de naissance': '10/10/10', 'Identifiant unique': '', 'Nom': 'Joueur 10', 'Prénom': 'Numero 10', 'Rang': 123, 'Score': 1.0, 'Sexe': 'F', 'VS': '2981'}, {'Date de naissance': '11/11/11', 'Identifiant unique': '', 'Nom': 'Joueur 11', 'Prénom': 'Numero 11', 'Rang': 329, 'Score': 0.0, 'Sexe': 'M', 'VS': '4c26'}]
