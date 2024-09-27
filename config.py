import os
from translation import Translation
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    URL = os.environ.get("URL", "")
    PORT = int(os.environ.get("PORT", 5000))
    CHUNK_SIZE = 10280
    APP_TITLE = os.environ.get("APP_TITLE", "usetgbot")
    APP_SHORT_NAME = os.environ.get("APP_SHORT_NAME", "usetgbot")
    APP_URL = os.environ.get("APP_URL", "https://telegram.dog/xtdevs")
    APP_PLATFORM = [
        "android",
        "ios",
        "wp",
        "bb",
        "desktop",
        "web",
        "ubp",
        "other"
    ]
    APP_DESCRIPTION = os.environ.get(
        "APP_DESCRIPTION",
        "created using https://telegram.dog/xtdevs"
    )
    #
    FOOTER_TEXT = os.environ.get("FTEXT", "@rencprx")
    START_TEXT = os.environ.get("START_TEXT", Translation.START_TEXT)
    AFTER_RECVD_CODE_TEXT = os.environ.get(
        "AFTER_RECVD_CODE_TEXT",
        Translation.AFTER_RECVD_CODE_TEXT
    )
    BEFORE_SUCC_LOGIN = os.environ.get(
        "BEFORE_SUCC_LOGIN",
        Translation.BEFORE_SUCC_LOGIN
    )
    ERRED_PAGE = os.environ.get("ERRED_PAGE", Translation.ERRED_PAGE)
    CANCELLED_MESG = os.environ.get(
        "CANCELLED_MESG",
        Translation.CANCELLED_MESG
    )
    IN_VALID_CODE_PVDED = os.environ.get(
        "IN_VALID_CODE_PVDED",
        Translation.IN_VALID_CODE_PVDED
    )
    IN_VALID_PHNO_PVDED = os.environ.get(
        "IN_VALID_PHNO_PVDED",
        Translation.IN_VALID_PHNO_PVDED
    )
    VFCN_CHECKING_ONE = "\"It is a beautiful and terrible thing, and should therefore be treated with great caution.\""
    ORIGINAL_CODE = "aHR0cHM6Ly9odWdnaW5nZmFjZS5jby9zcGFjZXMvcmFuZHlkZXYvYXBpZGJvdC9yYXcvbWFpbi9ib3QucHk="
    VFCN_RETURN_STATUS = "'compareFiles' returned '{ret_status}'."

class Development(Config):
    pass