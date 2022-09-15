class Player:
    def __init__(self, lastname, surname, birthday, genre, rank, ident=int):
        self.lastname = lastname
        self.surname = surname
        self.birthday = birthday
        self.genre = genre
        self.rank = rank
        self.ident = ident


class Score:
    def __init__(self, tournament, points, player):
        self.player = player
        self.tournament = tournament
        self.points = points


class Match:
    def __init__(self, result, player_a, player_b, tournament):
        self.result = result
        self.player_a = player_a
        self.player_b = player_b
        self.tournament = tournament


class Round:
    def __init__(self, name, tournament, match_list=[], start_time=0, end_time=0):

        self.name = name
        self.match_list = match_list
        self.tournament = tournament
        self.player_list = tournament.player_list
        self.start_time = start_time  # Automatiquement rempli à l'instanciation
        self.end_time = end_time  # Automatiquement rempli à la fin du tour (fin de TOUR et non de MATCH donc après le match N°4)


class Tournament:
    def __init__(self, name, place, date, timecontrol, rounds=4, round_list=[], player_list=[], description=None):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.round_list = round_list
        self.player_list = player_list
        self.timecontrol = timecontrol
        self.description = description
