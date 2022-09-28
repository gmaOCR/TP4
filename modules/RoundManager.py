import datetime

from .Models import Round


class RoundManager:

    def create_first_round(self, tournament):
        round = Round("Round_1", tournament.name,self.timestamp(),"")
        return round

    def timestamp(self):
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        return dt_string
