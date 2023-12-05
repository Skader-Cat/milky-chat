import hashlib
import secrets


def hash_password(password):
    salt = secrets.token_hex(16)

    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    hashed_password = hashlib.sha512(password_bytes + salt_bytes).hexdigest()

    return hashed_password, salt

def verify_password(password, hashed_password, salt):
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    new_hashed_password = hashlib.sha512(password_bytes + salt_bytes).hexdigest()

    return new_hashed_password == hashed_password

