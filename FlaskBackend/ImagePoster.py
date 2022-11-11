import requests
import base64

url = 'http://localhost:5000/predictImage'
with open('TestImages/banan.jpeg', "rb") as img_file:
    encoded_string = base64.b64encode(img_file.read())

prediction = requests.post(url, data=encoded_string)

print(prediction.text)