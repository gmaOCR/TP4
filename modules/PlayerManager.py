import uuid

from .Models import Player
from .View import Menus

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
        p_last_versus = []
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
                players_table.insert(serialized_player)
                print("\nJoueur ajouté avec succès !\n")
                choice = menu.yes_or_no("Ajouter un autre joueur ?")
                if choice is False:
                    return players_table
            elif choice is False:
                choice = menu.yes_or_no("Ajouter un autre joueur ?")
                if choice is False:
                    return players_table
        else:
            print("\nRetour au menu principal\n")

    @staticmethod
    def serialize_player(player):
        """Sérialise un joueur unitaire pour TinyDB"""
        serialized_player = {
            'Date de naissance': player.birthday,
            'Identifiant unique': str(player.ident),
            'Nom': player.lastname,
            'Prénom': player.firstname,
            'Rang': int(player.rank),
            'Score': player.score,
            'Sexe': player.genre,
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
                'Identifiant unique': str(player.ident)
            }
            serialized_players_list.append(serialized_player)
        return serialized_players_list

    @staticmethod
    def unserialize_all_players_from_db(players_table):
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
        last_versus = []
        player = Player(lastname, firstname, birthday, genre, rank, score, last_versus, ident)
        return player
    
    @staticmethod
    def create_players_from_db(serialized_players):
        """Instancie une liste de joueurs depuis tinyDB"""
        players_list = []
        for _ in serialized_players:
            lastname = serialized_players["Nom"]
            firstname = serialized_players["Prénom"]
            birthday = serialized_players["Date de naissance"]
            genre = serialized_players["Sexe"]
            rank = serialized_players["Rang"]
            score = serialized_players["Score"]
            ident = serialized_players["Identifiant unique"]
            last_versus = []
            player = Player(lastname, firstname, birthday, genre, rank, score, last_versus, ident)
            players_list.append(player)
        return players_list

    def edit_player_rank(self, player):
        """Edite le rang d'un joueur serialisé"""
        player = self.create_player_from_db(player)
        player.rank = menu.get_int("Saisir le nouveau classement du joueur:")
        print(f"Le nouveau rang du joueur est {player.rank}")
        player = self.serialize_player(player)
        return player

