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


"""generates a key from the 'password' and the salt.
If 'load_existing_salt' is True, it'll load the salt from a file
in the current directory called 'salt.salt'.
If 'save_salt' is True than it'll generate a new
salt and save it to 'salt.salt' . """
def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    if load_existing_salt:
        # load existing salt
        salt = load_salt()
    elif save_salt:
        # generate new salt and save it
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    # generate the key from the salt and the password
    derive_key = derive_key(salt,password)
    # encode it using Base 64 and return it
    return base64.urlsafe_b64encode(derive_key)


