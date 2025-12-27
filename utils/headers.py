import time
from requests import Request
import config


class HeaderUtils(object):
    def __init__(self, request: Request):
        request.headers = self.build_headers()

    @staticmethod
    def build_headers() -> dict:
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
            "android-id": 0,  # TODO
            "gaid": 0,
            "latitude": None,
            "longitude": None,
            "mcc": None,
            "mnc": None,
            "lac": None,
            "cid": None,
            "networkoperatorname": None,
            "networktype": config.NETWORK_TYPE,
            "x-extended-user-agent": config.EXTENDED_USER_AGENT,
            "user-agent": config.USER_AGENT,
            "integration-type": "standalone",
            "universe": config.UNIVERSE,
            "build-version": config.BUILD_VERSION,
            "split-apk-supported": True,
            "appsessionid": 0,
            "client-event-timestamp": int(time.time()) * 1000,
            "deviceid": 0,
            "x-source-app": "AB",
            "obb-supported": True,
            "x-app-id": config.APP_ID,
            "x-merchant-id": config.MERCHANT_ID,
            "x-org-id": config.ORG_ID,
            "x-source-locale": "en",
            "x-source-platform": "Android",
            "x-source-type": config.SOURCE_TYPE,
            "x-source-version": config.APP_VERSION,
            "iasvariant": "indus",
            "issystemapp": False,
            "termsandconditionsaccepted": True,
            "buildtrack": "release",
            "buildenvironment": "phonepeProduction",
            "islowmemory": False,
            "x-checkmate-client-id": config.CHECKMATE_CLIENT_ID,
            "x-checkmate-key-version": 1,
            "x-request-alias": config.REQUEST_ALIAS
        }
