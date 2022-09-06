class Film:
    def __init__(self, name):
        self.name = name

    def watch(self):
        print("Bon visionnage !")

class FilmCassette(Film):
    pass

class FilmDVD(Film):
    pass
class FilmBR(Film):
    pass


film = Film("Matrix")
film_cassette = FilmCassette("Blade runner")
film_DVD = FilmDVD("Battle royale")
film_BR = FilmBR("Inglorious Basterds")

print(film.name)
film.watch()

print(film_cassette.name)
film_cassette.watch()

print(film_BR.name)
film_BR.watch()

print(film_DVD.name)
film_DVD.watch()