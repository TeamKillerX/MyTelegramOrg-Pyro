import logging
import os
from base64 import b64decode

from pyrogram import Client, filters
from pyrogram.types import Message

from helper_funcs.step_one import request_tg_code_get_random_hash
from helper_funcs.step_two import login_step_get_stel_cookie
from helper_funcs.step_three import scarp_tg_existing_app
from helper_funcs.step_four import create_new_tg_app
from helper_funcs.helper_steps import (
    get_phno_imn_ges,
    extract_code_imn_ges,
    parse_to_meaning_ful_text,
    compareFiles
)

WEBHOOK = bool(os.environ.get("WEBHOOK", False))
if WEBHOOK:
    from sample_config import Config
else:
    from config import Development as Config

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

INPUT_PHONE_NUMBER, INPUT_TG_CODE = range(2)
GLOBAL_USERS_DICTIONARY = {}

app = Client(
    "apidbot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.TG_BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    """ ConversationHandler entry_point /start """
    await message.reply_text(
        Config.START_TEXT
    )
    GLOBAL_USERS_DICTIONARY[message.from_user.id] = {"state": INPUT_PHONE_NUMBER}


@app.on_message(filters.text)
async def handle_message(client: Client, message: Message):
    user_state = GLOBAL_USERS_DICTIONARY.get(message.from_user.id, {}).get("state")

    if user_state == INPUT_PHONE_NUMBER:
        await input_phone_number(client, message)
    elif user_state == INPUT_TG_CODE:
        await input_tg_code(client, message)


async def input_phone_number(client: Client, message: Message):
    """ Handle phone number input """
    user = message.from_user
    input_text = get_phno_imn_ges(message)
    if input_text is None:
        await message.reply_text(
            text=Config.IN_VALID_PHNO_PVDED
        )
        return
    random_hash = request_tg_code_get_random_hash(input_text)
    GLOBAL_USERS_DICTIONARY[user.id] = {
        "input_phone_number": input_text,
        "random_hash": random_hash,
        "state": INPUT_TG_CODE
    }
    await message.reply_text(
        Config.AFTER_RECVD_CODE_TEXT
    )


async def input_tg_code(client: Client, message: Message):
    """ Handle Telegram code input """
    user = message.from_user
    current_user_creds = GLOBAL_USERS_DICTIONARY.get(user.id)
    aes_mesg_i = await message.reply_text(Config.BEFORE_SUCC_LOGIN)

    provided_code = extract_code_imn_ges(message)
    if provided_code is None:
        await aes_mesg_i.edit_text(
            text=Config.IN_VALID_CODE_PVDED
        )
        GLOBAL_USERS_DICTIONARY[user.id]["state"] = INPUT_PHONE_NUMBER
        return

    # Login and get cookie
    status_r, cookie_v = login_step_get_stel_cookie(
        current_user_creds.get("input_phone_number"),
        current_user_creds.get("random_hash"),
        provided_code
    )

    if status_r:
        status_t, response_dv = scarp_tg_existing_app(cookie_v)
        if not status_t:
            create_new_tg_app(
                cookie_v,
                response_dv.get("tg_app_hash"),
                Config.APP_TITLE,
                Config.APP_SHORT_NAME,
                Config.APP_URL,
                Config.APP_PLATFORM,
                Config.APP_DESCRIPTION
            )

        status_t, response_dv = scarp_tg_existing_app(cookie_v)
        if status_t:
            me_t = parse_to_meaning_ful_text(
                current_user_creds.get("input_phone_number"),
                response_dv
            )
            me_t += "\n\n" + Config.FOOTER_TEXT
            await aes_mesg_i.edit_text(text=me_t)
        else:
            LOGGER.warning("Creating APP ID caused error %s", response_dv)
            await aes_mesg_i.edit_text(Config.ERRED_PAGE)
    else:
        await aes_mesg_i.edit_text(cookie_v)

    del GLOBAL_USERS_DICTIONARY[user.id]


@app.on_message(filters.command("cancel"))
async def cancel(client: Client, message: Message):
    """ Handle cancel """
    await message.reply_text(Config.CANCELLED_MESG)
    GLOBAL_USERS_DICTIONARY.pop(message.from_user.id, None)


@app.on_message(filters.command("verify"))
async def go_heck_verification(client: Client, message: Message):
    """ Verification check """
    s_m_ = await message.reply_text(Config.VFCN_CHECKING_ONE)
    oic = b64decode(Config.ORIGINAL_CODE).decode("UTF-8")
    pokk = f"{message.from_user.id}.py"
    os.system(f"wget {oic} -O {pokk}")
    ret_val = compareFiles(open("bot.py", "rb"), open(pokk, "rb"))
    await s_m_.edit_text(Config.VFCN_RETURN_STATUS.format(ret_status=ret_val))
    os.remove(pokk)


if __name__ == "__main__":
    app.run()