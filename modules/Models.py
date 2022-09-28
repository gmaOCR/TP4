class Player:
    def __init__(self, lastname, surname, birthday, genre, rank, points=None, ident=""):
        self.points = points
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
    def __init__(self, result_p_a, result_p_b, player_a, player_b, rounds, tournament):
        self.result_p_a = result_p_a
        self.result_p_b = result_p_b
        self.player_a = player_a
        self.player_b = player_b
        self.rounds = rounds
        self.tournament = tournament


class Round:
    def __init__(self, name, tournament, match_list, start_time=0, end_time=0):

        self.name = name
        self.match_list = match_list
        self.tournament = tournament
        self.player_list = tournament.player_list
        self.start_time = start_time  # Automatiquement rempli à l'instanciation
        self.end_time = end_time  # Automatiquement rempli à la fin du tour (fin de TOUR et non de MATCH donc après le match N°4)


class Tournament:
    def __init__(self, name, place, date, timecontrol, rounds=4, round_list=[], player_list=[], match_list=[], 
                 description=None):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.round_list = round_list
        self.player_list = player_list
        self.match_list = match_list
        self.timecontrol = timecontrol
        self.description = description
