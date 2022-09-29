class Player:
    def __init__(self, lastname, firstname, birthday, genre, rank, ident=""):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.genre = genre
        self.rank = rank
        self.ident = ident


class Match:
    def __init__(self, result_p_a, result_p_b, player_a, player_b, rounds):
        self.result_p_a = result_p_a
        self.result_p_b = result_p_b
        self.player_a = player_a
        self.player_b = player_b
        self.rounds = rounds


class Round:
    def __init__(self, name, tournament, start_time=0, end_time=0):

        self.name = name
        self.tournament = tournament
        self.start_time = start_time  # Automatiquement rempli à l'instanciation
        self.end_time = end_time  # Automatiquement rempli à la fin du tour (fin de TOUR et non de MATCH donc après le match N°4)


class Tournament:
    def __init__(self, name, place, date, timecontrol, rounds=4, description=None):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.timecontrol = timecontrol
        self.description = description
