import uuid
import config
from utils.device import IndusDevice
from utils.headers import IndusSession


class IndusClient(object):
    def __init__(self):
        self.device: IndusDevice = IndusDevice()
        self.session: IndusSession = IndusSession(self.device)

    def search_app(self, name: str) -> dict:
        """
        Searches for the app name and returns a dict of possible matches.
        """
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

    def download_app(self, package_name: str) -> dict:
        res = self.session.post(url=config.BASE_URL + "indus-abapi/device/apps/download/" + package_name, json={
            "version": "253372",
            "session_id": f"US{uuid.uuid4()}",
            "update": True,
            "destinationAvenue": "BROWSE",
            "destinationPage": "APP_DETAILS",
            "destinationTab": "",
            "language": "en",
            "installer": "INDUS_APPSTORE",
            "iasLang": "en",
            "deviceLang": "en"
        }, headers={
            "accept-version": "3.2.0"
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


if __name__ == "__main__":
    main()
