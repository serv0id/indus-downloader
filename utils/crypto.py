import time
from config import APP_SIGNATURE


class CryptoUtils(object):
    def __init__(self, device_id: str):
        self.current_time = int(time.time() * 1000)
        self.device_id = device_id

    def build_checksum_v4_1(self) -> None:
        """
        Also known as "newChecksumSecure", this value is derived
        from a certain known set of values which are shared with the
        server in other headers. The algorithm generates a string
        on the client side and is checked against the algorithm when
        run at the server side. Purpose seems to be anti-botting?

        Flow:
            - A v4 UUID is generated and trimmed to the first 16 characters.
            - The SHA-1 hash of the app signature is retrieved in base64.
            - The device ID is retrieved in base64.
            - These three values are appended and hashed (SHA-1) and used as the key.
            - The payload's SHA-256 is calculated and encoded to base64.
            - The hashed payload is encrypted using the first 16 bytes of the key and
              a random IV and tag using AES-GCM.
            - The result's IV and tag is appended to itself.
            - The UUID and the appended string is "zig-zagged" into a single string.
        """
        pass


if __name__ == "__main__":
    c = CryptoUtils()
