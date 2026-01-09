# Endpoints
BASE_URL = "https://api.indusappstore.com/apis/"

# Secrets
APP_ID = "c46aae5ef00640a09869fb183724b586"
APP_SIGNATURE = "L4lSY5pucA9Xwm5oS/xDmHZeDZA="

PAYLOAD_ENCRYPTION_KEY = ("MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmYu5nZQuf58VMwiVq"
                          "BNQM6+VGqs2EUSnueDYgKS0RjxFcZ5HwJHSLtsEbBLe8krONnM10frLfJwgmA"
                          "h1CtcQ0z322/mdHoGs2lHdiVZJA3F7i0b229YSU3jRF9wsujosbS+FJlbn2Tl"
                          "28iXc1tr5U/lIklGzoWpdVtM70tK8y+Z76Q/RvOLc4uJspCS76Oc45Pqc7z/s"
                          "pFlrkrhHo0Ql+Gn14V9KJI4n91RWC998TE/yxwNtckoUxz/sBqtl9+9ICYTca"
                          "+XyTKHKNOgS7nJb6l3sNkYo35uRxeihVCLtlj22UezafTMdRlm5UcGYj2DUBi"
                          "vb+8S5qsm8fqcHKGzXE8ehKr9TxwOLk7TKWoy0ps5RZYDw3BpAm+HI4DyOtyM"
                          "JhLpQZ3Rod5/jaOoh9Z+p+RHIX1JBzIXty7feyzYx6Zf8ECHASzI+rKfG6qkD"
                          "RyQ7Z9ttbkCyoXuqu/WCyRtlRK+XQHfEQlQwGAvFfsACxlMfx7U+665rqsfb0"
                          "nPoThSkIsXW6BPDo4GqOcZPzxBwvMONI8Ayc6ixQ5WAE7ctE6T4RCcWjzhJOn"
                          "RYTevo51gkJuqorf50DKNkBMkQASWGaKjBGrp+SDqLWfk/Ltv6Uxb1NGho2kY"
                          "VkQpiQRC09rJ6PrAlL2xmQgOEEPHSQxSAX1QWMervJxBUPiEtTiDiB/sCAwEA"
                          "AQ==")

REGISTRATION_ENCRYPTION_KEY = ("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsVtS18J6YIRV"
                               "xRuwVoOvhoYYOVTBV4Nc6wHH1ghBEBNIr9NWPWDaJ0rx5+IChO7qnsVw"
                               "BhuRJArrOnDlFdQ6PvvL3Qy0OJUnTQw5BC0pjWjkht6goxEhF7HNiCkm"
                               "tiE8/KeUr6oKcIHRTF5gsOiSuuihLzsowbGZZorDY+aZ07NblpAqnNDA"
                               "7o3TxJILRRljdTrgReEejik+0loovlGn8hlmZUYH6U75ytAzi7uE59fK"
                               "DJfLVPn7AveqUOSxtnst05xtks1hkYfic9U1Br6FJu8EmP36/7GSEaE8"
                               "ZAvn0Apn8tcFTZ147CU1z3G17bdzK/Xa4YJ/GBJO8T05JnQ9lQIDAQAB")

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
