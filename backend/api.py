import requests
import base64
from PIL import Image
import io

url = 'http://localhost:5000/predictImage'
dirs = {"FreshBanana":"b", "RottenBanana":"rb", "FreshApples":"a", "RottenApples":"ra", "FreshOranges":"o", "RottenOranges": "ro"}
HOST = 'http://localhost:5000'



def whatIsThis(data):
    #base64data = base64.b64encode(data)
    print ('Sending API request: ', url)
    r = requests.post(url, data)
    print ('Received: ', r.status_code, r.text)

    return r.text

if __name__ == "__main__":
    with open('backend/a0.jpg', "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read())
    prediction = whatIsThis(encoded_string)
    print(prediction)

    

 