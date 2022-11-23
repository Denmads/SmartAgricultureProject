from flask import Flask, request
from hub import Hub
import requests
import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
hub = Hub().getHub()


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
    dronesList = request.form.getList('drones') 
    fieldId = request.form.getList('field', type=int) 
    return hub.newJob(dronesList=dronesList, fieldId=fieldId)

@app.route('/field', methods=['POST'])
def createField():
    name = request.form.getList('name', type=string)
    width = request.form.getList('width', type=int)
    height = request.form.getList('height', type=int)
    hub.newField(height=height, width=width, name=name)

@app.route('/deletejob', methods=['POST'])
def deleteJob():
    ids = request.form.getList('job_ids', type=string)
    return hub.deletejob(ids)

@app.route('/deletefield', methods=['POST'])
def deleteField():
    ids = request.form.getList('field_ids', type=string)
    return hub.deletejob(ids)



@app.route("/getDronePosisions", methods=['POST'])
def getDronePosisions():
    ids = request.form.getList('drone_ids', type=string)
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
    ids = request.form.getList('drone_ids', type=string)
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
    drone_id = request.form.get('drone_id', type=string)
    hub.register(drone_id)
    return "200"

@app.route('/drone/updatestatus/')
def updateStatus():
    drone_id = request.form.getList('drone_id', type=string)
    status = request.form.getList('status', type=string)
    hub.updateStatus(drone_id, status)

@app.route('/drone/camera/', methods=['POST'])
def camera():
    image = request.form.getList('image', type=string)
    Drone.predictImage(image) 

@app.route('/drone/updatepos/', methods=['POST'])
def pos():
    drone_id = request.form.getList('drone_id', type=string)
    x = request.form.getList('x', type=int)
    y = request.form.getList('y', type=int)
    hub.updatePos(drone_id, x, y)
    return "200"

@app.route('/drone/update', methods=['POST'])
def isThereANewJob():
    drone_id = request.form.getList('drone_id', type=string)
    return hub.droneUpdate(drone_id)





app.run(host='0.0.0.0', port=3000)