import uuid
import config
from utils.device import IndusDevice
from utils.headers import IndusSession


class IndusClient(object):
    def __init__(self):
        self.device: IndusDevice = IndusDevice()
        self.session: IndusSession = IndusSession(self.device)

    def search_app(self, name: str) -> dict:
        res = self.session.post(url=config.BASE_URL + "appsearch/apps/search", json={
            "deviceLang": "en",
            "iasLang": "en",
            "language": "en",
            "limit": "15",
            "packages": "false",
            "query": name,
            "search_session_id": f"SEARCH-{uuid.uuid4()}",
            "shouldCorrectQuery": "1",
            "source": "search",
            "sourceType": "search_results",
            "start": "0",
            "subSourceType": name
        })

        return res.json()

    def epoch(self) -> int:
        """
        Retrieves the epoch timestamp from Indus servers.
        """
        res = self.session.get(url=config.BASE_URL + "users/system/v1/epoch")

        return res.json()["data"]["epoch"]


def main() -> None:
    indus = IndusClient()
    print(indus.search_app("snapchat"))


if __name__ == "__main__":
    main()
