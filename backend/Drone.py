from Field import Field

class Drone:

    def __init__(self, field, id):
        self.id = id
        self.assignField(field=field)

    def assignField(self, field=None):
        if field == None:
            self.x = -1
            self.y = -1
            self.field = Field(-1, -1, "None", -1)
            self.status = "assign field"
        else:
            self.field = field
            self.x = 0
            self.y = 0
            self.status = "waiting"

    def moveTo(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def changeStatus(self, status="waiting"):
        self.status = status

    def __str__(self):
        return f"drone {self.id} is on {self.field.name}({self.x}, {self.y}) with status {self.status}"

    def to_json(self):
        return {"id":f"self.id", "field":self.field.id, "x":self.x, "y":self.y, "status":self.status}
