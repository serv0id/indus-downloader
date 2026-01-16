import json
import uuid
import config
from utils.device import IndusDevice
from utils.headers import IndusSession
from loguru import logger
import click
from prettytable import PrettyTable


class IndusClient(object):
    def __init__(self):
        self.device: IndusDevice = IndusDevice()
        self.import_device()
        self.session: IndusSession = IndusSession(self.device)

    def import_device(self) -> None:
        """
        Imports a device from a dumped file.
        """
        try:
            with open("device.json", "r") as f:
                data = json.load(f)
                self.device.__dict__.update(data)
                logger.info("Device loaded!")
        except FileNotFoundError:
            logger.error("No device file found! Run register.py")

    def search_app(self, name: str) -> None:
        """
        Searches for the app name and displays a table of possible matches.
        """
        logger.info(f"Searching for app: {name}")
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

        table = PrettyTable()
        table.field_names = ["Name", "Developer", "Version", "Package Name"]

        for app in res.json()["list"]:
            table.add_row([app["title"], app["developer"]["name"]["display"], app["versions"][0]["label"],
                           app["package"]])

        print(table)

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
        }).json()

        if res["download_link"] != '':
            print(f"Download Link: {res['download_link']}")
        else:
            logger.error(f"Package {package_name} not found!")

    def epoch(self) -> int:
        """
        Retrieves the epoch timestamp from Indus servers.
        """
        res = self.session.get(url=config.BASE_URL + "users/system/v1/epoch")

        return res.json()["data"]["epoch"]


@click.group()
def cli():
    """CLI for interacting with indus-downloader."""
    pass


@cli.command()
@click.argument("app_name")
def search(app_name: str) -> None:
    """Search for an app by name."""
    indus = IndusClient()
    indus.search_app(app_name)


@cli.command()
@click.argument("package_name")
def download(package_name: str) -> None:
    """Download an app by package name."""
    indus = IndusClient()
    indus.download_app(package_name)


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
