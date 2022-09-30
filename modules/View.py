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
    def tc_menu(menu):
        """Retourne le menu de choix de TIMECONTROL """
        menu = input(menu + str("\n".join(TIME_CONTROL)))
        return menu

    @staticmethod
    def display_tournament(tournament):
        return print((f"\nNom du tournoi: {tournament.name}\n"
                f"Lieu: {tournament.place}\n"
                f"Jour:  {tournament.date}\n"
                f"Nombre de tour: {tournament.rounds}\n"
                f"Type de chrono: {tournament.timecontrol}\n"
                f"Information complémentaire: {tournament.description}\n"))

    @staticmethod
    def display_player(player):
        return print(f"\nNom: {player.lastname}\n"
                     f"Prénom: {player.firstname}\n"
                     f"Date de naissance: {player.birthday}\n"
                     f"Sexe: {player.genre}\n"
                     f"Classement: {player.rank}\n"
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

    def display_match(self, match):
        return print(f"\nN° du tour: {match.rounds.name}"
                     f"\nJoueur a: {match.player_a.lastname} et rang: {match.player_a.rank}"
                     f"\nJoueur b: {match.player_b.lastname} et rang: {match.player_b.rank}"
                     f"\nResultat joueur a: {match.result_p_a}"
                     f"\nResultat joueur b: {match.result_p_b}"
                     # f"\nTournoi: {match.tournament.name}"
                     )

    def display_round(self, current_round, tournament):
        return print(f"\nN° du tour: {current_round.name}"
                     f"\nNom du tournoi: {tournament.name}"
                     f"\nHeure de début: {current_round.start_time}"                         
                     f"\nHeure de fin: {current_round.end_time}"
                     )