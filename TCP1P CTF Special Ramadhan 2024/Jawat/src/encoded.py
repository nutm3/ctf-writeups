import jwt
jwtData = {"user": "admin"}
JWT_SECRET = "replican"
cookie = jwt.encode(jwtData, JWT_SECRET, algorithm='HS256')
print(f'cookie payload : {cookie}')
