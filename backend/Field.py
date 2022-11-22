import json

class Field:
    def __init__(self, height, width, name, id=-1):
        self.height = height
        self.width = width
        self.name = name
        self.id = id

    def __str__(self):
        return f"({self.id}){self.name}({self.height} by {self.width})"

    def to_json(self):
        return {"id":self.id, "name":f"{self.name}", "width":self.width, "height":self.height}

    def to_json_with_drones(self, hub):
        droneslist = []
        for drone in hub.drones:
            droneslist.append(drone.to_json())
            
        j = {"id":self.id, "name":f"{self.name}", "width":self.width, "height":self.height, "drones": json.dumps(droneslist)}
        return j

    def insert_into_db(self):
        db.save(f"INSERT INTO ff (Width, height, FieldName)VALUES({self.width}, {self.height}, {self.name})")
