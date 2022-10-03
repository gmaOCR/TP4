from modules.MainManager import MainManager


class App:

    def run(self):
        main = MainManager()
        main.start()


if __name__ == "__main__":
    app = App()
    app.run()
