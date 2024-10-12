# Unhashed-Password-Decryption-Tool (Brute Force Attack)
I built a tool to demonstrate the dangers of weak, unhashed passwords and highlight the importance of secure password practices.
This code is only for dyscription "decrypt"

# Code Breakdown: for decrypting
Input Variables:

unhashed_password = "abc123": The target password you're trying to crack.
charset: Set of lowercase letters and digits used for guessing combinations.
Brute-force Function:

The brute_force_decrypt function iterates over all possible combinations of the charset up to a given max_length (6 here).
For each combination, it checks if it matches the target password.
Output:

If the correct combination is found, the password is printed; otherwise, it reports failure.
This code highlights the risk of storing passwords unhashed and emphasizes the need for secure password practices.

encryption part:-
To add encryption, you could implement something like the SHA-256 hash function to securely encrypt passwords. Here's an example of hashing with hashlib:
Unhashed Password:

unhashed_password = "abc123": This sets the password to be cracked.
Character Set:

charset = string.ascii_lowercase + string.digits: Defines the characters (lowercase letters and digits) that will be used for guessing the password.
Brute Force Function:

brute_force_decrypt(): The function loops through all possible combinations of characters with increasing lengths (up to 6), generated using itertools.product(). It checks each combination to see if it matches the target password.
Decryption Logic:

The loop generates combinations (e.g., "a", "b", "aa", "ab", etc.), and compares them to the target password.
Once a match is found, it returns the password and stops.
Output:

If the password is decrypted, the code prints the password; otherwise, it prints that decryption failed.

# Encryption Part:-
To provide encryption for this project, you can hash the password using a secure algorithm like SHA-256. This ensures that even if passwords are exposed, they cannot be easily cracked like the unhashed password example.


use a libery hashlib
import hashlib

# Hash a password using SHA-256
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

hashed_password = encrypt_password(unhashed_password)
print(f"Hashed password: {hashed_password}")
