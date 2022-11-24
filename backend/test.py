
from parth import Parth
from Drone import Drone
from Field import Field

if __name__ == "__main__":
    d = Field(height=300, width=200, name='test')
    a = d.insert_into_db()
    d.id = a