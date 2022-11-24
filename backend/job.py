import json
from parth import Parth

class Job:
    def __init__(self, db, drones = [], fieldId = -1, id=-1):
        self.id = id
        self.droneslist = drones
        self.fieldId = fieldId
        size = self.get_field_size(fieldId= fieldId)
        self.parth = Parth(x = size[0], y = size[1])
        self.db = db

    def __str__(self):
        return f"({self.id})"

    def to_json(self):
        return {"id":self.id, "drones":f"{self.to_json_with_drones}", "fields":f"{self.field}"}

    def to_json_with_drones(self, hub):
        droneslist = []
        for drone in hub.drones:
            droneslist.append(drone.to_json())
            
        j = {"id":self.id, "name":f"{self.name}", "width":self.width, "hieght":self.hieght, "drones": json.dumps(droneslist)}
        return j

    def get_field_size(self, fieldId):
        fields = self.db.getAllField()
        for field in fields:
            if field.id == fieldId:
                return [field.width, field.height]

    #not made 
    def insert_into_db(self):
        for drone in self.droneslist:
            self.db.insert_into_db(f"INSERT INTO job (jobId, DroneId, Fieldid) VALUES ({self.id}, '{drone}', {self.fieldId})")