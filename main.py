import string
import getpass
import hashlib
import os


def generate_salt():
    return os.urandom(15)


def hash_pass(pwd, salt, iteration=100000):
    hashed = hashlib.sha256(pwd.encode() + salt).hexdigest()
    for _ in range(iteration):
        hashed = hashlib.sha256(hashed.encode() + salt).hexdigest()

    return hashed


def check_pass():
    salt = generate_salt()
    pwd = getpass.getpass("enter your password")
    hashed_pwd = hash_pass(pwd, salt)
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

    if feedback:
        print("Additional feedback:")
        for msg in feedback:
            print(msg)


check_pass()
