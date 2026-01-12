import base64
import secrets
import uuid
import utils


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
        self.device_id = base64.b64encode(secrets.token_bytes(32)).decode()
        self.fingerprint = utils.crypto.CryptoUtils.build_fingerprint(self.device_id)
