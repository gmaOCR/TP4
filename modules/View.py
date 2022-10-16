import sys
from operator import attrgetter

TIME_CONTROL = ["1. bullet", "2. blitz", "3. coup rapide"]


class Menus:

    @staticmethod
    def hello():
        print("\nBienvenue sur votre outil de gestion de tournois d'échecs:")

    @staticmethod
    def main_menu():
        return ("\n1.Créer et lancer un tournoi\n"
                "2.Ajouter des joueurs à la base de données\n"
                "3.Consulter des informations\n"
                "9.Quitter \n")

    @staticmethod
    def data_menu():
        return ("\n1.Consulter la liste des joueurs disponibles\n"
                "2.Consulter la liste des joueurs d'un tournoi spécifique\n"
                "3.Consulter la liste des tournois terminés\n"
                "4.Consulter la liste des rounds d'un tournoi spécifique\n"
                "5.Consulter la liste des matchs d'un tournoi spécifique\n"
                "9.Retour \n")

    def display_reports_menu(self, selection, datas, tournament):
        """"Sous-menu des rapports"""
        if selection == 1:
            """Sous menu des joueurs de la DB"""
            choice = self.get_int(self.menu_sort_by())
            if choice in [1, 2]:
                """Affiche la liste des joueurs classés"""
                return self.display_players_from_db(datas, choice)
            else:
                print("\nSaisie incorrecte, retour au menu principal")
        elif selection == 2:
            """Sous menu des joueurs d'un tournoi selectionné"""
            self.display_tournament_from_db(tournament)
            self.get_int("\nEntrer le numéro du tournoi:")
            return

    @staticmethod
    def menu_sort_by():
        return ("\n1.Par ordre alphabétique\n"
                "2.Par classement\n")

    @staticmethod
    def get_input(menu):
        choice = input(menu)
        return choice

    @staticmethod
    def get_int(menu):
        is_int = input(menu)
        while is_int.isnumeric() is False:
            print("La saisie doit être un nombre entier")
            try:
                is_int = input()
            except ValueError:
                print("Erreur: la saisie doit être un nombre entier")
        return int(is_int)

    @staticmethod
    def get_result(menu):
        while menu not in ["1", 1, "2", 2, "N", "n"]:
            print("Choix incorrect: 1 pour joueur 1 gagnant, 2 pour joueur 2 gagnant, N pour match nul ")
            menu = input(menu)
        return menu

    @staticmethod
    def tc_menu(menu):
        """Retourne le menu de choix de TIMECONTROL """
        menu = input(menu + str("\n".join(TIME_CONTROL)))
        return menu

    def display_tournament(self, tournament):
        tc = self.tc_selection(tournament)
        return print(f"Nom du tournoi: {tournament.name}\n"
                     f"Lieu: {tournament.place}\n"
                     f"Jour:  {tournament.date}\n"
                     f"Nombre de tour: {tournament.rounds}\n"
                     f"Type de chrono: {tc[3:]}\n"
                     f"Information complémentaire: {tournament.description}\n")

    @staticmethod
    def tc_selection(tournament):
        tc = ""
        if tournament.timecontrol == "1":
            tc = str(TIME_CONTROL[0])
        elif tournament.timecontrol == "2":
            tc = str(TIME_CONTROL[1])
        elif tournament.timecontrol == "3":
            tc = str(TIME_CONTROL[2])
        return tc

    @staticmethod
    def display_tournament_from_db(tournament):
        i = 0
        exclude = {"Liste des rounds"}
        for j in tournament:
            print("\nTournoi N°" + str(i + 1) + ":")
            dict_key_exclude = ({k: (tournament[i])[k] for k in tournament[i] if k not in exclude})
            dict_as_list = sorted(dict_key_exclude.items())
            new_index = [4, 1, 0, 2, 3]
            dict_sorted = dict([dict_as_list[ind] for ind in new_index])
            for t in dict_sorted.items():
                print(t[0], ":", t[1])
            i = i + 1

    @staticmethod
    def display_player(player):
        return print(f"\nNom: {player.lastname}\n"
                     f"Prénom: {player.firstname}\n"
                     f"Date de naissance: {player.birthday}\n"
                     f"Sexe: {player.genre}\n"
                     f"Classement: {player.rank}\n"
                     f"Score total: {player.score}\n"
                     f"Identifiant: {player.ident}\n")

    @staticmethod
    def display_players_from_db(datas, choice):
        datas["Nom"] = datas["players"].apply(lambda row: row["Nom"])
        datas["Prénom"] = datas["players"].apply(lambda row: row["Prénom"])
        datas["Date de naissance"] = datas["players"].apply(lambda row: row["Date de naissance"])
        datas["Sexe"] = datas["players"].apply(lambda row: row["Sexe"])
        datas["Classement"] = datas["players"].apply(lambda row: row["Rang"])
        datas = datas.drop("players", axis=1)
        datas = datas.drop("tournaments", axis=1)
        if choice == 1:
            return print(datas.sort_values(["Nom"], axis=0))
        elif choice == 2:
            return print(datas.sort_values(["Classement"], axis=0, ascending=False))

    @staticmethod
    def display_players_from_list(players_list):
        i = 0
        invalid_dict_key = {"Date de naissance", "Identifiant unique", "Score", "VS"}
        for _ in players_list:
            dict_filtered = ({k: (players_list[i])[k] for k in players_list[i] if k not in invalid_dict_key})
            print("\nJoueur N°" + str(i) + ":")
            for t in dict_filtered.items():
                print(t[0], ":", t[1], end=" | ")
            i = i + 1

    # @staticmethod
    # def display_match_without_results(match, tournament):
    #     return print(f"\nTournoi: {tournament.name}"
    #                  f"\nJoueur a: {match.score[0][0].lastname} rang: {match.player_a.rank}\n"
    #                  f"VS\n"
    #                  f"Joueur b: {match.player_b.lastname} rang: {match.player_b.rank}\n"
    #                  )

    @staticmethod
    def display_round(one_round, tournament):
        return print(f"\nN° du tour: {one_round.name}"
                     f"\nNom du tournoi: {tournament.name}"
                     f"\nHeure de début: {one_round.start_time}"
                     f"\nHeure de fin: {one_round.end_time}"
                     )

    @staticmethod
    def display_match_with_results(match, tournament):
        return print(f"\nTournoi: {tournament.name}"
                     f"\nJoueur 1: {(match.score[0][0]).lastname} rang: {(match.score[0][0]).rank}\n"
                     f"VS\n"
                     f"Joueur 2: {(match.score[1][0]).lastname} rang: {(match.score[1][0]).rank}\n"
                     f"\nResultat joueur 1: {match.score[0][1]}"
                     f"\nResultat joueur 2: {match.score[1][1]}"
                     f"\nTuple de TP: {match.score}"
                     )

    @staticmethod
    def display_round_validation(menu):
        while menu not in ["O", "o"]:
            print("Merci de saisir O ou o  pour le TP !")
            menu = input("Valider la fin du round en cours ? O/N")

    @staticmethod
    def yes_or_no(menu, default=None):
        valid = {"oui": True, "o": True, "O": True, "non": False, "n": False}
        if default is None:
            prompt = " [o/n] "
        elif default == "oui":
            prompt = " [O/n] "
        elif default == "non":
            prompt = " [y/N] "
        else:
            raise ValueError("Saisie incorrecte: '%s'" % default)

        while True:
            sys.stdout.write(menu + prompt)
            choice = input().lower()
            if default is not None and choice == "":
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Saisissez 'oui' ou 'non' " "(sinon 'o' ou 'n').\n")

    @staticmethod
    def display_winner(player_list):
        winner = max(player_list, key=attrgetter("score"))
        lastname = attrgetter("lastname")(winner)
        firstname = attrgetter("firstname")(winner)
        print("\nLe gagnant du tournoi est: [" + str(lastname) + "] [" + str(firstname) + "] avec un score de: ["
              + str(winner.score) + "] points" )
