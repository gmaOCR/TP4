class Tournament:
    def __init__(self, name, place, date, timecontrol, rounds=[1,2,3,4], description=None):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.timecontrol = timecontrol
        self.description = description
        
    def add_player(self):
        """A coder"""
        pass
    
    def select_tournament(self):
        """A coder"""
        pass

class Player:
    def __init__(self, lastname, surname, birthday, genre, rank, id=[int]):
        self.lastname = lastname
        self.surname = surname
        self.birthday = birthday
        self.genre = genre
        self.rank = rank
        self.id = id
        
    def add_player_to_db(self):
        """A coder"""
        pass
    
    def display_player(self):
        print(f"Nom: {self.lastname}\n"
              f"Prénom: {self.surname}\n"
              f"Date de naissance: {self.birthday}\n"
              f"Sexe: {self.genre}\n"
              f"Classement: {self.rank}\n")
        
    def player_testing(self):
        return Player("A","1","01/01/01","M","100",1000)
        return Player("B","2","02/02/02","M","95",1001)
        return Player("C","3","03/03/03","F","105",1002)
        
class RoundEightPlayers:
    def __init__(self, match=[1,2,3,4], start_time=0, end_time=0):
        
        self.pairs = match
        self.start_time = start_time #Automatiquement rempli à l'instanciation
        self.end_time = end_time #Automatiquement rempli à la fin du tour (fin de TOUR et non de MATCH donc après le match N°4)
        """Déclaration à voir avec Samuel"""
        """Besoin des instances de joueurs"""
        """Apparraige des joueurs à discuter, faire ici ou dans le contrôleur ? Si ici, comment ?"""
    
    def add_player_to_round(self):
        """A coder"""
        pass
    
    def generate_match(self):
        """A coder"""
        """Stocker sous forme de tuple en 2 listes chaque match"""
        """Liste 1 ref à une instance de Player"""
        """Liste 2 score du match"""
        pass
    
    def run_first_round(self):
        """A coder"""
        """Premier tour en fonction du Player rank soit:"""
        """N1 vs N5 et N2 vs N6 et N3 vs N7 et N4 vs N8"""
        pass
    
    def run_next_round(self):
        """A coder"""
        """A partir du tour 2 - Fonction du score total et (rank si nécessaire)"""
        """Puis N1 vs N2 etc.. sauf si VS a déjà eu lieu"""
        pass    
    
    def save_current_round(self):
        """A coder"""
        pass   
    

class Matchs:
    def __init__(self, result, pairs):
    
        self.result = result
        self.pairs = pairs
        
    def add_result(self):
        """A coder"""
        """Ajoute le score au Player"""
        pass