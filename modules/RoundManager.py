from datetime import datetime

from .Models import Round


class RoundManager:

    def create_first_round(self, tournament):
        round_1 = Round("Round 1", tournament.name, self.timestamp(), "")
        return round_1

    def timestamp(self):
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        return dt_string
