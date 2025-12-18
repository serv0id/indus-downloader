import requests
import config


class IndusClient(object):
    def __init__(self):
        self.session = requests.Session()

    def register(self) -> None:
        """
        Registers a new device with the servers.
        """
        pass

    def get_keys(self) -> dict:
        """
        Retrieves necessary RSA keys.
        """
        res = self.session.post(url=config.BASE_URL + "keystore/v2/keys/client/AB_ANDROID/latest",
                                json=[
                                        "PAYLOAD_ENCRYPTION",
                                        "REGISTRATION_ENCRYPTION_KEY",
                                        "OCI_VERIFICATION_KEY"
                                     ])

        return res.json()


def main() -> None:
    indus = IndusClient()


if __name__ == "__main__":
    main()
