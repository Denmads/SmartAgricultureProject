from flask import Flask
from hub import Hub
import requests
import db

app = Flask(__name__)
hub = Hub().getHub()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/droneinfo")
def getDrones():
    return f"{hub.getAllDrones()}"

@app.route('/fields')
def getAllFields():
    return f"{hub.getAllField()}"

@app.route('/jobs')
def getJobs():
    return f"{hub.getjobs()}"

@app.route('/job', methods=['POST'])
def getJob():
    ids = request.form.getList('job_ids', type=string)
    return hub.getjob()

@app.route('/field', methods=['POST'])
def getField():
    ids = request.form.getList('field_ids', type=string)
    return hub.getfield(ids)

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
    drone_id = request.form.getList('drone_id', type=string)
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





app.run(port=3000)