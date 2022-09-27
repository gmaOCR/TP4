class MatchManager:

    def add_result(self):
        """A coder"""
        """Ajoute le score au Player"""
        pass

    def generate_matches_first_round(self, player_list):
        newlist = sorted(player_list, key=lambda player: int(player.rank), reverse=True)
        return newlist
