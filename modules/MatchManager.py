import random
import time
from modules.Models import Match
from View import Menus

menu = Menus()


class MatchManager:

    @staticmethod
    def add_result(result, match):
        """Ajoute les resultats aux matchs"""
        if result in ["a", "A"]:
            match.result_p_a = 1
            match.result_p_b = 0
            match.player_a.score += 1
        elif result in ["b", "B"]:
            match.result_p_b = 1
            match.result_p_a = 0
            match.player_b.score += 1
        elif result in ["N", "n"]:
            match.result_p_b = 0.5
            match.result_p_a = 0.5
            match.player_a.score += 0.5
            match.player_a.score += 0.5

    @staticmethod
    def create_matches_first_round(players_list):
        """Créé la liste des matchs du PREMIER round uniquement"""
        sorted(players_list, key=lambda player: int(player.rank), reverse=True)
        match_list = []
        for i, match in enumerate(players_list):
            match = Match("", "", players_list[int(i)], players_list[int(i + 4)], ())
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
            match = Match("", "", sorted_list[int(i)], sorted_list[int(i + 1)], ())
            match_list.append(match)
            i = i + 2
            if j == 3:
                break
        return match_list

    def run_match(self, match_list):
        match_list_result = []
        # Prepare sequence for random results
        j = 1
        for match in match_list:
            print("Lancement du match N°" + str(j) + " !")
            self.countdown()
            print("\nMatch terminé !\n")
            sequence = [i for i in [0, 0.5, 1]]
            # Random match result and points
            select = float
            for _ in range(1):
                select = random.choice(sequence)
            if select == 0:
                print("Joueur B gagnant !\n")
            elif select == 0.5:
                print("Match Nul !\n")
            elif select == 1:
                print("Joueur A gagnant !\n")
            result = menu.get_result(input("Saisissez le résultat du match: A, B ou (N)ul"))
            self.add_result(result, match)
            """Ajoute les resultats au match ET aux joueurs"""
            match_list_result.append(match)
            j = j + 1
        return match_list_result

    @staticmethod
    def countdown():
        for i in range(2, 0, -1):
            time.sleep(1)
            print(i)

    @staticmethod
    def serialize_matchs(matchs_list, tournament):
        """Sérialise un match pour TinyDB"""
        serialized_matchs = []
        for match in matchs_list:
            serialized_round = {
                'Tournoi' : tournament.name,
                'Joueur A': match.player_a,
                'Résultat A': match.result_a,
                'Joueur B': match.player_b,
                'Résultat B': match.result_b,
            }
            serialized_matchs.append(serialized_round)
        return serialized_matchs
