dec = [84, 67, 80, 49, 80, 123, 99, 52, 99, 105, 78, 54, 95, 66, 51, 115, 97, 82, 95, 97, 108, 97, 83, 107, 52, 95, 109, 101, 82, 117, 115, 52, 75, 66, 105, 107, 49, 110, 95, 98, 48, 116, 116, 111, 77, 125]
decode = ''.join(chr(d) for d in dec)
print(f'Flag : {decode}')
