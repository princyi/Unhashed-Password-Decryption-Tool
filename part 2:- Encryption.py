import hashlib

# Hash a password using SHA-256
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

hashed_password = encrypt_password(unhashed_password)
print(f"Hashed password: {hashed_password}")
