import random
from modules.Models import Match


class MatchManager:

    def add_result(self):
        """A coder"""
        """Ajoute le score """
        pass

    def create_matches_first_round(self, round_obj, player_list_per_rank):
        i = 0
        match_list = []
        for i, match in enumerate(player_list_per_rank):
            match = Match("", "", player_list_per_rank[int(i)], player_list_per_rank[int(i + 4)], round_obj)
            match_list.append(match)
            if i == 3:
                break
        return match_list

    def run_match(self,match):
        #Init max loop and local variable
        i = 0
        #Prepare sequence for random results
        sequence = [i for i in [0, 0.5, 1]]
        #Random match result and points
        select = float()
        for _ in range(1):
            select = random.choice(sequence)
        if select == 0:
            match.result_p_a = 0
            match.result_p_b = 1

