import codecs

c2_hex = "36470088ba16f05854a998fc562fa8749e8c26e5dfe0ab08a73bc0e18c86b70b3743038eb519be1555a68df8576aaf7c9ac726ff9ee1ea0fbd3ec7f0848ce2"
P2 = "dengan menyelesaikan tantangan keamanan dalam tim atau individu"
P2_hex = P2.encode().hex()

c2_byte = codecs.decode(c2_hex, 'hex')
P2_byte = codecs.decode(P2_hex, 'hex')

key = [a ^ b for a, b in zip(c2_byte, P2_byte)]

C1_hex = "315608cfba1cb15950afc1ed5f27ab7483c732e58be1a146b13fc2e78789e5403f470088ae12b91555a68fb9572fb57c99802cea8bffab08f331cbf2889af60d224b028eb5"
C1_hex = C1_hex[64:]
C2_hex = "06722dde8b03a00642a293cd5b15b37485b234d492a7a403be0fc5e783b7f3011c7d03dcb51fb55e42b78dd6533eba66c6b82cee8da7a412b234cfe8b29ba61326110392"
C2_hex = C2_hex[64:]

# Lakukan operasi XOR antara setiap elemen byte dari C1_hex dan kunci untuk mendapatkan P1_byte
P1_byte = [a ^ b for a, b in zip(codecs.decode(C2_hex, 'hex'), key)]

# Konversi P1_byte menjadi karakter ASCII
P1_ascii = ''.join([chr(byte) for byte in P1_byte])


print(f'Key : {key}, length : {len(key)}')
print(f'len C1_hex : {len(C1_hex)}, len C2_hex : {len(C2_hex)}')
print(f'Flag (2/2):, {P1_ascii}')
