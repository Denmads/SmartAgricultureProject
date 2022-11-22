from dataclasses import dataclass
from enum import Enum


class DroneStatus(Enum):
    OFF = "off"
    BOOTING = "booting"
    IDLE = "idle"
    WORKING = "working"
    HARVESTING = "harvesting"
    DONE = "done"

@dataclass
class MovePoint:
    x: int
    y: int
    speed: int # pixels / 5 seconds
    
    def get_x_move(self, time_ms: int, current_x: float):
        x_speed = (self.speed / 5000.0) * time_ms
        
        missing_dist = self.x - current_x
        return min(missing_dist, x_speed)
    
    def get_y_move(self, time_ms: int, current_y: float):
        y_speed = (self.speed / 5000.0) * time_ms
        
        missing_dist = self.y - current_y
        return min(missing_dist, y_speed)
    
    def reached_point(self, current_x: float, current_y: float):
        return current_x == self.x and current_y == self.y
        