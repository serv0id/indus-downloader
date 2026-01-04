import base64
import hashlib
import time
import uuid
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import config


class CryptoUtils(object):
    def __init__(self, device_id: str):
        self.current_time = int(time.time() * 1000)
        self.device_id = device_id

    def build_checksum_v4_1(self, payload: str) -> str:
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
            - The (timestamp (in ms) || "###" || hashed payload) is encrypted using the first 16 bytes of the key and
              a random IV and tag using AES-GCM.
            - The tag and IV is appended to the result.
            - The appended string and the UUID is "zig-zagged" into a single string.
        """
        uuid_stripped: str = str(uuid.uuid4())[:16]

        key: bytes = hashlib.sha1((uuid_stripped + config.APP_SIGNATURE + self.device_id).encode()).digest()[:16]
        hashed_payload: bytes = base64.b64encode(hashlib.sha256(payload.encode()).digest())

        combined_payload = str(int(time.time()) * 1000) + "###" + hashed_payload.decode()

        nonce = get_random_bytes(12)
        cipher = AES.new(key, AES.MODE_GCM, nonce)
        encrypted_payload, tag = cipher.encrypt_and_digest(combined_payload.encode())

        encoded_checksum = b"16" + base64.b64encode(encrypted_payload + tag) + base64.b64encode(nonce)

        final_checksum = self.merge_bytes(encoded_checksum.decode(), uuid_stripped)

        return final_checksum.decode()

    @staticmethod
    def unmerge_bytes(data: bytes) -> tuple[str, str]:
        """
        * Helper Function *
        Reverse the merge_bytes() operation.
        """
        a4 = bytearray(16)
        a4[0:4] = data[0:4]
        a4[4:8] = data[8:12]
        a4[8:12] = data[16:20]
        a4[12:16] = data[24:28]

        a3_hdr = bytearray(12)
        a3_hdr[0:4] = data[4:8]
        a3_hdr[4:8] = data[12:16]
        a3_hdr[8:12] = data[20:24]

        a3_tail = data[28:]

        return (a3_hdr + a3_tail).decode(), a4.decode()

    @staticmethod
    def merge_bytes(a3: str, a4: str) -> bytes:
        """
        Merges the two strings in a "zigzag" manner.
        """
        a3b = a3.encode()
        a4b = a4.encode()
        return (
                a4b[0:4] + a3b[0:4] +
                a4b[4:8] + a3b[4:8] +
                a4b[8:12] + a3b[8:12] +
                a4b[12:16] + a3b[12:]
        )


if __name__ == "__main__":
    print("[-] Call this from an external module!")
