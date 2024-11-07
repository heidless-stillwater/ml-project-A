import requests

API='https://id-digit-backend-svc-394099236728.europe-west2.run.app'
#
# API='http://localhost:5000/'

resp = requests.post(API, files={'file': open('eight.png', 'rb')})

print(resp.json())
