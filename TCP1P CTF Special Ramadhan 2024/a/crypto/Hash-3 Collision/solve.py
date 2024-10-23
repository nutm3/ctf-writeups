import itertools

def my_hash(string):
    sum = 0
    for char in string:
        sum += ord(char)
    sum = sum % (2 ** 24)
    return str(sum).encode().hex()

def bruteforce_hash(hash_output):
    with open("/usr/share/wordlists/rockyou.txt", "r", errors="ignore") as f:
        total_attempts = 0
        for line in f:
            word = line.strip()
            hashed_string = my_hash(word)
            total_attempts += 1
            print(f"Loop {total_attempts} > '{word}'")
            if hashed_string == hash_output:
                return word
    return "Not Found :("

hash_output = "32323931"  # Admin hash

matched_word = bruteforce_hash(hash_output)
print("Password real:", matched_word)
