import uuid
from tinydb import TinyDB

from .Models import Player
from .View import Menus

menu = Menus()


class PlayerManager:
    def create_player(self):
        p_name = menu.get_input("Entrez le nom du joueur:")
        p_surname = menu.get_input("Entrez le prénom du joueur:")
        p_birthday = menu.get_input("Entrez la date de naissance du joueur:")
        p_genre = menu.get_input("Entrez le sexe du joueur:")
        p_rank = menu.get_input("Entrez le classement du joueur:")
        p_ident = uuid.uuid4()
        player = Player(p_name, p_surname, p_birthday, p_genre, p_rank, p_ident)


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
    """Génère 8 joueurs provisoires"""