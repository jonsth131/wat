import base64

from libwat.encodings.utils import run_func


def check_b16(text):
    return run_func(text, base64.b16decode, r"^[A-Fa-f0-9]*$", "Base16")


def check_b32(text):
    return run_func(text, base64.b32decode, r"^[A-Za-z2-7]*={0,6}$", "Base32")


def check_b64(text):
    return run_func(text, base64.b64decode, r"^[A-Za-z0-9+\/]*={0,2}$", "Base64")


def check_b85(text):
    return run_func(
        text, base64.b85decode, r"^[A-Za-z0-9!#$%&()*+-;<=>?@^_`{|}~]*$", "Base85"
    )
