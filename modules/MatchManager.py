import random
from modules.Models import Match


class MatchManager:

    def add_result(self, result, match):
        """Ajoute les resultats aux matchs"""
        if result in ["a", "A"]:
            match.result_p_a = 1
            match.result_p_b = 0
        elif result in ["b", "B"]:
            match.result_p_b = 1
            match.result_p_a = 0
        elif result in ["N", "n"]:
            match.result_p_b = 0.5
            match.result_p_a = 0.5

    def create_matches_first_round(self, round_obj, player_list_per_rank):
        """Créé la liste des matchs deu PREMIER round uniquement"""
        match_list = []
        for i, match in enumerate(player_list_per_rank):
            match = Match("", "", player_list_per_rank[int(i)], player_list_per_rank[int(i + 4)], round_obj)
            match_list.append(match)
            if i == 3:
                break
        return match_list

    def run_match(self, match):
        # Prepare sequence for random results
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
        return match
