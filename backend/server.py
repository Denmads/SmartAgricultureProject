from flask import Flask
from hub import Hub
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getDrones")
def getDrones():
    hub = Hub().genData()
    return f"{hub.getAllDrones()}"

@app.route('/getDrones/', methods=['POST'])
def getSpeceficDrones():
    ids = request.form.getList('drone_ids', type=string)
    drones = []

    for id in ids:
        try:
            # get from database
            # drone = Drone.get(id)
            drones.append(drone)
        except:
            continue
    
    return drones

