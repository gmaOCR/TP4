import uuid

from .Models import Player
from .View import Menus

menu = Menus()


class PlayerManager:
    def create_player(self):
        """Instancie un joueur"""
        p_name = menu.get_input("Entrez le nom du joueur:")
        p_surname = menu.get_input("Entrez le prénom du joueur:")
        p_birthday = menu.get_input("Entrez la date de naissance du joueur:")
        p_genre = menu.get_input("Entrez le sexe du joueur:")
        p_rank = menu.get_input("Entrez le classement du joueur:")
        p_ident = str(uuid.uuid4())
        p_ident = p_ident[0:4]
        player = Player(p_name, p_surname, p_birthday, p_genre, p_rank, p_ident)
        return player

    def serialize_player(self,player):
        """Sérialise le joueur pour TinyDB"""
        serialized_player = {
            'Nom': player.lastname,
            'Prénom': player.surname,
            'Date de naissance': player.birthday,
            'Sexe': player.genre,
            'Rang': player.rank,
            'Identifiant unique': str(player.ident)
        }
        return serialized_player

    def unserialize_player(self, choice, serialized_player):
        """Déserialise un joueur et l'instancie"""
        lastname = serialized_player[choice]["Nom"]
        surname = serialized_player[choice]["Prénom"]
        birthday = serialized_player[choice]["Date de naissance"]
        genre = serialized_player[choice]["Sexe"]
        rank = serialized_player[choice]["Rang"]
        ident = serialized_player[choice]["Identifiant unique"]
        player = Player(lastname, surname, birthday, genre, rank, ident)
        return player

    def unserialize_table_of_players(self, players_table):
        """Déserialise la table complète des joueurs"""
        unserialized_players = players_table.all()
        return unserialized_players

    def add_player_to_current_tournament(self):
        """"""
