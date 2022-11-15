from flask import Flask
from hub import Hub
import requests

app = Flask(__name__)
hub = Hub().getHub()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getDrones")
def getDrones():
    return f"{hub.getAllDrones()}"

@app.route('/getDrones/', methods=['POST'])
def getSpeceficDrones():
    ids = request.form.getList('drone_ids', type=string)
    drones = []

    for id in ids:
        try:
            # get from database
            drone = db.getDrone(id)
            drones.append(drone)
        except:
            continue
    
    return drones

@app.route('/drone/register/')
def registerDrone():
    hub.register(id)
    return "200"

@app.route('/drone/status/')
def updateStatus():
    hub.updateStatus(id, status)

@app.route('/drone/camera/')
def camera():
    Drone.predictImage(image) 

@app.route('/drone/updatepos/')
def pos():
    hub.updatePos(id, x, y)
    return "200"





app.run(port=3000)