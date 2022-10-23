import uuid

from .MainManager import MainManager
from .Models import Player
from .View import Menus

main = MainManager()
menu = Menus()


class PlayerManager:

    @staticmethod
    def create_player():
        """Instancie un joueur"""
        p_name = menu.get_input("Entrez le nom du joueur:")
        p_firstname = menu.get_input("Entrez le prénom du joueur:")
        p_birthday = menu.get_input("Entrez la date de naissance du joueur:")
        p_genre = menu.get_input("Entrez le sexe du joueur:")
        p_rank = menu.get_int("Entrez le classement du joueur:")
        p_ident = str(uuid.uuid4())
        p_ident = p_ident[0:4]
        p_last_versus = ""
        p_score = 0
        player = Player(p_name, p_firstname, p_birthday, p_genre, p_rank, p_score, p_last_versus, p_ident)
        return player

    def menu_add_players_to_db(self, players_table):
        """ Ajoute des joueurs à la database"""
        choice = True
        while choice is True:
            player = self.create_player()
            menu.display_player(player)
            choice = menu.yes_or_no("Verifier la saisie, ajouter à la base ?")
            if choice is True:
                serialized_player = self.serialize_player(player)
                main.add_data_to_db(serialized_player, players_table)
                print("\nJoueur ajouté avec succès !\n")
                choice = menu.yes_or_no("Ajouter un autre joueur ?")
                if choice is False:
                    break
            elif choice is False:
                choice = menu.yes_or_no("Ajouter un autre joueur ?")
                if choice is False:
                    break
        else:
            print("\nRetour au menu principal\n")

    @staticmethod
    def serialize_player(player):
        """Sérialise un joueur unitaire pour TinyDB"""
        serialized_player = {
            'Nom': player.lastname,
            'Prénom': player.firstname,
            'Date de naissance': player.birthday,
            'Sexe': player.genre,
            'Rang': int(player.rank),
            'Score': str(player.score),
            'VS': player.last_versus,
            'Identifiant unique': str(player.ident)
        }
        return serialized_player

    @staticmethod
    def serialize_players(players_list):
        """Sérialise une liste de  joueurs pour TinyDB"""
        serialized_players_list = []
        for player in players_list:
            serialized_player = {
                'Nom': player.lastname,
                'Prénom': player.firstname,
                'Date de naissance': player.birthday,
                'Sexe': player.genre,
                'Rang': int(player.rank),
                'Score': float(player.score),
                'Identifiant unique': str(player.ident),
                'VS': player.last_versus
            }
            serialized_players_list.append(serialized_player)
        return serialized_players_list

    @staticmethod
    def serialize_all_players_from_db(players_table):
        """Serialise les joueurs DEPUIS tinyDB"""
        serialized_players = players_table.all()
        return serialized_players

    @staticmethod
    def create_player_from_db(serialized_player):
        """Serialise un joueur depuis tinyDB et l'instancie"""
        lastname = serialized_player["Nom"]
        firstname = serialized_player["Prénom"]
        birthday = serialized_player["Date de naissance"]
        genre = serialized_player["Sexe"]
        rank = serialized_player["Rang"]
        score = serialized_player["Score"]
        ident = serialized_player["Identifiant unique"]
        last_versus = serialized_player["VS"]
        player = Player(lastname, firstname, birthday, genre, rank, score, ident, last_versus)
        return player

    def edit_player_rank(self, player):
        """Edite le rang d'un joueur serialisé"""
        player = self.create_player_from_db(player)
        player.rank = menu.get_int("Saisir le nouveau classement du joueur:")
        print(f"Le nouveau rang du joueur est {player.rank}")
        player = self.serialize_player(player)
        return player


