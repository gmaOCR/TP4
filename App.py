from modules.MainManager import MainManager


class App:

    @staticmethod
    def run():
        main = MainManager()
        main.start()


if __name__ == "__main__":
    app = App()
    app.run()
