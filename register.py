import config
from utils.device import IndusDevice
from utils.headers import IndusSession
from loguru import logger


class Register(object):
    def __init__(self):
        self.device: IndusDevice = IndusDevice()
        self.session: IndusSession = IndusSession(self.device)

    def retrieve_keys(self) -> dict:
        """
        Retrieves public keys for necessary cryptographic functions.
        """
        res = self.session.post(url=config.BASE_URL + "keystore/v2/keys/client/AB_ANDROID/latest", json=[
            "PAYLOAD_ENCRYPTION",
            "REGISTRATION_ENCRYPTION_KEY",
            "OCI_VERIFICATION_KEY"
        ])

        if res.status_code != 200:
            logger.error("Something went wrong while fetching public keys.")
            raise SystemExit

        return res.json()["data"]

    def register_device(self) -> None:
        """
        Registers a new device with the servers.
        """
        device = IndusDevice()

    def dump(self) -> None:
        """
        Dumps the credentials to a JSON file.
        """
        pass


def main() -> None:
    register = Register()
    register.retrieve_keys()


if __name__ == "__main__":
    main()
