class Tournament:
    def __init__(self, name, place, date, rounds, timecontrol, description=None):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.timecontrol = timecontrol
        self.description = description


class Player:
    def __init__(self, lastname, surname, birthday, genre, rank):
        self.lastname = lastname
        self.sruname = surname
