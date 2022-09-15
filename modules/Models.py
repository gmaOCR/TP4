class Player:
    def __init__(self, lastname, surname, birthday, genre, rank, ident=int):
        self.lastname = lastname
        self.surname = surname
        self.birthday = birthday
        self.genre = genre
        self.rank = rank
        self.ident = ident

    def add_player_to_db(self):
        """A coder"""
        pass

    def display_player(self):
        return(f"Nom: {self.lastname}\n"
              f"Prénom: {self.surname}\n"
              f"Date de naissance: {self.birthday}\n"
              f"Sexe: {self.genre}\n"
              f"Classement: {self.rank}\n"
              f"Identifiant: {self.ident}\n")


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

    def add_result(self):
        """A coder"""
        """Ajoute le score au Player"""
        pass

class Round:
    def __init__(self, name, tournament, match_list=[], start_time=0, end_time=0):

        self.name = name
        self.match_list = match_list
        self.tournament = tournament
        self.player_list = tournament.player_list
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

    def display_tournament(self):
        return(f"Nom du tournoi: {self.name}\n"
              f"Lieur: {self.place}\n"
              f"Jour:  {self.date}\n"
              f"Nombre de tour: {self.rounds}\n"
              f"Type de chrono: {self.timecontrol}\n"
              f"Joueurs: {self.player_list}\n"
              f"Information complémentaire: {self.description}\n")

    def add_player_tournament(self, player):
        self.player_list.append(player)


    def select_tournament(self):
        """A coder"""
        pass