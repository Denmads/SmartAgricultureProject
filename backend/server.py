from flask import Flask, request, json
from Drone import Drone
from hub import Hub, loadHub
import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
hub = loadHub()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/droneinfo")
def getDrones():
    return hub.getAllDrones()

@app.route('/fields')
def getAllFields():
    return hub.getAllField()

@app.route('/jobs')
def getJobs():
    return hub.getjobs()

@app.route('/job', methods=['POST'])
def createJob():

    data = json.loads(request.data)

    print(data)

    dronesList = data['drones']
    fieldId = int(data['field'])
    hub.newJob(dronesList=dronesList, fieldId=fieldId)
    return "200"

@app.route('/field', methods=['POST'])
def createField():

    data = json.loads(request.data)

    name = str(data['name'])
    width = int(data['width'])
    height = int(data['height'])

    hub.newField(height=height, width=width, name=name)
    return "200"

@app.route('/job', methods=['DELETE'])
def deleteJob():
    ids = request.args.get('id', type=int)
    hub.deletejob(ids)

    return "204"

@app.route('/field', methods=['DELETE'])
def deleteField():
    ids = request.args.get('id', type=int)
    hub.deleteField(ids)

    return "204"


@app.route("/getDronePosisions", methods=['POST'])
def getDronePosisions():
    ids = request.form.getList('drone_ids', type=str)
    drones = []

    for drone_id in ids:
        try:
            # get from database
            drone = db.getDrone(drone_id)
            drones.append(drone)
        except:
            continue
    
    return drones

@app.route('/getDrones/', methods=['POST'])
def getSpeceficDrones():
    ids = request.form.getList('drone_ids', type=str)
    drones = []

    for drone_id in ids:
        try:
            # get from database
            drone = db.getDrone(drone_id)
            drones.append(drone)
        except:
            continue
    
    return drones


@app.route('/drone/register/drone', methods=['POST'])
def registerDrone():

    data = json.loads(request.data)

    drone_id = data['id']
    hub.register(drone_id)
    return "200"

@app.route('/drone/updatestatus', methods=['POST'])
def updateStatus():

    data = json.loads(request.data)

    print(data)

    drone_id = str(data['drone_id'])
    status = str(data['status'])
    hub.updateStatus(drone_id, status)
    return "200"

@app.route('/drone/camera', methods=['POST'])
def camera():
    image = request.form.get('image', type=str)
    Drone.predictImage(image) 

@app.route('/drone/updatepos', methods=['POST'])
def pos():
    drone_id = request.form.get('drone_id', type=str)
    x = request.form.get('x', type=int)
    y = request.form.get('y', type=int)
    hub.updatePos(drone_id, x, y)
    return "200"

@app.route('/drone/update', methods=['POST'])
def isThereANewJob():

    data = json.loads(request.data)

    drone_id = str(data['drone_id'])
    return hub.droneUpdate(drone_id)

app.run(host='0.0.0.0', port=3000)