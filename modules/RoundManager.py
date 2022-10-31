from datetime import datetime

from modules.MatchManager import MatchManager
from modules.Models import Round
from modules.View import Menus

"""Instancie le menu"""
menu = Menus()
"""Instancie le MatchManager"""
mm = MatchManager()


class RoundManager:

    def create_round(self, tournament, max_round):
        """Instance un round"""
        i = 0
        round_list = []
        while i < int(max_round):
            unit_round = Round(f"Round n°{i + 1}", tournament.name, self.timestamp(),"",[])
            round_list.append(unit_round)
            i = i + 1
        return round_list

    @staticmethod
    def timestamp():
        """"Methode renvoyant l'heure du moment présent"""
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        return dt_string

    @staticmethod
    def serialize_rounds(rounds_list, tournament):
        """Sérialise un round pour TinyDB"""
        serialized_rounds = []
        for round_unit in rounds_list:
            serialized_round = {
                'Nom du round': round_unit.name,
                'Tournoi': tournament.name,
                'Heure de début': round_unit.start_time,
                'Heure de fin': round_unit.end_time,
                'Liste des match du round': mm.serialize_matchs(round_unit.match_list, tournament),
            }
            serialized_rounds.append(serialized_round)
        return serialized_rounds

    @staticmethod
    def instance_rounds_from_db(serialized_rounds):
        """Instancie une liste de round depuis TinyDB par le tournoi"""
        rounds_list = []
        if serialized_rounds is None:
            return rounds_list
        else:
            for unit_round in serialized_rounds:
                name = unit_round['Nom du round']
                tournament_name = unit_round['Tournoi']
                start_time = unit_round['Heure de début']
                end_time = unit_round['Heure de fin']
                round_instance = Round(name, tournament_name, start_time, end_time, [])
                rounds_list.append(round_instance)
            return rounds_list
