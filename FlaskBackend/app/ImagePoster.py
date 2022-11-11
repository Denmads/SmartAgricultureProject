import requests
import base64
import os

url = 'http://localhost:5000/predictImage'
dirs = {"FreshBanana":"b", "RottenBanana":"rb", "FreshApples":"a", "RottenApples":"ra", "FreshOranges":"o", "RottenOranges": "ro"}
# dirs = ["FreshBananas", "RottenBananas", "FreshApples", "RottenApples", "FreshOranges", "RottenOranges"]

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for _ in it:
            total += 1
    return total

right, wrong, predictions = 0, 0, []

for dir in dirs.keys():
    for i in range(get_dir_size(f'TestImages/{dir}')):
        img_path = f'TestImages/{dir}/{dirs[dir]}{i}.jpg'
        print(img_path)
        with open(img_path, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read())
        prediction = requests.post(url, data=encoded_string)
        predictions.append(prediction.text)
        if prediction.text == dir.lower():
            right +=1
        else: 
            print(f'{img_path} was wrongly predicted as {prediction.text}')
            wrong += 1

print(predictions)
print(f'Right: {right}')
print(f'Wrong: {wrong}')
print(f'Total: {right/(right+wrong)}')

#################### SINGLE POST REQUEST TEST ####################
# with open('TestImages/FreshBananas/b0.jpg', "rb") as img_file:
#     encoded_string = base64.b64encode(img_file.read())
# prediction = requests.post(url, data=encoded_string)
# print(prediction.text)