import requests
import config


class IndusClient(object):
    def __init__(self):
        self.session = requests.Session()


def main() -> None:
    indus = IndusClient()


if __name__ == "__main__":
    main()
