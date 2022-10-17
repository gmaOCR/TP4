from modules.PlayerManager import PlayerManager
from modules.Models import Match
from modules.View import Menus

menu = Menus()
pm = PlayerManager()


class MatchManager:

    @staticmethod
    def add_result(result, match):
        """Ajoute les resultats aux matchs"""
        (match.score[0][0]).score = int((match.score[0][0]).score)
        (match.score[1][0]).score = int((match.score[1][0]).score)
        if result in ["1", 1]:
            match.score[0][1] = 1
            match.score[1][1] = 0
            (match.score[0][0]).score += 1
        elif result in ["2", 2]:
            match.score[1][1] = 1
            match.score[0][1] = 0
            (match.score[1][0]).score += 1
        elif result in ["N", "n"]:
            match.score[1][1] = 0.5
            match.score[0][1] = 0.5
            (match.score[0][0]).score += 0.5
            (match.score[1][0]).score += 0.5

    @staticmethod
    def create_matches_first_round(players_list):
        """Créé la liste des matchs du PREMIER round uniquement"""
        sorted(players_list, key=lambda player: int(player.rank), reverse=True)
        match_list = []
        for i, match in enumerate(players_list):
            match = Match("", "", players_list[int(i)], players_list[int(i + 4)])
            match_list.append(match)
            if i == 3:
                break
        return match_list

    @staticmethod
    def create_matches_next_round(players_list):
        """Créé la liste des matchs pour les rounds suivants les scores du round précédent"""
        sorted_list = sorted(players_list, key=lambda player: (int(player.score), int(player.rank)))
        match_list = []
        i = 0
        for j, match in enumerate(sorted_list):
            match = Match(float, float, sorted_list[int(i)], sorted_list[int(i + 1)])
            match_list.append(match)
            i = i + 2
            if j == 3:
                break
        return match_list

    def run_match(self, match_list):
        match_list_result = []
        j = 1
        for match in match_list:
            print(f"\nQuel est le joueur gagnant match N°" + str(j) + f" opposant {(match.score[0][0]).lastname} "
                  f"{(match.score[0][0]).firstname} à {(match.score[1][0]).lastname} {(match.score[1][0]).firstname} !\n")
            result = menu.get_result(input("Saisissez le résultat du match: (1) pour le premier joueur"
                                           " gagnant, (2) pour le second joueur gagnant ou (N)ul"))
            self.add_result(result, match)
            """Ajoute les resultats au match ET aux joueurs"""
            match_list_result.append(match)
            j = j + 1
        return match_list_result

    @staticmethod
    def serialize_matchs(matchs_list, tournament):
        """Sérialise un match pour TinyDB"""
        serialized_matchs = []
        for match in matchs_list:
            serialized_round = {
                'Tournoi': tournament.name,
                'Score': (pm.serialize_player(match.score[0][0]), str(match.score[0][1]),
                          pm.serialize_player(match.score[1][0]), str(match.score[1][1]))
                                }
            serialized_matchs.append(serialized_round)
        return serialized_matchs
