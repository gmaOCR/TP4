import sys

TIME_CONTROL = ["1. bullet", "2. blitz", "3. coup rapide"]


class Menus:

    @staticmethod
    def hello():
        print("\nBienvenue sur votre outil de gestion de tournois d'échecs:")

    @staticmethod
    def main_menu():
        return ("\n1.Créer et lancer un tournoi\n"
                "2.Consulter la base de joueurs\n"
                "3.Ajouter des joueurs à la base de données\n"
                "4.Consulter des informations\n"
                "9.Quitter \n")

    @staticmethod
    def data_menu():
        return ("\n1.Consulter la liste des joueurs disponibles\n"
                "2.Consulter la liste des joueurs d'un tournoi spécifique\n"
                "3.Consulter la liste des tournois terminés\n"
                "4.Consulter la liste des rounds d'un tournoi spécifique\n"
                "5.Consulter la liste des matchs d'un tournoi spécifique\n"
                "9.Quitter \n")

    def to_rename(self, selection, players_list, tournaments_table):
        if selection == 1:
            choice = self.get_int(self.menu_sort_by())
            if choice == 1:
                players_list = sorted(players_list, key=lambda players: players['Nom'], reverse=False)
                self.display_players_from_db(players_list)
            if choice == 2:
                self.display_players_from_db(sorted(players_list, key=lambda player: int(player.rank), reverse=True))
            else:
                print("\nSaisie incorrecte, retour au menu principal")
        elif selection == 3:
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
        print(menu)
        is_int = input()
        while is_int.isnumeric() is False:
            print("La saisie doit être un nombre entier")
            try:
                is_int = input()
            except ValueError:
                print("Erreur: la saisie doit être un nombre entier")
        return int(is_int)

    @staticmethod
    def get_result(menu):
        while menu not in ["A", "a", "B", "b", "N", "n"]:
            print("Choix incorrect: A pour joueur A gagnant, B pour joueur B gagnant, N pour match nul ")
            menu = input(menu)
        return menu

    @staticmethod
    def tc_menu(menu):
        """Retourne le menu de choix de TIMECONTROL """
        menu = input(menu + str("\n".join(TIME_CONTROL)))
        return menu

    @staticmethod
    def display_tournament(tournament):
        tc = ""
        if tournament.timecontrol == "1":
            tc = str(TIME_CONTROL[0])
        elif tournament.timecontrol == "2":
            tc = TIME_CONTROL[1]
        elif tournament.timecontrol == "3":
            tc = TIME_CONTROL[2]
        return print(f"\nNom du tournoi: {tournament.name}\n"
                     f"Lieu: {tournament.place}\n"
                     f"Jour:  {tournament.date}\n"
                     f"Nombre de tour: {tournament.rounds}\n"
                     f"Type de chrono: {tc[3:]}\n"
                     # f"Liste de rounds: {tournament.round_list}\n"
                     f"Information complémentaire: {tournament.description}\n")

    @staticmethod
    def display_tournament_from_db(tournaments_table):
        tournaments_list = []
        j = - 1
        for i in tournaments_table:
            j = j + 1
            tournaments_list.append(i)
            print("N°", str(j), i)
        return tournaments_list

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
    def display_players_from_db(players_table):
        players_list = []
        j = - 1
        for _ in players_table:
            j = j + 1
            result = ' '.join(f'{key}: {value}' for key, value in players_table[j].items())
            players_list.append(result)
            print("N°:", str(j), " ", result)
        return players_list

    @staticmethod
    def display_match_without_results(match, tournament):
        return print(f"\nTournoi: {tournament.name}"
                     f"\nJoueur a: {match.score[0][0].lastname} rang: {match.player_a.rank}\n"
                     f"VS\n"
                     f"Joueur b: {match.player_b.lastname} rang: {match.player_b.rank}\n"
                     )

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
                     f"\nJoueur a: {(match.score[0][0]).lastname} rang: {(match.score[0][0]).rank}\n"
                     f"VS\n"
                     f"Joueur b: {(match.score[1][0]).lastname} rang: {(match.score[1][0]).rank}\n"
                     f"\nResultat joueur a: {match.score[0][1]}"
                     f"\nResultat joueur b: {match.score[1][1]}"
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
