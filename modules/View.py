import datetime


TIME_CONTROL = ["1. bullet", "2. blitz", "3. coup rapide"]



class Menus:

    @staticmethod
    def hello():
        print("Bienvenue sur votre outil de gestion de tournois d'échecs:")

    @staticmethod
    def main_menu():
        return ("\n1.Créer un tournoi\n"
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
        return print((f"Nom du tournoi: {tournament.name}\n"
                f"Lieu: {tournament.place}\n"
                f"Jour:  {tournament.date}\n"
                f"Nombre de tour: {tournament.rounds}\n"
                f"Type de chrono: {tournament.timecontrol}\n"
                f"Liste des rondes: {tournament.round_list}\n"
                f"Joueurs: {tournament.players_list}\n"
                f"Information complémentaire: {tournament.desc}\n"))

    @staticmethod
    def display_player(player):
        return print(f"\nNom: {player.lastname}\n"
                     f"Prénom: {player.surname}\n"
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

    def display_match(self,match):
        return print(f"\nJoueur a: {match.Player.surname}"
                     f"\nJoueur b: {match.player_b}"
                     f"\nResultat joueur a: {match.result_p_a}"
                     f"\nResultat joueur b: {match.result_p_b}"
                     f"\nTournoi: {match.tournament.name}")