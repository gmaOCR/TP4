from Models import Player

def add_player_to_db(self):
    """A coder"""
    pass

def display_player(self):
    return(f"Nom: {self.lastname}\n"
            f"Prénom: {self.surname}\n"
            f"Date de naissance: {self.birthday}\n"
            f"Sexe: {self.genre}\n"
            f"Classement: {self.rank}\n"
            f"Identifiant: {self.ident}\n")


# Lignes de test
players_list = {Player("A", "1", "01/01/01", "M", "100", 1000), Player("B", "2", "02/02/02", "M", "95", 1001),
                Player("C","3", "03/03/03","M","103", 1002), Player("D", "4", "04/04/04", "F", "140", 1003),
                Player("E", "5", "05/05/05", "M", "65", 1004), Player("F", "6", "06/06/06", "F", "233", 1005),
                Player("G", "7", "07/07/07", "M", "230", 1006), Player("H", "8", "08/08/08", "F", "324", 1007)}
#for players in players_list:
# print(players.display_player())
"""Génère 8 joueurs provisoires"""