from datetime import datetime

from .Models import Round
from .View import Menus

menu = Menus()


class RoundManager:

    def create_round(self, tournament, max_round):
        i = 0
        round_list = []
        while i < int(max_round):
            round_number = f"Round n°{i + 1}"
            round = Round(f"Round {round_number}", tournament.name, self.timestamp(), "")
            round_list.append(round)
            i = i + 1
        return round_list

    def timestamp(self):
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        return dt_string

    def serialize_rounds(self, rounds_list, tournament):
        """Sérialise un round pour TinyDB"""
        serialized_rounds = []
        for rounds in rounds_list:
            serialized_round = {
                'Nom du round': rounds.name,
                'Tournoi': tournament.name,
                'Heure de début': rounds.start_time,
                'Heure de fin': rounds.end_time,
                'Liste des match du round': rounds.match_list,
            }
            serialized_rounds.append(serialized_round)
        return serialized_rounds
