# Endpoints
BASE_URL = "https://api.indusappstore.com/apis/"

# Secrets
APP_ID = "c46aae5ef00640a09869fb183724b586"
APP_SIGNATURE = "L4lSY5pucA9Xwm5oS/xDmHZeDZA="

RSA_PUB = ("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsVtS18J6YIRVxRuwVoOv"
           "hoYYOVTBV4Nc6wHH1ghBEBNIr9NWPWDaJ0rx5+IChO7qnsVwBhuRJArrOnDlFdQ6"
           "PvvL3Qy0OJUnTQw5BC0pjWjkht6goxEhF7HNiCkmtiE8/KeUr6oKcIHRTF5gsOiS"
           "uuihLzsowbGZZorDY+aZ07NblpAqnNDA7o3TxJILRRljdTrgReEejik+0loovlGn"
           "8hlmZUYH6U75ytAzi7uE59fKDJfLVPn7AveqUOSxtnst05xtks1hkYfic9U1Br6F"
           "Ju8EmP36/7GSEaE8ZAvn0Apn8tcFTZ147CU1z3G17bdzK/Xa4YJ/GBJO8T05JnQ9"
           "lQIDAQAB")

# Header Values
MERCHANT_ID = "APPBAZAARONLINE"
CHECKMATE_CLIENT_ID = "AB_ANDROID"
ORG_ID = "INDUS_OS"
REQUEST_ALIAS = "V4_1"
SOURCE_TYPE = "INDUS_APP"
APP_VERSION = 25093063
ANDROID_VERSION = 33
RELEASE_VERSION = 13
SDK_VERSION = "25.09.23.6_BETA"
GA_VERSION = 25092360
UNIVERSE = "standaloneB2C"
BUILD_VERSION = "sta-25092360"

# Device specific values
DEVICE_BRAND = "Redmi"
DEVICE_MODEL = "RAD69"
FORM_FACTOR = "phone"
SERVICE_SUPPORTED = "gms"
DEVICE_SCREEN_DENSITY = 440
DEVICE_SCREEN_DENSITY_BUILDPROP = 440
DEVICE_LOCALES = ["en", "en-IN"]
DEVICE_ABIS = ["arm64-v8a", "armeabi-v7a", "armeabi"]

# User specific values
ANDROID_ID = ""
GAID = ""

LATITUDE = None
LONGITUDE = None

MCC = None
MNC = None
LAC = None
CID = None

NETWORK_OPERATOR_NAME = None
NETWORK_TYPE = "wifi"

EXTENDED_USER_AGENT = {
    "client": "AppBazaarClient",
    "meta": {
        "version": GA_VERSION,
        "source": {
            "id": "thirdparty",
            "manufacturer": DEVICE_BRAND,
            "model": DEVICE_MODEL
        },
        "build-date": "1758649125614"  # 23/09
    }
}

USER_AGENT = "Dalvik/2.1.0 (Linux; U; Android 13; RAD69 Build/TKQ1.221114.001)"
SPLIT_APK_SUPPORTED = True

DEVICE_ID = ""  # 32 bytes
