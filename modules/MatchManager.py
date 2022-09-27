from .Models import Match

class MatchManager:

    def add_result(self):
        """A coder"""
        """Ajoute le score au Player"""
        pass

    def generate_matches_first_round(self, player_list_per_rank):
        i = 0
        j = 0
        match_list = []
        #while j < 4: #magic number (= max_player_tournament / 2)
        for match in player_list_per_rank:
            match = Match("","",player_list_per_rank[int(i)],player_list_per_rank[int(i+4)],"")
            i = i + 1
            match_list.append(match)
        #    j = j + 1
        return match_list
