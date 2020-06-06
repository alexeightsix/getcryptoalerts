import re
from password_strength import PasswordPolicy


def isEmail(string: str) -> bool:
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.match(regex, string):
        return True
    return False


def isFullName(string: str) -> bool:
    regex = r"^([a-zA-Z0-9]+|[a-zA-Z0-9]+\s{1}[a-zA-Z0-9]{1,}|[a-zA-Z0-9]+\s{1}[a-zA-Z0-9]{3,}\s{1}[a-zA-Z0-9]{1,})$"
    if re.match(regex, string):
        return True
    return False


def isSecurePassword(string: str) -> bool:
    policy = PasswordPolicy.from_names(
        nonletters=0,
        length=6,
        uppercase=0,
        numbers=0,
        special=0,
    )
    return (len(policy.test(string)) == 0)


def isMailPusherId(string: str) -> bool:
    regex = r'^[a-zA-Z0-9]+'
    return re.search(regex, string)
