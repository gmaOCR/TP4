from modules.TournamentManager import TournamentManager


class App:

    def run(self):
        start = TournamentManager()
        start.get_info()


if __name__ == "__main__":
    app = App()
    app.run()
