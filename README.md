# Unhashed-Password-Decryption-Tool (Brute Force Attack)
I built a tool to demonstrate the dangers of weak, unhashed passwords and highlight the importance of secure password practices.
This code is only for dyscription "decrypt"


###Code Breakdown:
Input Variables:

unhashed_password = "abc123": The target password you're trying to crack.
charset: Set of lowercase letters and digits used for guessing combinations.
Brute-force Function:

The brute_force_decrypt function iterates over all possible combinations of the charset up to a given max_length (6 here).
For each combination, it checks if it matches the target password.
Output:

If the correct combination is found, the password is printed; otherwise, it reports failure.
This code highlights the risk of storing passwords unhashed and emphasizes the need for secure password practices.
