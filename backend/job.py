import json
from parth import Parth

class Job:
    def __init__(self, db, drones = [], fieldId = -1, id=-1):
        self.id = id
        self.droneslist = drones
        self.fieldId = fieldId
        self.db = db
        [x, y] = self.get_field_size(fieldId=fieldId)
        self.parth = Parth(x = x, y = y)

    def __str__(self):
        return f"({self.id})"

    def to_json(self):
        return {"id":self.id, "drones":self.to_json_with_drones(), "field":f"{self.fieldId}"}

    def to_json_with_drones(self):
        droneslist = []
        for drone in self.db.getAllDrones():
            droneslist.append(drone.to_json())
            
        return droneslist

    def get_field_size(self, fieldId):
        fields = self.db.getAllField()
        for field in fields:

            print(field.id, "SPACE", fieldId)


            if field.id == fieldId:
                return [field.width, field.height]
        return [-1, -1]

    #not made 
    def insert_into_db(self):
        for drone in self.droneslist:
            self.db.insert_into_db(f"INSERT INTO job (jobId, DroneId, Fieldid) VALUES ({self.id}, '{drone}', {self.fieldId})")