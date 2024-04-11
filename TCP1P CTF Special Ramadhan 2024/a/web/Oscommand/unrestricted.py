import string
wordlist = string.printable
blacklist = [';', '&', '|', '||', '&&', '>', '<', '(', ')', '{', '}', '', '', '\\', '\'', '"', '!', '', '?', '~', '#', '%', '+', ' ']
allowed = []

for i in wordlist:
    print(f'now char :   {i}')
    if i not in blacklist:
        allowed.append(i)
print(''.join(allowed))

