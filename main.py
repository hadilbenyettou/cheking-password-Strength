import string
import getpass
import re
import hashlib


def hash_pass(pwd):
    hashed = hashlib.sha256(pwd.encode()).hexdigest()
    return hashed


def check_pass():
    pwd = getpass.getpass("enter your password")
    hashed_pwd = hash_pass(pwd)
    print(f"your hashed password is :{hashed_pwd}\n")

    strength = 0
    feedback = []
    remarks = ""
    low = 0
    upper = 0
    special = 0
    length = 0
    degit = 0

    for char in list(pwd):
        length += 1
        if char in string.ascii_lowercase:
            low += 1
        elif char in string.ascii_uppercase:
            upper += 1
        elif char in string.digits:
            degit += 1
        else:
            special += 1

    if length >= 8:
        strength += 1
    else:
        feedback.append(
            "your password is too short it should be at least 8 charachters"
        )
    if low >= 1:
        strength += 1
    else:
        feedback.append("your password should contain at least 1 lowercase letter")
    if upper >= 1:
        strength += 1
    else:
        feedback.append("your password should contain at least 1 uppercase letter")
    if degit >= 1:
        strength += 1
    else:
        feedback.append("your password should contain at least 1 degit")
    if special >= 1:
        strength += 1
    else:
        feedback.append("your password should contain at least 1 special character")

    if strength == 1:
        remarks = "Very Bad Password!!! Change ASAP"
    elif strength == 2:
        remarks = "Not A Good Password!!! Change ASAP"
    elif strength == 3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"
    print("your password has :")
    print(f"{length} charachters")
    print(f"{low} lowercase characters")
    print(f"{upper} uppercase characters")
    print(f"{degit} digit")
    print(f"{special} special chaachters")
    print(f"PS: {remarks} ")


check_pass()
