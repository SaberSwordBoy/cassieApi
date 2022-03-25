import requests

url = "http://localhost:5000/getresponse"

while True:
    data = {"input": input(">>> ")}
    print(requests.post(url, data=data).json()['data']['response'])
