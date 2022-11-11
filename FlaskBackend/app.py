from flask import Flask, request
import tensorflow as tf
from ModelHandler import predict
import base64



app = Flask(__name__)

@app.route("/")
def version():
    return f"<p>tfVersion: {tf.version.VERSION}</p>"

# curl -X POST -d @{ImageName}.jpg localhost:5000/processImage 
# Takes base64encoded data
@app.route("/predictImage", methods=["POST"])
def predictImage():
    img_data = base64.decodebytes(request.get_data())
    result = predict(img_data)
    return result

if __name__ == '__main__':
    app.run(debug=True)