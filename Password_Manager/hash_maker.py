import hashlib

def hash_maker(password=str):
    h = hashlib.new("SHA256")
    h.update(password.encode())
    hashed_pass = h.hexdigest()
    return hashed_pass