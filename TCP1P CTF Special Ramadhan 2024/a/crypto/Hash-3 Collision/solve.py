import itertools

def my_hash(string):
    sum = 0
    for char in string:
        sum += ord(char)
    sum = sum % (2 ** 24)
    return str(sum).encode().hex()

def brute_force_hash(hash_output):
    with open("rockyou.txt", "r", errors="ignore") as f:
        total_attempts = 0
        for line in f:
            word = line.strip()
            hashed_string = my_hash(word)
            total_attempts += 1
            print(f"Perhitungan ke-{total_attempts}: Kata yang sedang dicoba: '{word}'")
            if hashed_string == hash_output:
                return word
    return "Tidak ditemukan"

hash_output = "32323931"  # Hasil output print yang diberikan

matched_word = brute_force_hash(hash_output)
print("Kata yang sesuai dengan hasil output hash adalah:", matched_word)
