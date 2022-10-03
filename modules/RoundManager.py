from datetime import datetime

from .Models import Round


class RoundManager:

    def create_round(self, tournament, round_number):
        round = Round(f"Round {round_number}", tournament.name, self.timestamp(), "")
        return round

    def timestamp(self):
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        return dt_string

