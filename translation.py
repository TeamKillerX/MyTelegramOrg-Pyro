class Translation(object):
    START_TEXT = """Halo Kawan
Mau nyari App ID sama Api HASH kah?🗿
Masukin nomer Telegram mu disini kawan, pake +62 didepannya.
Channel Support @RendyProjects

───────────────────────
/start untuk melanjutkan pengisian."""
    AFTER_RECVD_CODE_TEXT = """Berhasil Kawan🗿
Kirim kesini kode yang telah dikirim oleh pihak telegramnya!

kode ini hanya digunakan untuk tujuan mendapatkan App Id & Api Hash dari my.telegram.org
kalau kamu gak percaya sama bot ini, ke my.telegram.org saja kawan, tapi disana lebih ribet hehe.

───────────────────────
/start untuk melanjutkan pengisian."""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@RendyProjects"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"