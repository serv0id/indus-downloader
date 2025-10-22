import requests


class IndusClient(object):
    def __init__(self):
        self.session = requests.Session()

    def register(self) -> None:
        """
        Registers a new device with the servers.
        """


def main() -> None:
    indus = IndusClient()


if __name__ == "__main__":
    main()
