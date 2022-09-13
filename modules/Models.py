class Tournament:
    def __init__(self, name, place, date, timecontrol, rounds=4, description=None):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.timecontrol = timecontrol
        self.description = description


class Player:
    def __init__(self, lastname, surname, birthday, genre, rank, id):
        self.lastname = lastname
        self.surname = surname
        self.birthday = birthday
        self.genre = genre
        self.rank = rank
        self.id = id
        
        
class RoundFourPlayers:
    def __init__(self, player1, player2, player3, player4):
        self.player1 = Player.id
        
        
        

