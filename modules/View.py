import sys
from operator import attrgetter

TIME_CONTROL = ["1. bullet", "2. blitz", "3. coup rapide"]


class Menus:

    @staticmethod
    def hello():
        """Message de bienvenue"""
        print("\nBienvenue sur votre outil de gestion de tournois d'échecs:")

    @staticmethod
    def display_main_menu():
        """Affiche le menu principal"""
        return ("\n---Gestion d'un tournoi---\n"
                "\n1.Créer un tournoi\n"
                "2.Ajouter des joueurs à un tournoi\n"
                "3.Jouer les match d'un round\n"
                "\n---Gestion des rapports et de la base---\n"
                "\n4.Consulter des informations\n"
                "5.Ajouter des joueurs à la base de données\n"
                "6.Modifier le rang d'un joueur\n"
                "\n9.Quitter \n")

    @staticmethod
    def display_main_reports_menu():
        """Affiche le menu des rapports"""
        return ("\n1.Consulter la liste des joueurs disponibles\n"
                "2.Consulter la liste des joueurs d'un tournoi\n"
                "3.Consulter la liste des tournois\n"
                "4.Consulter la liste des rounds d'un tournoi\n"
                "5.Consulter la liste des matchs d'un tournoi\n"
                "9.Retour \n")

    def display_reports_menus(self, selection, datas, tournaments_list_obj):
        """"Sous-menu des rapports"""
        if selection == 1:
            """Sous menu des joueurs de la DB"""
            choice = self.get_int(self.menu_sort_by())
            if choice in [1, 2]:
                """Affiche la liste des joueurs classése"""
                return self.display_players_from_db(datas, choice)
            else:
                return print("\nSaisie incorrecte, retour au menu principal")
        elif selection == 2:
            """Sous menu des joueurs d'un tournoi sélectionné"""
            self.players_list_display_checker(tournaments_list_obj)
            return
        elif selection == 3:
            """Sous menu d'un tournoi selectionné"""
            self.tournament_list_display_checker(tournaments_list_obj)
            return
        elif selection == 4:
            """Sous menu des rounds d'un tournoi sélectionné"""
            self.rounds_list_display_checker(tournaments_list_obj)
        elif selection == 5:
            """Sous menu des matchs d'un tournoi sélectionné"""
            self.matchs_list_display_checker(tournaments_list_obj)

    @staticmethod
    def menu_sort_by():
        """Menu de classement"""
        return ("\n1.Par ordre alphabétique\n"
                "2.Par classement\n")

    @staticmethod
    def get_input(message):
        """Renvoi n'importe quelle valeur"""
        choice = input(message)
        return choice

    @staticmethod
    def get_int(message):
        """Renvoie un entier"""
        is_int = input(message)
        while is_int.isnumeric() is False:
            print("La saisie doit être un nombre entier")
            try:
                is_int = input()
            except ValueError:
                print("Erreur: la saisie doit être un nombre entier")
        return int(is_int)

    @staticmethod
    def get_result(message):
        """Menu de saisie du gagnant du match"""
        while message not in ["1", 1, "2", 2, "N", "n"]:
            print("Choix incorrect: 1 pour joueur 1 gagnant, 2 pour joueur 2 gagnant, N pour match nul ")
            message = input(message)
        return message

    def tc_menu(self, menu):
        """Retourne le menu de choix de TIMECONTROL """
        menu = self.get_int(menu + str("\n".join(TIME_CONTROL)))
        return menu

    @staticmethod
    def display_tournament_obj(tournament_obj):
        """Affiche un objet tournoi"""
        return print(f"\n\033[4mNom du tournoi:\033[0m {tournament_obj.name}\n"
                     f"Lieu: {tournament_obj.place}\n"
                     f"Jour:  {tournament_obj.date}\n"
                     f"Nombre de tour: {tournament_obj.rounds}\n"
                     f"Type de chrono: {tournament_obj.timecontrol}\n"
                     f"Information complémentaire: {tournament_obj.description}\n")

    @staticmethod
    def display_tournament_obj_list_short(tournament_obj_list):
        i = 1
        for tournament in tournament_obj_list:
            print(f"\n\033[4mTournoi N°{i}:\033[0m\n"
                  f"Nom du tournoi: {tournament.name}")
            i = i + 1

    @staticmethod
    def display_tournament_dict_short(tournament):
        """Affiche une version courte d'un tournoi depuis la table tournoi"""
        i = 0
        exclude = {"Liste des rounds", "Liste des joueurs", "Lieu", "Date", "Nb de rounds", "Nature du chronométrage",
                   "Commentaires", "Terminé"}
        for _ in tournament:
            print("\nTournoi N°" + str(i + 1) + ":")
            dict_key_exclude = ({k: (tournament[i])[k] for k in tournament[i] if k not in exclude})
            for t in dict_key_exclude.items():
                print(t[0], ":", t[1])
            i = i + 1

    def display_tournament_with_winner(self, tournament):
        """Affiche un tournoi depuis une instance de tournoi"""
        if tournament.done is not True:
            self.display_tournament_obj(tournament)
            print("\nCe tournoi n'est pas encore terminé.")
        else:
            self.display_tournament_obj(tournament)
            print("\nCe tournoi est terminé.")
            self.display_winner(tournament.players_list)

    @staticmethod
    def display_player_obj(player):
        """Affiche un joueur depuis une instance joueur"""
        return print(f"\nNom: {player.lastname}\n"
                     f"Prénom: {player.firstname}\n"
                     f"Date de naissance: {player.birthday}\n"
                     f"Sexe: {player.genre}\n"
                     f"Classement: {player.rank}\n"
                     f"Score total: {player.score}\n"
                     # f"Identifiant: {player.ident}\n"
                     )

    @staticmethod
    def display_players_list_obj_by_line(players_list):
        """Affiche un joueur par ligne depuis une instance joueur"""
        i = 1
        for player in players_list:
            print(f"\033[4mJoueur N°{i}\033[0m")
            print(f"Nom: {player.lastname}  "
                  f"Prénom: {player.firstname}  "
                  f"Date de naissance: {player.birthday}  "
                  f"Sexe: {player.genre}  "
                  f"Classement: {player.rank}"
                  )
            i = i + 1

    def display_player_obj_from_list(self, players_list):
        i = 1
        for player in players_list:
            print(f"\033[4mJoueur N°{i}:\033[0m")
            self.display_player_obj(player)
            i = i + 1

    @staticmethod
    def display_players_from_db(datas, choice):
        """Affiche des joueurs depuis une dataframe Pandas"""
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
    def display_players_to_select(players_list):
        """Affiche des joueurs pour selection"""
        i = 0
        invalid_dict_key = {"Date de naissance", "Identifiant unique", "Score", "VS"}
        for _ in players_list:
            dict_filtered = ({k: (players_list[i])[k] for k in players_list[i] if k not in invalid_dict_key})
            print("\nJoueur N°" + str(i) + ":")
            for t in dict_filtered.items():
                print(t[0], ":", t[1], end=" | ")
            i = i + 1
        print("\n")

    @staticmethod
    def display_players_to_report(players_list):
        """Affiche des joueurs pour des rappports"""
        if players_list is not None:
            i = 0
            invalid_dict_key = {"Identifiant unique", "VS"}
            print("Voici la liste des 8 joueurs du tournoi sélectionné:\n")
            for _ in players_list:
                dict_filtered = ({k: (players_list[i])[k] for k in players_list[i] if k not in invalid_dict_key})
                dict_as_list = sorted(dict_filtered.items())
                new_index = [1, 2, 0, 3, 4, 5]
                dict_sorted = dict(dict_as_list[ind] for ind in new_index)
                for t in dict_sorted.items():
                    print(t[0], ":", t[1], end=" | ")
                i = i + 1
                print("\n")
        else:
            print("\nLa liste des joueurs de ce tournoi est vide\n")

    @staticmethod
    def display_rounds_from_db(choice, tournament):
        """Affiche des rounds pour rapports"""
        exclude_match = {"Liste des match du round"}
        rounds = (tournament[int(choice) - 1])["Liste des rounds"]
        i = 0
        for _ in rounds:
            print("\n")
            dict_key_exclude = ({k: rounds[i][k] for k in rounds[i] if k not in exclude_match})
            i = i + 1
            dict_as_list = sorted(dict_key_exclude.items())
            new_index = [3, 2, 0, 1]
            dict_sorted = dict([dict_as_list[ind] for ind in new_index])
            for n in dict_sorted.items():
                print(n[0], ":", n[1])
        print("\nCi-dessus la liste des rounds du tournoi sélectionné.")

    @staticmethod
    def display_rounds_obj_from_tournament(tournament):
        for a_round in tournament.round_list:
            print(f"\n\033[4mNom du round: {a_round.name}\033[0m\n"
                  f"Nom du tournoi: {tournament.name}\n"
                  f"Heure de début: {a_round.start_time}\n"
                  f"Heure de fin: {a_round.end_time}\n")
        print("Les tours sans heures de fin ne sont pas encore joués.\n")

    @staticmethod
    def display_round_validation():
        """Affiche la validation de fin de round"""
        print("\nCe round est à présent clôturé !")

    @staticmethod
    def display_matchs_obj_from_round(a_round):
        if a_round.match_list is not None:
            print("\n\033[4mRESULTATS DES MATCHS DU ROUND: \033[0m\n")
            i = 1
            for match in a_round.match_list:
                player_a = match.score[0][0]
                result_a = match.score[0][1]
                player_b = match.score[1][0]
                result_b = match.score[1][1]
                print(f"\033[4mMatch N°{i}: \033[0m\n"
                      f"Le score de [{player_a.lastname}] [{player_a.firstname}] est de [{result_a}]\n"
                      f"Le score de [{player_b.lastname}] [{player_b.firstname}] est de [{result_b}]\n")
                i = i + 1
            print("Pour rappel du score: 1 = gagnant, 0 = perdant et 0.5 = nul.\n")
        else:
            print("\nCe round ne contient pas de match\n")

    @staticmethod
    def display_winner(player_list):
        """Affiche le gagnant du tournoi"""
        winner = max(player_list, key=attrgetter("score"))
        lastname = attrgetter("lastname")(winner)
        firstname = attrgetter("firstname")(winner)
        return print(
            "Le gagnant de ce tournoi est: [" + str(lastname) + "] [" + str(firstname) + "] avec un score de: ["
            + str(winner.score) + "] points")

    def display_players_from_tournament(self, choice, tournament):
        """Affiche les joueurs d'un tournoi spécifique"""
        players_list = tournament[choice - 1]["Liste des joueurs"]
        return self.display_players_to_report(players_list)

    @staticmethod
    def yes_or_no(menu, default=None):
        """Méthode de gestion de la saisie Oui/Non"""
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
    def players_list_not_empty():
        print("\nLa liste de joueurs est déjà remplie pour ce tournoi.\n"
              "Retour au menu principal.")

    @staticmethod
    def round_already_played():
        print("\nCe round est dèjà terminé.\n"
              "Retour au menu principal.")

    @staticmethod
    def no_matchs_avalaible():
        print("\nAucun match n'est associé à ce round !\n"
              "Retour au menu principal.")

    @staticmethod
    def tournament_list_is_empty(tournaments_list_obj):
        if len(tournaments_list_obj) == 0:
            print("\nLa base de donnée ne contient aucun tournoi !\n")
            return True
        else:
            return False

    def tournament_list_display_checker(self, tournaments_list_obj):
        if self.tournament_list_is_empty(tournaments_list_obj) is True:
            return
        else:
            self.display_tournament_obj_list_short(tournaments_list_obj)
            index = self.get_int("\nCi-dessus la liste des tournois enregistrés.\nEntrez le numéro d'un tournoi "
                                 "pour plus d'informations")
            return self.display_tournament_with_winner(tournaments_list_obj[index - 1])

    def players_list_display_checker(self, tournaments_list_obj):
        if self.tournament_list_is_empty(tournaments_list_obj) is True:
            return
        else:
            self.display_tournament_obj_list_short(tournaments_list_obj)
            index = self.get_int("\nEntrer le numéro du tournoi:")
            if tournaments_list_obj[index - 1].players_list is None:
                return print("\nCe tournoi ne contient aucun joueurs !\n")
            else:
                return self.display_player_obj_from_list(tournaments_list_obj[index - 1].players_list)

    def rounds_list_display_checker(self, tournaments_list_obj):
        if self.tournament_list_is_empty(tournaments_list_obj) is True:
            return
        else:
            self.display_tournament_obj_list_short(tournaments_list_obj)
            index = self.get_int("\nEntrer le numéro du tournoi:")
            return self.display_rounds_obj_from_tournament(tournaments_list_obj[index - 1])

    def matchs_list_display_checker(self, tournaments_list_obj):
        if self.tournament_list_is_empty(tournaments_list_obj) is True:
            return
        else:
            self.display_tournament_obj_list_short(tournaments_list_obj)
            index_t = self.get_int("\nEntrer le numéro du tournoi:")
            self.display_rounds_obj_from_tournament(tournaments_list_obj[index_t - 1])
            index_r = self.get_int("\nEntrer le numéro du round:")
            return self.display_matchs_obj_from_round(tournaments_list_obj[index_t - 1].round_list[index_r - 1])

