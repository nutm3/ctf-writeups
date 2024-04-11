import string
import itertools
import jwt

cookie='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW5cbiJ9.ktryupDoqb9oeqZbhp7KrCrr0iGtk_VfRNpSdWfA93U'
def generate_words(min_length, max_length):
    words = []
    alphabet = 'replican'
    for length in range(min_length, max_length + 1):
        for word in itertools.product(alphabet, repeat=length):
            words.append(''.join(word))
    return words

if __name__ == "__main__":
    min_length = 1
    max_length = 8
    dictionary = generate_words(min_length, max_length)
#    JWT_SECRET = "replican"

    for JWT_SECRET in dictionary:
        try:
            decoded = jwt.decode(cookie, JWT_SECRET, algorithms=["HS256"])
            print("JWT_SECRET :", JWT_SECRET)
            print("Payload hasil dcode:", decoded)
            break
        except jwt.InvalidTokenError:
            print("JWT_SECRET not valid:", JWT_SECRET)
            continue
