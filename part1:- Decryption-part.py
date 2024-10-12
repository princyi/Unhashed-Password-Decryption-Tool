import itertools
import string

# Sample unhashed password to "decrypt"
unhashed_password = "abc123"

# Define character set (lowercase letters, digits, etc.)
charset = string.ascii_lowercase + string.digits

# Function to brute-force the password
def brute_force_decrypt(target_password, charset, max_length=6):
    for length in range(1, max_length + 1):
        # Generate all possible combinations of passwords with the given length
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            if guess == target_password:
                return guess
    return None

# Attempt to decrypt the unhashed password
decrypted_password = brute_force_decrypt(unhashed_password, charset)

# Output the result
if decrypted_password:
    print(f"Password decrypted: {decrypted_password}")
else:
    print("Failed to decrypt the password.")
