import datetime

TIME_CONTROL = ["1. bullet", "2. blitz", "3. coup rapide"]


class Menus:

    @staticmethod
    def hello():
        print("Bienvenue sur votre outil de gestion de tournois d'échecs:")

    @staticmethod
    def main_menu():
        return ("1.Créer un tournoi\n"
                "2.Consulter la base de joueurs\n"
                "3.Ajouter des joueurs à la base de données\n"
                "4.Consulter des informations\n"
                "5 *** RESET LA BASE DE JOUEURS (F° TP)\n"
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
    def display_tournament(name, place, date, rounds, timecontrol, players_list, round_list, desc):
        return print((f"Nom du tournoi: {name}\n"
                f"Lieu: {place}\n"
                f"Jour:  {date}\n"
                f"Nombre de tour: {rounds}\n"
                f"Type de chrono: {timecontrol}\n"
                f"Liste des rondes: {round_list}\n"
                f"Joueurs: {players_list}\n"
                f"Information complémentaire: {desc}\n"))

    @staticmethod
    def display_player(lastname, surname, birthday, genre, rank, ident):
        return (f"\nNom: {lastname}\n"
                f"Prénom: {surname}\n"
                f"Date de naissance: {birthday}\n"
                f"Sexe: {genre}\n"
                f"Classement: {rank}\n"
                f"Identifiant: {ident}\n")

    def display_player_from_db(self, players):
        return print(*players)
        #return print(("\n" .join(map(str, players)) + "\n").replace("}", ""))
        #return print("\n" .join(map(str("Nom"), (str(players).translate(str.maketrans({"{": None, "}": None, "'": None}))))))


