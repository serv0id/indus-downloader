import requests
import config
from utils.headers import IndusSession


class IndusClient(object):
    def __init__(self):
        self.session = IndusSession()


def main() -> None:
    indus = IndusClient()


if __name__ == "__main__":
    main()
