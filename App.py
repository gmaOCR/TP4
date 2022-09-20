from modules.TournamentManager import TournamentManager


class App:

    def run(self):
        tm = TournamentManager()
        tm.start()


if __name__ == "__main__":
    app = App()
    app.run()
