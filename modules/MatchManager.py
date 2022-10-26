from modules.PlayerManager import PlayerManager
from modules.Models import Match
from modules.View import Menus

menu = Menus()
pm = PlayerManager()


class MatchManager:

    @staticmethod
    def add_result(result, match):
        """Ajoute les resultats aux matchs et joueurs"""
        player_1 = match.score[0][0]
        player_2 = match.score[1][0]
        if result in ["1", 1]:
            match.score[0][1] = 1
            match.score[1][1] = 0
            player_1.score += 1
        elif result in ["2", 2]:
            match.score[1][1] = 1
            match.score[0][1] = 0
            player_2.score += 1
        elif result in ["N", "n"]:
            match.score[1][1] = 0.5
            match.score[0][1] = 0.5
            player_1.score += 0.5
            player_2.score += 0.5
        return [player_1, player_2]

    @staticmethod
    def create_matches_first_round(players_list):
        """Créé la liste des matchs du PREMIER round uniquement"""
        sorted(players_list, key=lambda player: int(player.rank), reverse=True)
        match_list = []
        for i, match in enumerate(players_list):
            """Ajout du joueur à sa propre liste d'exclusion"""
            players_list[int(i)].last_versus.append(players_list[int(i)])
            players_list[int(i + 4)].last_versus.append(players_list[int(i + 4)])
            """Constitue la liste des VS dans chaque Player"""
            players_list[int(i)].last_versus.append(players_list[int(i + 4)])
            players_list[int(i + 4)].last_versus.append(players_list[int(i)])
            """Instancie les match et les paires"""
            match = Match("", "", players_list[int(i)], players_list[int(i + 4)])
            match_list.append(match)
            if i == 3:
                break
        return match_list

    @staticmethod
    def create_matches_next_round_back(players_list):
        """Créé la liste des matchs pour les rounds suivants avec les scores du round précédent"""
        sorted_list = sorted(players_list, key=lambda player: (int(player.score), int(player.rank)))
        match_list = []
        i = 0
        for j, match in enumerate(sorted_list):
            match = Match(float, float, sorted_list[i], sorted_list[i + 1])
            match_list.append(match)
            i = i + 2
            if j == 3:
                break
        return match_list

    @staticmethod
    def create_matches_next_round(players_list):
        """Créé la liste des matchs pour les rounds suivants avec les scores du round précédent"""
        sorted_list = sorted(players_list, key=lambda player: (int(player.score), int(player.rank)))
        match_list = []
        i = 0
        while sorted_list[i].last_versus not in sorted_list[i + 1].last_versus:
            """Constitue la liste des VS dans chaque Player"""
            sorted_list[int(i)].last_versus.append(sorted_list[int(i + 1)])
            sorted_list[int(i + 1)].last_versus.append(sorted_list[int(i)])
            """Instancie le match"""
            match = Match(float, float, sorted_list[i], sorted_list[i + 1])
            match_list.append(match)
            if len(match_list) == 4:
                break
            elif len(sorted_list) > 1:
                del sorted_list[i]
                del sorted_list[i]
        return match_list

    def run_match(self, match_list):
        """Demande la saisie des resultats à l'operateur et les envois aux joueurs + match"""
        match_list_result = []
        next_round_players_list = []
        j = 1
        for match in match_list:
            print("\nQuel est le joueur gagnant match N°" + str(j) +
                  f" opposant {(match.score[0][0]).lastname} "
                  f"{(match.score[0][0]).firstname} à "
                  f"{(match.score[1][0]).lastname} {(match.score[1][0]).firstname} !\n")
            result = menu.get_result(input("Saisissez le résultat du match: (1) pour le premier joueur"
                                           " gagnant, (2) pour le second joueur gagnant ou (N)ul"))
            """Ajoute les resultats au match ET recupere les joueurs"""
            players = self.add_result(result, match)
            """Extendla liste des joueurs du tour suivant"""
            next_round_players_list.extend(players)
            """Append les match pour les renvoyer vers le round en cours"""
            match_list_result.append(match)
            j = j + 1
        return [match_list_result, next_round_players_list]

    @staticmethod
    def serialize_matchs(match_list, tournament):
        """Sérialise un match pour TinyDB"""
        serialized_matchs = []
        for match in match_list:
            serialized_match = {
                'Tournoi': tournament.name,
                'Score': (pm.serialize_player(match.score[0][0]), match.score[0][1],
                          pm.serialize_player(match.score[1][0]), match.score[1][1])
            }
            serialized_matchs.append(serialized_match)
        return serialized_matchs
