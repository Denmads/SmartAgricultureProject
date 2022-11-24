import json
from parth import Parth

class Job:
    def __init__(self, db, field, drones = [], id=-1):
        self.id = id
        self.droneslist = drones
        self.field = field
        self.db = db
        [x, y] = self.get_field_size()
        self.parth = Parth(x = x, y = y)
        for drone in drones:
            drone.field = self.field

    def __str__(self):
        return f"({self.id})"

    def to_json(self):
        return {"id":self.id, "drones":self.to_json_with_drones(), "field":f"{self.field.id}"}

    def to_json_with_drones(self):
        droneslist = []
        for drone in self.droneslist:
            droneslist.append(drone.to_json())
            
        return droneslist

    def get_field_size(self):
        return [self.field.width, self.field.height]
     

    #not made 
    def insert_into_db(self):
        for drone in self.droneslist:
            self.db.insert_into_db(f"INSERT INTO job (jobId, DroneId, Fieldid) VALUES ({self.id}, '{drone.id}', {self.field.id})")