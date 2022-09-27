import uuid

from .Models import Player
from .View import Menus

menu = Menus()


class PlayerManager:
    @staticmethod
    def create_player_to_db():
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

    @staticmethod
    def serialize_player(player):
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

    @staticmethod
    def unserialize_player(serialized_player):
        """Déserialise un joueur et l'instancie"""
        lastname = serialized_player["Nom"]
        surname = serialized_player["Prénom"]
        birthday = serialized_player["Date de naissance"]
        genre = serialized_player["Sexe"]
        rank = serialized_player["Rang"]
        ident = serialized_player["Identifiant unique"]
        player = Player(lastname, surname, birthday, genre, rank, ident)
        return player

    @staticmethod
    def unserialize_all_players(players_table):
        """Déserialise la table complète des joueurs"""
        unserialized_players = players_table.all()
        return unserialized_players
    @staticmethod
    def add_player_to_db(serialized_players,table):
        return table.insert(serialized_players)

