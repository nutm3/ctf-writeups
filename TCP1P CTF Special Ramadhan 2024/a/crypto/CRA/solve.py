from Crypto.Util.number import long_to_bytes
from sympy import cbrt

import os

c = ""
with open("output.txt", "r") as file:
    c = int(file.read())
m = cbrt(c)
print(long_to_bytes(m).decode())

