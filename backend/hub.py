from Field import Field
from Drone import Drone
from job import Job
import db

class Hub:
    def __init__(self, name="hub"):
        self.name = name
        self.fields = []
        self.drones = []
        self.jobs = []
        self.jobIdCount = 0

    def newField(self, height, width, name):
        field = Field(height=height, width=width, name=name, db=db)
        i = field.insert_into_db()
        field.id = i
        self.fields.append(field)

    def newDrone(self, drone):
        self.drones.append(drone)
    
    def register(self, id):
        drone = Drone(None, id, db)
        drone.register()
        self.newDrone(drone)

    def newJob(self, dronesList, fieldId):
        drones = []
        for drone in self.drones:
            if dronesList.__contains__(drone.id): 
                drones.append(drone)

        self.jobIdCount += 1
        da_field = list(filter(lambda field: field.id == fieldId, self.fields))[0]
        job = Job(db=db, field=da_field, drones=drones, id=self.jobIdCount)
        self.jobs.append(job)
        job.insert_into_db()


    def deleteField(self, fieldId):
        for field in self.fields:
            if field.id == fieldId:
                print("Removing field")
                self.fields.remove(field)
                db.delete_field(field.id)
        return

    def deleteDrone(self, droneId):
        for drone in self.drones:
            if drone.id == droneId:
                self.drones.remove(drone)
        return

    def deletejob(self, jobId):
        for job in self.jobs:
            if job.id == jobId:
                self.jobs.remove(job)
                db.delete_job(job.id)
        return

    def getAllDrones(self):
        list = []
        for drone in self.drones:
            list.append(drone.to_json())
        return list

    def getDrones(self, ids):
        list = []
        for drone in self.drones:
            if ids.__contains__(drone.id):
                list.append(drone.to_json())
        return list

    def getAllField(self):
        list = []
        for field in self.fields:
            list.append(field.to_json())
        return list

    def getField(self, ids):
        list = []
        for field in self.fields:
            if ids.__contains__(field.id):
                list.append(field.to_json())
        return list

    def getName(self):
        return self.name

    def getHub(self):
        #db.getHub()
        hub = Hub()
        f1 = Field(height=10,width=5,name="first",id=1)
        hub.fields.append(f1)
        f2 = Field(height=20,width=10,name="sec",id=2)
        hub.fields.append(f2)

        hub.newDrone(Drone(hub.fields[0],"2de9e221-da40-4315-a08a-5f20929ae0d9"))
        hub.newDrone(Drone(hub.fields[1],"2de9e221-da40-4315-a08a-5f20929ae0d8"))
        return hub

    def updatePos(self, DroneId, x, y):
        for drone in self.drones:
            if drone.id == DroneId:
                drone.x = x
                drone.y = y
        db.updatePos(DroneId, x, y)

    def updateStatus(self, droneId, status):
        for drone in self.drones:

            if drone.id == droneId:
                drone.status = status
                db.updateStatus(droneId, status)
        
    def getjobs(self):
        joblist = []
        for job in self.jobs:
            f = job.to_json()
            joblist.append(f)
        return joblist
            
    def droneUpdate(self, drone_id):
        for job in self.jobs:
            for droneId in job.droneslist:
                if drone_id == droneId.id:
                    [x,y] = job.parth.getNextTile()
                    return {"hasJob": "true", "x": x, "y": y}
        return {"hasJob": "false"}

    def save_image(self, id, image):
        for drone in self.drones:
            if drone.id == id:
                drone.image = image
                drone.label = None
                return

    def getImage(self, id):
        for drone in self.drones:
            if drone.id == id:
                return {'id': id, 'image': drone.image, 'label': drone.label}
    
    def giveLabel(self, id, label):
        for drone in self.drones:
            if drone.id == id:
                drone.label = label
                return

def loadHub():
    hub = Hub()
    hub.fields = db.getAllField()
    hub.drones = db.getAllDrones(hub.fields)
    hub.jobs = db.getAllJobs(hub.fields, hub.drones)
    return hub