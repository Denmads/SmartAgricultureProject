from flask import Flask, request, jsonify
import tensorflow as tf
from ModelHandler import predict



app = Flask(__name__)

@app.route("/")
def version():
    return f"<p>tfVersion: {tf.version.VERSION}</p>"

@app.route("/posttest", methods=["POST"])
def test():
    input_json = request.get_json(force=True)
    print('data from client:', input_json)
    dictToReturn = {'answer':42}
    return jsonify(dictToReturn)

# curl -X POST -d @Hip-Flask.jpg localhost:5000/processImage 
@app.route("/processImage", methods=["POST"])
def processImage():
    # predict(request.get_data())
    result = predict(request.get_data())
    return result

if __name__ == '__main__':
    app.run(debug=True)