class CRUD:
    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class Player(CRUD):
    def __init__(self, lastname, firstname, birthday, genre, rank, score, last_versus="", ident=""):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.genre = genre
        self.rank = rank
        self.score = score
        self.last_versus = last_versus
        self.ident = ident


class Match(CRUD):
    def __init__(self, result_p_a, result_p_b, player_a, player_b):
        self.score = tuple([[player_a, result_p_a], [player_b, result_p_b]])


class Round(CRUD):
    def __init__(self, name, tournament, start_time=0, end_time=0, match_list=None):
        self.name = name
        self.match_list = match_list
        self.tournament = tournament
        self.start_time = start_time
        self.end_time = end_time


class Tournament(CRUD):
    def __init__(self, name, place, date, timecontrol, rounds=None, round_list=None, description=None,
                 players_list=None):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.round_list = round_list
        self.timecontrol = timecontrol
        self.description = description
        self.players_list = players_list



