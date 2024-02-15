import pathlib 
import secrets
import os
import base64
import getpass

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


"""Generate the salt used for key derivation,
    'size' is the length of the salt to generate"""
def generate_salt(size=16):
    return secrets.token_bytes(size)


"""Derive the key from the `password` 
    using the passed `salt` """
def derive_key(salt, password):
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())


# load salt from salt.salt file
def load_salt():
    return open("salt.salt", "rb").read()

