import datetime

from .Models import Round

class RoundManager:

    def create_first_round(self, tournament):
        r_name = "Round_1"
        r_tournament = tournament
        r_match_list = []

        pass

    def add_player_to_round(self, player):
        """Ajout des joueurs au round"""
        Round.match_list.append(player)

    def generate_match(self, playerA, playerB):
        """A coder"""
        """Stocker sous forme de tuple en 2 listes chaque match"""
        """Liste 1 ref à une instance de Player"""
        """Liste 2 score du match"""
        pass

    def run_first_round(self, playerA, playerB):
        """A coder"""
        """Premier tour en fonction du Player rank soit:"""
        """N1 vs N5 et N2 vs N6 et N3 vs N7 et N4 vs N8"""
        pass

    def run_next_round(self):
        """A coder"""
        """A partir du tour 2 - Fonction du score total et (rank si nécessaire)"""
        """Puis N1 vs N2 etc.. sauf si VS a déjà eu lieu"""
        pass

    def save_current_round(self):
        """A coder"""
        pass