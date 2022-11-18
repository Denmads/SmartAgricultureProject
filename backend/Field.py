import json

class Field:
    def __init__(self, hieght, width, name, id=-1):
        self.hieght = hieght
        self.width = width
        self.name = name
        self.id = id

    def __str__(self):
        return f"({self.id}){self.name}({self.hieght} by {self.width})"

    def to_json(self):
        return {"id":self.id, "name":f"{self.name}", "width":self.width, "hieght":self.hieght}

    def to_json_with_drones(self, hub):
        droneslist = []
        for drone in hub.drones:
            droneslist.append(drone.to_json())
            
        j = {"id":self.id, "name":f"{self.name}", "width":self.width, "hieght":self.hieght, "drones": json.dumps(droneslist)}
        return j

    def insert_into_db(self):
        db.save(f"INSERT INTO ff (Width, height, FieldName)VALUES({self.width}, {self.hieght}, {self.name})")
