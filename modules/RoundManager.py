from datetime import datetime

from modules.MatchManager import MatchManager
from Models import Round
from View import Menus

"""Instancie le menu"""
menu = Menus()
"""Instancie le MatchManager"""
mm = MatchManager()


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

    @staticmethod
    def timestamp():
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        return dt_string

    @staticmethod
    def serialize_rounds(rounds_list, match_list, tournament):
        """Sérialise un round pour TinyDB"""
        serialized_rounds = []
        for round_unit in rounds_list:
            serialized_round = {
                'Nom du round': round_unit.name,
                'Tournoi': tournament.name,
                'Heure de début': round_unit.start_time,
                'Heure de fin': round_unit.end_time,
                'Liste des match du round': mm.serialize_matchs(match_list, tournament),
            }
            serialized_rounds.append(serialized_round)
        return serialized_rounds
