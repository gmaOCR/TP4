from datetime import datetime

from modules.MatchManager import MatchManager
from modules.Models import Round
from modules.View import Menus

"""Instancie le menu"""
menu = Menus()
"""Instancie le MatchManager"""
mm = MatchManager()


class RoundManager:

    @staticmethod
    def create_round(tournament, max_round):
        """Instance un round"""
        if len(tournament.round_list) < int(max_round):
            unit_round = Round(f"Round n°{len(tournament.round_list)+1}", tournament.name, 0, 0, None)
            tournament.round_list.append(unit_round)
            return tournament.round_list
        else:
            print("\nC'était le dernier round de ce tournoi !")
            return tournament.round_list

    @staticmethod
    def timestamp():
        """"Methode renvoyant l'heure du moment présent"""
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        return dt_string

    @staticmethod
    def serialize_rounds(tournament):
        """Sérialise un round pour TinyDB"""
        serialized_rounds = []
        for round_unit in tournament.round_list:
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
                if unit_round['Liste des match du round'] is not None:
                    match_list = mm.instance_matchs_from_db(unit_round['Liste des match du round'])
                else:
                    match_list = None
                round_instance = Round(name, tournament_name, start_time, end_time, match_list)
                rounds_list.append(round_instance)
            return rounds_list
