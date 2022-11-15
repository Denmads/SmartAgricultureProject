from Field import Field
from Drone import Drone

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

    def genData(self):
        hub = Hub()
        hub.newField(Field(10,5,"first",1))
        hub.newField(Field(20,10,"sec",2))

        hub.newDrone(Drone(hub.fields[0],1))
        hub.newDrone(Drone(hub.fields[1],2))
        return hub

    def getName(self):
        return self.name

if __name__ == "__main__":
    hub = Hub.genData(Hub())
    

    print(hub.getAllDrones())

    for field in hub.fields:
        print(field.to_json())
    
    for drone in hub.drones:
        print(drone.to_json())