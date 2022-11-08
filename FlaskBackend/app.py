from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This is a test :)</p>"

@app.route("/posttest", methods=["POST"])
def test():
    input_json = request.get_json(force=True)
    print('data from client:', input_json)
    dictToReturn = {'answer':42}