import logging
from pyrogram.types import Message

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)


def parse_to_meaning_ful_text(input_phone_number, in_dict):
    """ Convert the dictionary returned in STEP FOUR into Telegram HTML text """
    me_t = ""
    me_t += "<i>Phone Number</i>: "
    me_t += f"<u>{input_phone_number}</u>"
    me_t += "\n\n"
    me_t += "<i>App Configuration</i>\n"
    me_t += "<b>APP ID</b>: <code>{}</code>\n".format(in_dict["App Configuration"]["app_id"])
    me_t += "<b>API HASH</b>: <code>{}</code>\n".format(in_dict["App Configuration"]["api_hash"])
    me_t += "\n"
    me_t += "<i>Available MTProto Servers</i>\n"
    me_t += "<b>Production Configuration</b>: <code>{}</code> <u>{}</u>\n".format(
        in_dict["Available MTProto Servers"]["production_configuration"]["IP"],
        in_dict["Available MTProto Servers"]["production_configuration"]["DC"]
    )
    me_t += "<b>Test Configuration</b>: <code>{}</code> <u>{}</u>\n".format(
        in_dict["Available MTProto Servers"]["test_configuration"]["IP"],
        in_dict["Available MTProto Servers"]["test_configuration"]["DC"]
    )
    me_t += "\n<i>Disclaimer</i>: <u>{}</u>".format(in_dict["Disclaimer"])

    return me_t


def extract_code_imn_ges(pyro_message: Message):
    """ Extracts the input message and returns the Telegram Web login code """
    telegram__web_login_code = None
    incoming_message_text = pyro_message.text
    incoming_message_text_in_lower_case = incoming_message_text.lower()

    if "web login code" in incoming_message_text_in_lower_case:
        parted_message_pts = incoming_message_text.split("\n")
        if len(parted_message_pts) >= 2:
            telegram__web_login_code = parted_message_pts[1]
    elif "\n" in incoming_message_text_in_lower_case:
        LOGGER.info("Did it come inside this 'elif'?")
    else:
        telegram__web_login_code = incoming_message_text

    return telegram__web_login_code


def get_phno_imn_ges(pyro_message: Message):
    """ Gets the phone number (in international format) from the input message """
    LOGGER.info(pyro_message)
    my_telegram_ph_no = None

    if pyro_message.text is not None:
        if pyro_message.entities is not None:
            for c_entity in pyro_message.entities:
                if c_entity.type == "phone_number":
                    # In Pyrogram, `c_entity.offset` and `c_entity.length` work similarly
                    my_telegram_ph_no = pyro_message.text[
                        c_entity.offset:c_entity.offset + c_entity.length
                    ]
        else:
            my_telegram_ph_no = pyro_message.text

    elif pyro_message.contact is not None:
        # Pyrogram provides `contact.phone_number` directly from the `contact` field
        if pyro_message.contact.phone_number != "":
            my_telegram_ph_no = pyro_message.contact.phone_number

    return my_telegram_ph_no


def compareFiles(first, second):
    """Compares two files byte by byte"""
    while True:
        firstBytes = first.read(4096)
        secondBytes = second.read(4096)
        if firstBytes != secondBytes:
            return False
        if firstBytes == b"":
            break
    return True
