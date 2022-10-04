import datetime


TIME_CONTROL = ["1. bullet", "2. blitz", "3. coup rapide"]



class Menus:

    @staticmethod
    def hello():
        print("Bienvenue sur votre outil de gestion de tournois d'échecs:")

    @staticmethod
    def main_menu():
        return ("\n1.Créer et lancer un tournoi\n"
                "2.Consulter la base de joueurs\n"
                "3.Ajouter des joueurs à la base de données\n"
                "4.Consulter des informations\n"
                "5 *** RESET LA BASE DE JOUEURS (F° HORS TP!)\n"
                "9.Quitter \n")

    @staticmethod
    def get_input(menu):
        choice = input(menu)
        return choice

    @staticmethod
    def get_result(menu):
        while menu not in ["A","a", "B", "b", "N", "n" ]:
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
                #f"Liste de rounds: {tournament.round_list}\n"
                f"Information complémentaire: {tournament.description}\n")

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
    def display_players_from_db(players):
        list_players = []
        j = - 1
        for i in players:
            j = j + 1
            list_players.append(i)
            print("N°", str(j), i)
        return list_players

    def display_match_without_results(self, match, tournament):
        return print(f"\nTournoi: {tournament.name}"
                     f"\nJoueur a: {match.player_a.lastname} rang: {match.player_a.rank}\n"
                     f"VS\n"
                     f"Joueur b: {match.player_b.lastname} rang: {match.player_b.rank}\n"
                     )

    def display_round(self, round, tournament):
        return print(f"\nN° du tour: {round.name}"
                     f"\nNom du tournoi: {tournament.name}"
                     f"\nHeure de début: {round.start_time}"                         
                     f"\nHeure de fin: {round.end_time}"
                     )

    def display_match_with_results(self, match,tournament):
        return print(f"\nTournoi: {tournament.name}"
                     f"\nJoueur a: {match.player_a.lastname} rang: {match.player_a.rank}\n"
                     f"VS\n"
                     f"Joueur b: {match.player_b.lastname} rang: {match.player_b.rank}\n"
                     f"\nResultat joueur a: {match.result_p_a}"
                     f"\nResultat joueur b: {match.result_p_b}"
                     f"\nTuple de TP: {match.score}"
                     )

    def display_round_validation(self, menu):
        while menu not in ["O", "o"]:
            print("Merci de saisir O ou o  pour le TP !")
            menu = input("Valider la fin du round en cours ? O/N")

