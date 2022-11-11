import time
import requests
import datetime
import concurrent.futures
import base64

HOST = 'http://localhost:8080'
API_PATH = '/predictImage'
ENDPOINT = HOST + API_PATH
MAX_THREADS = 30
CONCURRENT_THREADS = 200

with open("TestImages/FreshApples/a0.jpg", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read())

def send_api_request():
    print ('Sending API request: ', ENDPOINT)
    r = requests.post(ENDPOINT, encoded_image)
    print ('Received: ', r.status_code, r.text)

start_time = datetime.datetime.now()
print ('Starting:', start_time)

with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
    futures = [ executor.submit(send_api_request) for x in range (CONCURRENT_THREADS) ]
time.sleep(5)
end_time = datetime.datetime.now()
print ('Finished start time:', start_time, 'duration: ', end_time-start_time)
