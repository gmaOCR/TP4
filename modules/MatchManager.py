from modules.Models import Match


class MatchManager:

    def add_result(self):
        """A coder"""
        """Ajoute le score """
        pass

    def create_matches_first_round(self, round, player_list_per_rank):
        i = 0
        match_list = []
        for i, match in enumerate(player_list_per_rank):
            match = Match("", "", player_list_per_rank[int(i)], player_list_per_rank[int(i + 4)], round)
            match_list.append(match)
            if i == 3:
                break

        return match_list
