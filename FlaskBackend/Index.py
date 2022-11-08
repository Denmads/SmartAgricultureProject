from flask import Flask

app = Flask(__NNBackend__)

@app.route("/")
def hello_world():
    return "<p>This is a test :)</p>"