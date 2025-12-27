import base64
import secrets
import uuid
from requests import Session
import config


class Register(object):
    def __init__(self):
        self.gaid: str
        self.android_id: str
        self.device_id: str
        self.session: Session = Session()

    def register(self) -> None:
        """
        Registers a new device with the servers.
        """
        pass

    def create_device(self) -> None:
        """
        Creates device unique secrets that form the basis for all
        subsequent API calls.
        """
        self.gaid = str(uuid.uuid4())
        self.android_id = secrets.token_hex(8)
        self.device_id = base64.b64encode(secrets.token_bytes(32))

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

    def dump(self) -> None:
        """
        Dumps the credentials to a JSON file.
        """
        pass


def main() -> None:
    register = Register()
    register.dump()


if __name__ == "__main__":
    main()
