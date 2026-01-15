import json
import time
import config
from utils.device import IndusDevice
from utils.headers import IndusSession
from utils.crypto import CryptoUtils
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
        Registers a new device with the servers and dumps its JSON file.
        Payload can be adjusted to suit your needs.
        """
        payload_dict: dict = {
            "manufacturer": config.DEVICE_BRAND,
            "language": "en-US",
            "cid": "12345",
            "lac": "678",
            "imsi": "310260123456789",
            "model": config.DEVICE_MODEL,
            "deviceModel": config.DEVICE_MODEL,
            "carrier": "Airtel",
            "currentNetwork": "Airtel",
            "androidId": self.device.android_id,
            "android_name": "13",
            "disk_size": "128.0 GB",
            "totalDiskSize": "128.0 GB",
            "ram_size": "8.0 GB",
            "totalRamSize": "8.0 GB",
            "disk_size_left": "45.0 GB",
            "deviceCurrentDiskSizeLeft": "45.0 GB",
            "screen_resolution": "1080x2400",
            "deviceId": self.device.device_id,
            "externalDeviceId": self.device.device_id,
            "gaId": self.device.gaid,
            "hardware_id": self.device.android_id,
            "ab_system_app_flag": True,
            "device": config.DEVICE_MODEL,
            "deviceMarketName": config.DEVICE_MODEL
        }

        payload = json.dumps(payload_dict)

        res = self.session.post(url=config.BASE_URL + "indus-abapi/registration/web", headers={
            "x-encryption-type": "rsa-aes",
            "x-key-version": "1",
            "content-type": "text/plain",
        }, data=CryptoUtils.build_fingerprint(payload, config.REGISTRATION_ENCRYPTION_KEY))

        print(res.text)

    def dump(self) -> None:
        """
        Dumps the credentials to a JSON file.
        """
        with open(f"device_{time.time()}.json", "w") as f:
            json.dump(self.device.__dict__, f, indent=2)


def import_device(file) -> IndusDevice:
    """
    Imports a device from a dumped file.
    """
    with open(file, "r") as f:
        data = json.load(f)
        device = IndusDevice()
        device.__dict__.update(data)

        return device


def main() -> None:
    register = Register()
    register.register_device()


if __name__ == "__main__":
    main()
