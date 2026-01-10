import base64
import secrets
import uuid
from requests import Session
import config
import utils.crypto


class IndusDevice(object):
    def __init__(self):
        self.gaid: str = ''
        self.android_id: str = ''
        self.device_id: str = ''
        self.fingerprint: str = ''

        self.create_device()

    def create_device(self) -> None:
        """
        Creates device unique secrets that form the basis for all
        subsequent API calls.
        """
        self.gaid = str(uuid.uuid4())
        self.android_id = secrets.token_hex(8)
        self.device_id = base64.b64encode(secrets.token_bytes(32))
        self.fingerprint = utils.crypto.CryptoUtils.build_fingerprint(self.device_id.decode())


class Register(object):
    def __init__(self):
        self.session: Session = Session()

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
    register.dump()


if __name__ == "__main__":
    main()
