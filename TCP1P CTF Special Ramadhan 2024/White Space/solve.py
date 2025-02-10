def readfile_and_createarray(filename):
    values = []
    with open(filename, 'r') as file:
        for line in file:
            values.append(line.rstrip('\n'))
    return values

filename = "output.txt"
arr = readfile_and_createarray(filename)

def dec(cipher, key_1, key_2):
    decrypted_text = ""
    lines = cipher
    for i, line in enumerate(lines):
        if (i % 2 == 0):
            decrypted_text += chr(len(line) // key_1)
        if (i % 2 == 1):
            decrypted_text += chr(len(line) // key_2)
    return decrypted_text

for key_1 in range(1, 65):
    for key_2 in range(1, 65):
        decrypted_text = dec(arr, key_1, key_2)
        if "TCP1P" in decrypted_text:
            print(f'key 1 = {key_1}\nkey 2 = {key_2}\n>> dcode: {decrypted_text}')
