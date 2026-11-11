from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    hash = password_hash.hash(password)

    return hash

def verify_hash(password: str, db_hash: str) -> bool:
    return password_hash.verify(db_hash, get_password_hash(password))