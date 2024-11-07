import requests

resp = requests.post("https://my-prediction-394099236728.europe-west2.run.app", files={'file': open('eight.png', 'rb')})
# resp = requests.post("http://localhost:5000/", files={'file': open('three.png', 'rb')})

print(resp.json())
