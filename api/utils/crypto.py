from hashlib import scrypt

# TODO move hash functions to their own file.
"""
Hash password.
"""
def hash_password(password, salt):
    scrypt_key = scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
    return scrypt_key

"""
Check that the current password.
"""
def check_password(pass_to_check, current_pass, salt):
    encoded_pass = hash_password(pass_to_check, salt)
    print(current_pass) # PROBLEMA.
    print("________")
    print(encoded_pass)
    return encoded_pass == current_pass
