import json

class Job:
    def __init__(self, drones = [], field = [], id=-1):
        self.id = id
        self.droneslist = drones
        self.field = field

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

    #not made 
    def insert_into_db(self):
        db.save(f"INSERT INTO ff (Width, height, FieldName)VALUES({self.width}, {self.hieght}, {self.name})")