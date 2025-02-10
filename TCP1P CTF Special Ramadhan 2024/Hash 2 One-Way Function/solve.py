import random

flags = open("flags.txt", "r").read().splitlines()
hash_output = "32333934"  # hasil out

def my_hash(string):
    sum = 0
    for char in string:
        sum += ord(char)
    sum = sum % (2 ** 24)
    return str(sum).encode().hex()

for flag in flags:
    if my_hash(flag) == hash_output:
        print(f'Flag :  {flag}')
        break
