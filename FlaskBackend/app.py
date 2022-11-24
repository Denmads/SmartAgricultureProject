from flask import Flask, request
import tensorflow as tf
from ModelHandler import predict
import base64

app = Flask(__name__)

@app.route("/")
def version():
    return f"<h1>tfVersion: {tf.version.VERSION}</h1>"

# curl -X POST -d @{ImageName}.jpg localhost:5000/predictImage 
# Takes base64encoded data
@app.route("/predictImage", methods=["POST"])
def predictImage():
    img_data = base64.decodebytes(request.get_data(as_text=True).encode("utf-8"))
    result = predict(img_data)
    return result

if __name__ == '__main__':
    app.run(debug=True)