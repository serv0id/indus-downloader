import time
from typing import override
from urllib.parse import urlparse
import requests
import config
import utils.crypto
from utils.device import IndusDevice


class IndusSession(requests.Session):
    def __init__(self, device: IndusDevice):
        super().__init__()
        self.device = device

    def _build_headers(self) -> dict:
        return {
            "android-version": config.ANDROID_VERSION,
            "release-version": config.RELEASE_VERSION,
            "sdk-version": config.SDK_VERSION,
            "ga-version": config.GA_VERSION,
            "device-brand": config.DEVICE_BRAND,
            "device-model": config.DEVICE_MODEL,
            "form-factor": config.FORM_FACTOR,
            "service-supported": config.SERVICE_SUPPORTED,
            "device-screen-density": config.DEVICE_SCREEN_DENSITY,
            "device-screen-density-buildprop": config.DEVICE_SCREEN_DENSITY_BUILDPROP,
            "device-locales": config.DEVICE_LOCALES,
            "device-abis": config.DEVICE_ABIS,
            "android-id": self.device.android_id,
            "gaid": self.device.gaid,
            "latitude": "",
            "longitude": "",
            "mcc": "",
            "mnc": "",
            "lac": "",
            "cid": "",
            "networkoperatorname": "",
            "networktype": config.NETWORK_TYPE,
            "x-extended-user-agent": str(config.EXTENDED_USER_AGENT),
            "user-agent": config.USER_AGENT,
            "integration-type": "standalone",
            "universe": config.UNIVERSE,
            "build-version": config.BUILD_VERSION,
            "split-apk-supported": "true",
            "appsessionid": "AS1765322136845",
            "client-event-timestamp": str(int(time.time()) * 1000),
            "deviceid": self.device.device_id,
            "x-source-app": "AB",
            "obb-supported": "true",
            "x-app-id": config.APP_ID,
            "x-merchant-id": config.MERCHANT_ID,
            "x-org-id": config.ORG_ID,
            "x-source-locale": "en",
            "x-source-platform": "Android",
            "x-source-type": config.SOURCE_TYPE,
            "x-source-version": config.APP_VERSION,
            "iasvariant": "indus",
            "issystemapp": "false",
            "termsandconditionsaccepted": "true",
            "buildtrack": "release",
            "buildenvironment": "phonepeProduction",
            "islowmemory": "false",
            "x-checkmate-client-id": config.CHECKMATE_CLIENT_ID,
            "x-checkmate-key-version": "1",
            "x-request-alias": config.REQUEST_ALIAS,
            "x-device-fingerprint": self.device.fingerprint,
        }

    @override
    def prepare_request(self, request) -> requests.PreparedRequest:
        prepared = super().prepare_request(request)
        parsed_url = urlparse(prepared.url)

        if prepared.body is None:
            body = b''
        else:
            body = prepared.body

        prepared.headers.update(self._build_headers())
        crypto = utils.crypto.CryptoUtils(self.device.device_id)

        prepared.headers["x-request-checksum-v4"] = crypto.build_checksum_v4_1(
            parsed_url.path.encode() + body
        )

        return prepared
