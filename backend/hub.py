from Field import Field
from Drone import Drone
import json

class Hub:
    def __init__(self, name="hub"):
        self.name = name
        self.fields = []
        self.drones = []

    def newField(self, field):
        self.fields.append(field)

    def newDrone(self, drone):
        self.drones.append(drone)

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
        hub.newField(Field(10,5,"first",1))
        hub.newField(Field(20,10,"sec",2))

        hub.newDrone(Drone(hub.fields[0],1))
        hub.newDrone(Drone(hub.fields[1],2))
        return hub

    def updatePos(self, DroneId, x, y):
        for drone in self.drones:
            if drone.id == DroneId:
                drone.x = x
                drone.y = y
        db.updatePos(DroneId, x, y)

    def updateStatus(self, status, droneId):
        for drone in self.drones:
            if drone.id == DroneId:
                drone.status = status
            
        db.updateStatus(status, droneId)
        
    def getjobs(self):
        joblist = []
        for field in self.fields:
            f = field.to_json_with_drones(self)
            joblist.append(f)
        return json.dumps(joblist)
            
            