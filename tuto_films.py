films = [
    ("Blade Runner (1982)", "vhf"),
    ("Alien : Le 8ème Passager (1979)", "vhf"),
    ("2001 : L'Odyssée de l'espace (1968)", "VhF"),
    ("Matrix (1999)", "DVD"),
    ("Interstellar (2014)", "dvD"),
    ("L'Empire contre-attaque (1980)", "vhf"),
    ("Retour vers le futur (1985)", "vhf"),
    ("La Guerre des Étoiles (1977)", "vhf"),
    ("L'Armée des 12 singes (1995)", "dVd"),
    ("Terminator 2 : Le Jugement dernier (1991)", "DVD"),
]


friends = [
    ("Paul", "Blade Runner"),
    ("Lucie",),
    ("Zoé", "Terminator 2 : Le Jugement dernier"),
]

class Film:
    def __init__(self, titre, date, lieu):
        self.titre = titre
        self.date = date
        self.lieu = lieu
        
    def display(self):
        print(f" Titre:'{self.titre}' de '{self.date}' chez '{self.lieu}' ")
        
    
class TypeFormat(Film):
    def __init__(self,type):
        self.type = type
    
    def display(self):
        super().display()
        print(f" Le film est de type:'{self.type}'")
